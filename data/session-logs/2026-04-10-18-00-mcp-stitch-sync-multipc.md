---
type: session
date: 2026-04-10
projeto: GERAL
assunto: MCP Stitch instalado + sincronização multi-PC + dashboard hospedada
---

# Sessão: 2026-04-10 — MCP Stitch + Multi-PC + Dashboard Live

## Resumo
Sessão focada em finalizar a infraestrutura completa do OGARCOM: dashboard hospedada no GitHub Pages com leitura real do vault, script de sincronização automática, MCP do Stitch instalado e configurado, e todo o sistema preparado para funcionar em múltiplos PCs via Google Drive.

## Decisões

- **Dashboard hospedada** em `https://BoubbleG.github.io/ogarcom-dashboard` — lê arquivos .md do vault via GitHub API em tempo real.
- **Script SINCRONIZAR.bat** criado em `G:\meu drive\ogarcom-dashboard\` — clique duplo copia os arquivos do vault para o repo e faz push automático para o GitHub.
- **Pasta ogarcom-dashboard movida para o Google Drive** (`G:\meu drive\ogarcom-dashboard\`) para sincronizar entre PCs automaticamente.
- **MCP do Stitch instalado** via `@_davideast/stitch-mcp` — Claude agora consegue criar projetos, gerar telas e buscar código HTML/CSS direto do Stitch sem o usuário abrir o navegador.
- **Chave de API do Stitch** salva no `~/.claude.json` com flag `-s user`.
- **Arquivo SETUP-NOVO-PC.md** criado em `System/` com todos os comandos necessários para configurar um novo PC — vai junto no Google Drive.

## Pendências

- [x] Rodar os 2 comandos MCP no notebook (Obsidian + Stitch) — arquivo `System/SETUP-NOVO-PC.md` ✓ 2026-04-10
- [x] Watcher automático instalado e testado ✓ 2026-04-10
- [ ] Testar o SINCRONIZAR.bat após mudanças reais no vault
- [ ] Preencher dados reais nos arquivos .md dos 3 projetos (Campanhas, Copy, Criativos, Página, Análises)
- [ ] Confirmar status dos entregáveis nos 3 projetos (Etapa 6)
- [ ] Testar capacidade do Claude de gerar design no Stitch diretamente

## Aprendizados

- O MCP do Stitch (`@_davideast/stitch-mcp`) funciona com API Key — não precisa de OAuth/gcloud. Instalação em 5 minutos.
- O terminal do Claude Code não suporta menus interativos com setas — para rodar `stitch-mcp init` é preciso usar CMD ou PowerShell normal.
- MCPs são locais por PC — precisam ser configurados uma vez em cada máquina. A chave API é a mesma.
- Tudo que está no Google Drive (`G:\meu drive\`) sincroniza automaticamente nos 2 PCs — vault, dashboard, scripts e setup.
- O `-s user` no `claude mcp add` salva em `~/.claude.json` (global no usuário), não no projeto.

---
## Log Completo

### Infraestrutura final do OGARCOM

**Dashboard:**
- URL: https://BoubbleG.github.io/ogarcom-dashboard
- Repo: https://github.com/BoubbleG/ogarcom-dashboard
- Leitura: GitHub API → arquivos `data/` no repo
- Atualização: `SINCRONIZAR.bat` → copia vault → git push

**MCPs configurados (PC de casa):**
```
claude mcp list:
- obsidian-vault  → ✓ Connected (npx obsidian-mcp)
- stitch          → ✓ Connected (HTTP + API Key)
- Figma           → ✓ Connected
- Magic Patterns  → ✓ Connected
```

**Para configurar no notebook:**
Ver `G:\meu drive\ogarcom\System\SETUP-NOVO-PC.md`

**Estrutura Google Drive:**
```
G:\meu drive\
├── ogarcom\                  ← Vault Obsidian (sincroniza automático)
│   ├── CLAUDE.md
│   ├── Session-Logs\
│   ├── Skills\
│   ├── System\
│   │   └── SETUP-NOVO-PC.md  ← novo
│   └── Conhecimento\MVT\Projetos\
└── ogarcom-dashboard\        ← Dashboard + Script (sincroniza automático)
    ├── SINCRONIZAR.bat
    ├── sync.ps1
    ├── index.html
    └── data\
```

**Capacidades do Claude com Stitch MCP:**
- `create_project` — criar projeto no Stitch
- `generate_screen_from_text` — gerar tela a partir de prompt
- `get_screen` — buscar tela existente
- `get_screen_code` — buscar HTML/CSS gerado
- `get_screen_image` — screenshot do design
- `build_site` — construir site completo

