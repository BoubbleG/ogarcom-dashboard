/**
 * OGARCOM — Fetch UTMify Data (Node.js)
 * Busca métricas reais (Greenn + Meta Ads) via UTMify MCP
 * Rode localmente pelo SINCRONIZAR.bat
 */

const https = require('https');
const fs    = require('fs');
const path  = require('path');

const TOKEN     = '8cjACwWYN7AjB8Kcub4CXv5kJyIiVgMG';
const DASHBOARD = '687d8aa585bf1434643becc6';
const RESOURCES = 'gs,gm,gg,gt,gu,gwe,ga,gp,gwa,gr,gtf,gpc,gcs';
const MCP_HOST  = 'mcp.utmify.com.br';
const MCP_PATH  = `/mcp/?token=${TOKEN}&resources=${RESOURCES}`;

const ACCOUNTS = {
  'GESSEIRO-MASTER': '1398408144771165',
  'PINTOR-PRO':      '1331372135233963',
  'SINDICO-PRO':     '2302574626902808',
};

function mcpCall(method, params) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ jsonrpc: '2.0', id: 1, method, params });
    const req  = https.request({
      hostname: MCP_HOST,
      path:     MCP_PATH,
      method:   'POST',
      headers:  {
        'Content-Type':   'application/json',
        'Accept':         'application/json, text/event-stream',
        'Content-Length': Buffer.byteLength(body),
      },
    }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch(e) { reject(new Error('Parse error: ' + data.slice(0, 200))); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

function cents(v) { return Math.round(v / 100 * 100) / 100; }

function dateRange() {
  const to   = new Date();
  const from = new Date(to - 30 * 24 * 60 * 60 * 1000);
  const fmt  = d => d.toISOString().slice(0, 10);
  return { from: fmt(from), to: fmt(to) };
}

async function main() {
  const range = dateRange();
  process.stdout.write(`  Buscando dados de ${range.from} ate ${range.to}...\n`);

  const resp = await mcpCall('tools/call', {
    name: 'get_meta_ad_objects',
    arguments: {
      dashboardId: DASHBOARD,
      dateRange:   range,
      level:       'account',
    },
  });

  if (resp.result?.isError) {
    throw new Error(resp.result.content[0].text);
  }

  const { results } = JSON.parse(resp.result.content[0].text);

  const contas = {};
  for (const acc of results) {
    const name = Object.entries(ACCOUNTS).find(([, id]) => id === acc.accountId)?.[0];
    if (!name) continue;

    contas[name] = {
      gasto:            cents(acc.spend),
      receita:          cents(acc.revenue),
      receita_bruta:    cents(acc.grossRevenue),
      lucro:            cents(acc.profit),
      roas:             Math.round(acc.roas * 100) / 100,
      roi:              Math.round(acc.roi * 100 * 100) / 100,
      cpa:              cents(acc.cpa),
      vendas:           acc.approvedOrdersCount,
      total_pedidos:    acc.totalOrdersCount,
      pendentes:        acc.pendingOrdersCount,
      reembolsos:       acc.refundedOrdersCount,
      receita_pendente: cents(acc.pendingRevenue),
      impressoes:       acc.impressions,
      cliques:          acc.inlineLinkClicks,
      ctr:              Math.round(acc.inlineLinkClickCtr * 100) / 100,
      cpm:              cents(acc.cpm),
      cpc:              cents(acc.costPerInlineLinkClick),
      visitas_pagina:   acc.landingPageViews,
      initiate_checkout: acc.initiateCheckout,
      taxa_meta:        cents(acc.metaAdsTax),
    };

    process.stdout.write(`  [OK] ${name}\n`);
  }

  const output = {
    atualizado: new Date().toISOString(),
    periodo:    'last_30d',
    fonte:      'utmify',
    contas,
  };

  const outPath = path.join(__dirname, '..', 'data', 'meta-ads.json');
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2));
  process.stdout.write(`  Salvo: data/meta-ads.json\n`);
}

main().catch(e => { process.stderr.write('ERRO: ' + e.message + '\n'); process.exit(1); });
