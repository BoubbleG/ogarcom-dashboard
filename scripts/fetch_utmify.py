"""
OGARCOM — Fetch UTMify Data
Busca métricas consolidadas (Greenn + Meta Ads) via UTMify MCP
"""

import urllib.request
import urllib.error
import json
import os
from datetime import datetime, timedelta

TOKEN     = os.environ["UTMIFY_TOKEN"]
DASHBOARD = "687d8aa585bf1434643becc6"
MCP_URL   = f"https://mcp.utmify.com.br/mcp/?token={TOKEN}&resources=gs,gm,gg,gt,gu,gwe,ga,gp,gwa,gr,gtf,gpc,gcs"

ACCOUNTS = {
    "GESSEIRO-MASTER": "1398408144771165",
    "PINTOR-PRO":      "1331372135233963",
    "SINDICO-PRO":     "2302574626902808",
}

def mcp_call(method, params):
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }).encode()
    req = urllib.request.Request(
        MCP_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def cents(v):
    return round(v / 100, 2)

def main():
    today = datetime.utcnow().date()
    date_from = str(today - timedelta(days=30))
    date_to   = str(today)

    print(f"  Buscando dados de {date_from} até {date_to}...")

    resp = mcp_call("tools/call", {
        "name": "get_meta_ad_objects",
        "arguments": {
            "dashboardId": DASHBOARD,
            "dateRange": {"from": date_from, "to": date_to},
            "level": "account"
        }
    })

    if resp.get("result", {}).get("isError"):
        raise Exception(resp["result"]["content"][0]["text"])

    raw_text = resp["result"]["content"][0]["text"]
    data = json.loads(raw_text)
    results = data["results"]

    contas = {}
    for account in results:
        acc_id = account["accountId"]
        name = next((n for n, i in ACCOUNTS.items() if i == acc_id), None)
        if not name:
            continue

        print(f"  [OK] {name}")
        contas[name] = {
            # Financeiro
            "gasto":            cents(account["spend"]),
            "receita":          cents(account["revenue"]),
            "receita_bruta":    cents(account["grossRevenue"]),
            "lucro":            cents(account["profit"]),
            "roas":             round(account["roas"], 2),
            "roi":              round(account["roi"] * 100, 2),
            "cpa":              cents(account["cpa"]),
            # Vendas
            "vendas":           account["approvedOrdersCount"],
            "total_pedidos":    account["totalOrdersCount"],
            "pendentes":        account["pendingOrdersCount"],
            "reembolsos":       account["refundedOrdersCount"],
            "receita_pendente": cents(account["pendingRevenue"]),
            # Alcance
            "impressoes":       account["impressions"],
            "cliques":          account["inlineLinkClicks"],
            "ctr":              round(account["inlineLinkClickCtr"], 2),
            "cpm":              cents(account["cpm"]),
            "cpc":              cents(account["costPerInlineLinkClick"]),
            "visitas_pagina":   account["landingPageViews"],
            "initiate_checkout": account["initiateCheckout"],
            "taxa_meta":        cents(account["metaAdsTax"]),
        }

    output = {
        "atualizado": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "periodo":    "last_30d",
        "fonte":      "utmify",
        "contas":     contas
    }

    os.makedirs("data", exist_ok=True)
    with open("data/meta-ads.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n  Salvo em data/meta-ads.json")
    print(f"  Atualizado: {output['atualizado']}")

if __name__ == "__main__":
    main()
