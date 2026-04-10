---
type: session
date: 2026-04-09
projeto: GERAL
assunto: setup-inicial
---

# Sessão: 2026-04-09 — Setup Inicial do OGARCOM

## Resumo
Primeira sessão. Configuramos todo o sistema OGARCOM do zero — estrutura de pastas no Google Drive, vault no Obsidian, CLAUDE.md com contexto completo e skills de memória no Claude Code.

## Decisões
- Pasta mãe: `G:\Meu Drive\OGARCOM` (Google Drive como backup automático)
- Vault do Obsidian aponta para essa pasta
- Claude Code deve ser sempre aberto dentro de `G:\Meu Drive\OGARCOM`
- Skills criadas: `/resume`, `/compress`, `/preserve`, `/cleanup`
- Claude deve ser rigoroso, exigir qualidade e nunca aceitar respostas vagas
- Claude deve fazer perguntas antes de criar qualquer coisa quando faltar contexto
- Claude deve lembrar de salvar sessão após tarefas complexas ou conversas longas

## Estrutura criada
```
G:\Meu Drive\OGARCOM\
├── +Inbox\
├── Projetos\
│   ├── GESSEIRO-MASTER\ (Campanhas, Criativos, Copy, Analises, Assets)
│   ├── PINTOR-PRO\      (Campanhas, Criativos, Copy, Analises, Assets)
│   └── SINDICO-PRO\     (Campanhas, Criativos, Copy, Analises, Assets)
├── Conhecimento\
│   ├── MVT\ (Tecnicas, Referencias)
│   ├── Copy\
│   ├── Criativos\
│   └── Analise-de-Dados\
├── Session-Logs\
├── System\ (Templates, Dashboards)
├── Calendar\ (Daily, Weekly, Monthly)
└── CLAUDE.md
```

## Aprendizados
- Usuário trabalha com marketing digital low ticket, método MVT
- Projetos ativos: GESSEIRO MASTER, PINTOR PRO, SÍNDICO PRO
- Usuário prefere explicações simples sem termos técnicos
- Contexto é tudo — quanto mais contexto, melhor a resposta da IA
- Skills ficam em `C:\Users\pc\.claude\commands\`

## Pendências
- [ ] Instalar plugin Local REST API no Obsidian
- [ ] Configurar MCP Server obsidian-mcp no settings.json
- [ ] Testar fluxo completo: /resume → trabalho → /compress
- [ ] Definir fluxo de campanhas para estruturar melhor as pastas

## Log desta sessão
Configuração completa do sistema OGARCOM. Leitura do guia Reddit sobre Claude Code + Obsidian. Discussão sobre automação de memória, filtro de ruído, como fazer bons prompts e filosofia de trabalho com IA.
