---
type: session
date: 2026-04-10
projeto: GERAL
assunto: setup vault e dashboard
---

# Sessão: 2026-04-10 — Setup Vault e Dashboard

## Resumo
Sessão focada em organizar o vault OGARCOM, centralizar skills e construir uma dashboard visual no Obsidian. Ao final, iniciamos a criação de um dashboard web local usando Google Stitch.

## Decisões
- Skills centralizadas em `G:\Meu Drive\OGARCOM\Skills\` (pasta visível no vault, seguindo convenções)
- Cópia das skills também mantida em `.claude/commands\` para funcionamento nativo do Claude Code
- Dashboard principal criada em `System/Dashboards/HOME.md`
- Cada projeto ganhou um `INDEX.md` com checklist do funil MVT, pendências e bloco de prompt para iniciar conversa com o Claude
- Tema Obsidian escolhido: **AnuPpuccin** (escuro) + plugins **Style Settings** e **Banners**
- Dashboard web local será gerada via **Google Stitch** (gera HTML/CSS/JS a partir de prompt)
- Solução para leitura de arquivos locais: dados embutidos no HTML + script de atualização

## Pendências
- [ ] Adicionar imagens de banner nas pastas Assets de cada projeto
- [ ] Gerar dashboard web no Google Stitch com o prompt preparado
- [ ] Trazer código HTML gerado pelo Stitch para adaptação com dados reais
- [ ] Criar script que lê HOME.md e atualiza o HTML automaticamente
- [ ] Confirmar status dos entregáveis nos 3 projetos (campo ❓ no INDEX)

## Aprendizados
- Plugins do Obsidian rodam 100% local — não afetam tokens ou processamento do Claude
- `.claude/commands/` dentro do vault = skills funcionam automaticamente quando Claude está no diretório
- Google Stitch gera UI visual a partir de prompts — ideal para criar dashboards sem codar do zero
- Navegador não lê arquivos locais por segurança — solução: dados embutidos no HTML ou servidor local

---
## Log Completo

### Estrutura final do vault
```
OGARCOM\
  +Inbox\
  Conhecimento\
    Claude\
    Copy\
    Criativos\
    Analise-de-Dados\
    MVT\
      Projetos\
        GESSEIRO-MASTER\ (INDEX.md criado)
        PINTOR-PRO\ (INDEX.md criado)
        SINDICO-PRO\ (INDEX.md criado)
      Referencias\
      Tecnicas\
  Session-Logs\
  Skills\              ← novo, todas as skills aqui
  System\
    Dashboards\        ← HOME.md criado
    Templates\
  Calendar\
  Areas\
  CLAUDE.md
```

### Skills disponíveis em Skills/
**Sistema:** /resume, /compress, /preserve, /cleanup
**MVT:** /agente-mestre-mvt, /icp-mvt, /concepcao-oferta-mvt, /copywriter-pagina-mvt, /auditor-mvt, /direcao-design-mvt, /entregaveis-digitais-mvt, /presets-ui-mvt, /json-elementor-mvt, /json-elementor-importavel-mvt

### Funil MVT dos projetos (6 etapas)
1. ICP definido
2. Página criada
3. Criativos prontos
4. Testes de campanha
5. Testes de oferta (meta: 2-3 vendas)
6. Entregáveis criados

Status atual: os 3 projetos estão na etapa 5 concluída, etapa 6 pendente de confirmação.

### Prompt gerado para o Google Stitch
Prompt completo para gerar dashboard web escuro com: header OGARCOM, 3 cards de projeto com barra de progresso, pipeline MVT visual, grid de skills, painel de memória do Claude.
