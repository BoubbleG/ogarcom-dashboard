---
type: session
date: 2026-04-10
projeto: GERAL
assunto: rebuild completo da dashboard com UTMify
tags: [dashboard, utmify, meta-ads, campanhas, analises]
---

# Sessão: 2026-04-10 — Dashboard UTMify Completo

## Resumo
Rebuild completo da dashboard OGARCOM para integrar dados reais do UTMify MCP em todos os níveis: selector de período (hoje/ontem/3d/7d/30d), seção Meta Ads com dados por período, e drawer de projeto com tabs Campanhas e Análises populadas com dados reais. Script `fetch_utmify.cjs` reescrito para buscar todos os períodos + campanhas em paralelo. Infraestrutura de sync local via `SINCRONIZAR.bat` funcionando.

## Decisões
- **UTMify em vez de Meta API direta** — UTMify consolida Greenn (checkout) + Meta Ads num único endpoint, dados mais completos e sem precisar gerir token Meta
- **Dados buscados localmente** — GitHub Actions bloqueado pela UTMify (403). Solução: rodar `fetch_utmify.cjs` via `SINCRONIZAR.bat` no PC e fazer push
- **fetch_utmify.cjs** (extensão .cjs obrigatória) — package.json tem `"type":"module"`, então arquivos `.js` são ESM. Script CJS precisa da extensão `.cjs`
- **5 períodos + campanhas em paralelo** — `Promise.all([hoje, ontem, 3d, 7d, 30d, campanhas])` no fetch, JSON salvo com estrutura `{ periodos: {...}, campanhas: {...}, contas: d30 }`
- **Campainha data por projeto** — `ADS_DATA.campanhas[projectId]` com campos: nome, status (ACTIVE/PAUSED), gasto, receita, lucro, roas, vendas, impressoes, cliques, ctr, cpa
- **Tab Análises** — 6 cards (CPA, ROAS, Vendas, Gasto, Receita, Lucro) + tabela comparativa com os 5 períodos lado a lado
- **Tab Campanhas** — 2 tabelas separadas (ativas/pausadas) com colunas: Nome, Status, Gasto, ROAS, Vendas, CTR, CPA
- **Fallback para markdown** — quando UTMify não disponível, drawer usa dados do vault (.md)

## Pendências
- [ ] Preencher vault: `COPY.md`, `CRIATIVOS.md`, `ESTRUTURA-PAGINA.md` dos 3 projetos
- [ ] Rodar SINCRONIZAR.bat para atualizar `meta-ads.json` com dados mais recentes
- [ ] Testar dashboard ao vivo após sync — verificar tabs Campanhas e Análises nos 3 projetos
- [ ] Avaliar se precisa adicionar selector de período no drawer (atualmente fixo em 30d para análises)

## Aprendizados
- UTMify MCP retorna valores em **centavos** — dividir por 100 para BRL. Funções `cents()` e `fmt()` lidam com isso
- UTMify **bloqueia IPs do GitHub Actions** — dados de produção só via execução local
- `package.json` com `"type":"module"` quebra `require()` — qualquer script CJS precisa de extensão `.cjs`
- Tokens no `meta-ads.json` público eram um risco — sanitizar mensagens de erro para não expor `access_token=...`
- `git pull` antes de `commit + push` é obrigatório no sync.ps1 para evitar push rejected
- `Split-Path` no PowerShell retorna null com hashtables aninhadas — usar array `@(origem, destino)` com `$arq[0]/$arq[1]`

---
## Log Completo

### Estrutura do meta-ads.json (gerado por fetch_utmify.cjs)
```json
{
  "atualizado": "2026-04-10T...",
  "fonte": "utmify",
  "periodos": {
    "hoje":  { "GESSEIRO-MASTER": {...}, "PINTOR-PRO": {...}, "SINDICO-PRO": {...} },
    "ontem": { ... },
    "3d":    { ... },
    "7d":    { ... },
    "30d":   { ... }
  },
  "campanhas": {
    "GESSEIRO-MASTER": [ { nome, status, gasto, receita, lucro, roas, vendas, impressoes, cliques, ctr, cpa } ],
    "PINTOR-PRO":      [ ... ],
    "SINDICO-PRO":     [ ... ]
  },
  "contas": { ...igual a periodos.30d... }
}
```

### Contas UTMify
- TOKEN: `8cjACwWYN7AjB8Kcub4CXv5kJyIiVgMG`
- DASHBOARD: `687d8aa585bf1434643becc6`
- GESSEIRO-MASTER: account `1398408144771165`
- PINTOR-PRO: account `1331372135233963`
- SINDICO-PRO: account `2302574626902808`

### Arquivos modificados nesta sessão
- `G:\meu drive\ogarcom-dashboard\index.html` — rebuild completo: period selector, renderMetaAds por período, drawer campanhas/análises com dados reais
- `G:\meu drive\ogarcom-dashboard\scripts\fetch_utmify.cjs` — reescrito para 5 períodos + campanhas
- `G:\meu drive\ogarcom-dashboard\sync.ps1` — corrigido Split-Path, git pull, chamada ao fetch_utmify.cjs
- `G:\meu drive\ogarcom-dashboard\.github\workflows\fetch-meta-ads.yml` — desabilitado (UTMify bloqueia Actions)

### Status das campanhas (últimos 30d, aprox.)
- GESSEIRO-MASTER: 2 ACTIVE + 1 PAUSED
- PINTOR-PRO: 1 ACTIVE + 3 PAUSED
- SINDICO-PRO: 0 ACTIVE + 5 PAUSED
