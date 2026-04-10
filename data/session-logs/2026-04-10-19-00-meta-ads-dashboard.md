---
type: session
date: 2026-04-10
projeto: GERAL
assunto: Watcher automático + integração Meta Ads na dashboard
---

# Sessão: 2026-04-10 — Meta Ads + Watcher Automático

## Resumo
Sessão focada em duas frentes: (1) automação completa do watcher de vault com inicialização no boot do Windows, (2) integração da Meta Ads API na dashboard — criação do workflow GitHub Actions, script Python de coleta, e seção visual na dashboard com todas as métricas.

## Decisões

- **Watcher automático instalado** — `WATCHER-SILENCIOSO.vbs` + `INSTALAR-STARTUP.bat` em `G:\meu drive\ogarcom-dashboard\`. Roda em background, sem janela, inicia automaticamente com o Windows. Qualquer `.md` salvo no vault sincroniza a dashboard em ~5 segundos.
- **CLAUDE.md adicionado ao sync** — `sync.ps1` atualizado para copiar `CLAUDE.md` para `data/CLAUDE.md` no repo da dashboard.
- **Meta Ads API integrada** — workflow GitHub Actions `fetch-meta-ads.yml` roda a cada 6 horas e salva métricas em `data/meta-ads.json`.
- **IDs corretos das contas descobertos** via script de debug (`scripts/debug_token.py`). Os IDs do print estavam errados.
- **Token Meta Ads atualizado** no GitHub Secrets com permissões corretas: `ads_read`, `read_insights`, `ads_management`.
- **Seção Meta Ads Performance** adicionada na dashboard (entre Active Projects e Pipeline). Mostra 3 cards (um por projeto) com 16 métricas cada.

## IDs Corretos das Contas
| Projeto | Conta | ID |
|---|---|---|
| GESSEIRO-MASTER | CA 01 GESSEIRO MASTER | 1398408144771165 |
| PINTOR-PRO | CA 02 PINTOR PRO | 1331372135233963 |
| SINDICO-PRO | CA 03 SÍNDICO PRO | 2302574626902808 |

## Estado Atual da Integração
- ✅ Workflow criado e rodando (`.github/workflows/fetch-meta-ads.yml`)
- ✅ Script Python criado (`scripts/fetch_meta_ads.py`)
- ✅ IDs corretos configurados
- ✅ Token com permissões certas no GitHub Secrets
- ✅ Dados reais no repo — `data/meta-ads.json` com dados de GESSEIRO MASTER (R$5.219 gastos, ROAS 3.91x)
- ✅ Seção visual criada no `index.html` com `fetchJson()` usando TextDecoder
- ⏳ Verificar se a dashboard está exibindo os dados (aguardando cache do GitHub Pages limpar)

## Pendência Principal — O QUE FALTA VERIFICAR NO NOTEBOOK

### 1. Verificar se a dashboard está mostrando os dados
Acesse: **https://BoubbleG.github.io/ogarcom-dashboard**
- Use aba anônima (Ctrl+Shift+N) para evitar cache
- Deve aparecer seção **"Meta Ads Performance"** com 3 cards
- Cada card mostra: Gastos, Lucro, ROI, ROAS, CPA, Vendas, Impressões, CPM, Cliques, CPC, CTR, Visitas, CPV, Init. Checkout, CPI, ICR

### 2. Se ainda aparecer "Sem dados" ou branco
Rodar o workflow manualmente:
1. Acesse **github.com/BoubbleG/ogarcom-dashboard**
2. Aba **Actions** → **"Fetch Meta Ads Data"** → **"Run workflow"**
3. Aguarda ~30 segundos
4. Recarrega a dashboard com Ctrl+Shift+R

### 3. Se aparecer erro no workflow
Me manda o log do passo **"Buscar dados do Meta Ads"**.

### 4. Token expira em ~60 dias
O token do Meta Ads expira. Quando parar de funcionar:
1. Ir em **developers.facebook.com/tools/explorer**
2. Gerar novo token com: `ads_read`, `read_insights`, `ads_management`
3. Atualizar em GitHub → Settings → Secrets → `META_ACCESS_TOKEN`

## Estrutura de Arquivos Criados Nesta Sessão
```
G:\meu drive\ogarcom-dashboard\
├── WATCHER.ps1                         ← watcher file system
├── WATCHER-SILENCIOSO.vbs              ← inicia sem janela
├── INICIAR-WATCHER.bat                 ← inicia com janela (debug)
├── INSTALAR-STARTUP.bat                ← instala no boot do Windows
├── scripts\
│   ├── fetch_meta_ads.py               ← coleta dados do Meta Ads
│   └── debug_token.py                  ← diagnostica token/contas
└── .github\workflows\
    └── fetch-meta-ads.yml              ← workflow automático (6h)
```

## Métricas Disponíveis na Dashboard (por projeto)
**Financeiro:** Gastos, Lucro, ROI, ROAS, CPA, Vendas
**Alcance:** Impressões, CPM, Cliques, CPC, CTR, Visitas de Página
**Conversão:** CPV, Initiate Checkout, CPI, ICR

## Aprendizados
- O token gerado no Graph API Explorer é pessoal — precisa das permissões `ads_read`, `read_insights`, `ads_management` marcadas antes de gerar
- Os IDs exibidos no Business Manager não correspondem aos IDs da API — usar `/me/adaccounts` para listar os IDs reais
- `escape()/decodeURIComponent()` quebra quando o JSON tem URLs longas com caracteres especiais — usar TextDecoder é mais robusto
- Token dura ~60 dias — renovar antes de expirar
- O GitHub Pages pode demorar até 10 minutos para refletir mudanças no `index.html`
