---
type: session
date: 2026-04-10
projeto: GERAL
assunto: instalação e configuração do MCP da Utmify
---

# Sessão: 2026-04-10 — Utmify MCP Setup

## Resumo
Sessão curta focada em configurar o MCP da Utmify no Claude Code. MCP instalado com sucesso via HTTP transport, 13 recursos habilitados. Definida convenção de salvar análises de campanha nos arquivos ANALISES.md de cada projeto no Drive. Memória permanente iniciada.

## Decisões
- **MCP da Utmify instalado** via `claude mcp add utmify --transport http [URL]` — transport HTTP, 13 recursos ativos (gs, gm, gg, gt, gu, gwe, ga, gp, gwa, gr, gtf, gpc, gcs)
- **Análises de campanha** devem ser salvas nos arquivos `ANALISES.md` de cada projeto — nunca criar arquivo separado, sempre acumular com seção datada
- **Memória permanente criada** em `C:/Users/pc/.claude/projects/G--Meu-Drive-OGARCOM/memory/` com referência do MCP e feedback sobre análises

## Pendências
- [ ] Reiniciar Claude Code para ativar o MCP da Utmify
- [ ] Testar ferramentas do MCP após reinício
- [ ] Rodar SINCRONIZAR.bat para atualizar meta-ads.json com dados recentes
- [ ] Testar dashboard ao vivo — tabs Campanhas e Análises nos 3 projetos
- [ ] Preencher vault: COPY.md, CRIATIVOS.md, ESTRUTURA-PAGINA.md dos 3 projetos

## Aprendizados
- MCP da Utmify precisa ser configurado uma vez por máquina — comando salvo na memória para reinstalar em novo PC
- UTMify bloqueia GitHub Actions (403) — dados só via execução local com SINCRONIZAR.bat
- Arquivos .js com package.json "type":"module" quebram require() — scripts CJS precisam extensão .cjs

---
## Log Completo

### MCP Instalado
- **Nome:** utmify
- **URL:** `https://mcp.utmify.com.br/mcp/?token=8cjACwWYN7AjB8Kcub4CXv5kJyIiVgMG&resources=gs,gm,gg,gt,gu,gwe,ga,gp,gwa,gr,gtf,gpc,gcs`
- **Comando de instalação:**
```bash
claude mcp add utmify --transport http "https://mcp.utmify.com.br/mcp/?token=8cjACwWYN7AjB8Kcub4CXv5kJyIiVgMG&resources=gs,gm,gg,gt,gu,gwe,ga,gp,gwa,gr,gtf,gpc,gcs"
```

### Recursos do MCP
| Código | Função |
|--------|--------|
| gs | Get Sales |
| gm | Get Metrics |
| gg | Get Goals |
| gt | Get Traffic |
| gu | Get UTMs |
| gwe | Get Website Events |
| ga | Get Analytics |
| gp | Get Products |
| gwa | Get Website Analytics |
| gr | Get Reports |
| gtf | Get Traffic Sources |
| gpc | Get Paid Channels |
| gcs | Get Campaign Stats |

### Convenção de Análises
- GESSEIRO MASTER: `G:\meu drive\ogarcom\Conhecimento\MVT\Projetos\GESSEIRO-MASTER\Analises\ANALISES.md`
- PINTOR PRO: `G:\meu drive\ogarcom\Conhecimento\MVT\Projetos\PINTOR-PRO\Analises\ANALISES.md`
- SINDICO PRO: `G:\meu drive\ogarcom\Conhecimento\MVT\Projetos\SINDICO-PRO\Analises\ANALISES.md`
