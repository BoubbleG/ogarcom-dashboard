# OGARCOM — Memória Permanente

## Quem sou eu
Trabalho com marketing digital focado em ofertas **low ticket**.
Meu método de trabalho é o **MVT**: oferecer uma solução simples para uma dor forte, de forma clara, objetiva e tangível — resolvendo a dor real do lead.

## Meus Projetos
| Projeto | Nicho | Status |
|---|---|---|
| GESSEIRO MASTER | Gesseiros | Ativo |
| PINTOR PRO | Pintores | Ativo |
| SÍNDICO PRO | Síndicos | Ativo |

## Método MVT — Como eu penso
- **M** — A solução precisa ser simples e direta
- **V** — O valor percebido precisa ser claro e tangível
- **T** — A oferta resolve uma dor forte e específica do lead

Ao criar qualquer copy, criativo ou campanha, sempre verificar:
1. A dor está clara?
2. A solução é simples e objetiva?
3. O resultado é tangível (o lead consegue imaginar)?

## Estrutura do Vault
- `G:\Meu Drive\OGARCOM\+Inbox` — ideias rápidas, capturas do dia
- `G:\Meu Drive\OGARCOM\Conhecimento\MVT\Projetos\` — cada projeto com campanhas, copy, criativos e análises
- `G:\Meu Drive\OGARCOM\Conhecimento\` — técnicas, referências e aprendizados
- `G:\Meu Drive\OGARCOM\Session-Logs\` — histórico de sessões com Claude
- `G:\Meu Drive\OGARCOM\Skills\` — todas as skills disponíveis (buscar aqui quando uma skill for chamada)

## Convenções
- Datas: YYYY-MM-DD
- Nomes de arquivo: MAIUSCULO-COM-HIFEN.md
- Todo arquivo novo começa com frontmatter

## Frontmatter Padrão
```
---
type: campanha | copy | criativo | analise | ideia | conhecimento
date: YYYY-MM-DD
projeto: GESSEIRO-MASTER | PINTOR-PRO | SINDICO-PRO | GERAL
status: rascunho | ativo | pausado | concluido | arquivado
tags: []
---
```

## Decisões & Aprendizados
<!-- /preserve adiciona aqui automaticamente -->

### 2026-04-10 — MCP Stitch + Infraestrutura Multi-PC

- **MCP do Google Stitch instalado** via `@_davideast/stitch-mcp` com API Key. Claude consegue criar projetos, gerar telas, buscar código HTML/CSS e screenshots direto no Stitch sem o usuário abrir o navegador. Capacidades: `create_project`, `generate_screen_from_text`, `get_screen_code`, `get_screen_image`, `build_site`.
- **Infraestrutura multi-PC completa** — tudo que importa está no Google Drive (`G:\meu drive\`): vault Obsidian, dashboard, scripts. Qualquer alteração sincroniza automaticamente nos 2 PCs.
- **Pasta ogarcom-dashboard** movida para `G:\meu drive\ogarcom-dashboard\` — script SINCRONIZAR.bat funciona em qualquer PC com Google Drive.
- **Dashboard hospedada e ao vivo** em `https://BoubbleG.github.io/ogarcom-dashboard` — lê arquivos .md do vault via GitHub API em tempo real.
- **Script SINCRONIZAR.bat** em `G:\meu drive\ogarcom-dashboard\` — clique duplo copia vault → faz push GitHub → dashboard atualiza em ~1 min.
- **SETUP-NOVO-PC.md** em `System/` com todos os comandos para configurar novo PC. MCPs precisam ser configurados uma vez por máquina — a chave API do Stitch é a mesma.
- **Terminal do Claude Code não suporta menus interativos** — para rodar `stitch-mcp init` usar CMD ou PowerShell normal do Windows.

### 2026-04-10 — Dashboard Web + MCP + Estrutura dos Projetos

- **MCP do Obsidian instalado** via `npx obsidian-mcp "G:\meu drive\ogarcom"` — sem plugin no Obsidian, lê direto do filesystem. Claude consegue ler, criar e editar arquivos do vault dentro da conversa. Servidor configurado como `obsidian-vault` no Claude Code.
- **Obsidian instalado no PC** — versão 1.12.7, vault apontado para `G:\Meu Drive\OGARCOM`.
- **Estrutura dos projetos expandida** — cada projeto agora tem 5 arquivos base: `Campanhas/CAMPANHAS.md`, `Copy/COPY.md`, `Criativos/CRIATIVOS.md`, `Pagina/ESTRUTURA-PAGINA.md` (pasta nova), `Analises/ANALISES.md`. Caminho real dos projetos: `Conhecimento/MVT/Projetos/NOME/`.
- **Dashboard web construída** — arquivo em `G:\meu drive\ogarcom-dashboard\index.html`. Hospedada em `https://BoubbleG.github.io/ogarcom-dashboard`. Tecnologia: HTML + CSS + JS vanilla + Lucide CDN. Cobre 100% do vault (projetos, pipeline, skills MVT + sistema, session logs, saúde da memória, base de conhecimento, inbox, calendar).
- **Fluxo de design da dashboard** — Google Stitch = designer (gera protótipo visual) → Claude = programador (converte para HTML funcional e adiciona lógica).
- **GitHub Pages para hospedagem** — username: BoubbleG. URL futura: `https://BoubbleG.github.io/ogarcom-dashboard`. Próximo passo: criar repo e conectar GitHub API para leitura automática do vault.
- **Skills de sistema** agora visíveis na dashboard separadas das skills MVT (4 cards verdes: /resume, /compress, /preserve, /cleanup).

### 2026-04-10 — Setup do Vault

- **Skills centralizadas em `G:\Meu Drive\OGARCOM\Skills\`** — sempre buscar aqui quando uma skill for chamada. Cópia também em `.claude/commands/` para funcionamento nativo.
- **Dashboard principal em `System/Dashboards/HOME.md`** — ponto de entrada do vault. Tem visão geral dos projetos, skills, memória do Claude e acesso rápido.
- **Cada projeto tem `INDEX.md`** em `Conhecimento/MVT/Projetos/NOME/INDEX.md` com checklist do funil MVT, pendências e bloco de prompt para iniciar conversa com o Claude.
- **Funil MVT tem 6 etapas fixas:** ICP → Página → Criativos → Testes de Campanha → Testes de Oferta (meta: 2-3 vendas) → Entregáveis. Status atual: os 3 projetos concluíram etapa 5, etapa 6 pendente.
- **Dashboard web local via Google Stitch** — fluxo: Stitch gera HTML/CSS/JS → Claude adapta com dados reais → script atualiza quando HOME.md mudar.

## Como o Claude deve se comportar

### Antes de criar qualquer coisa
Nunca sair criando sem contexto suficiente. Sempre que faltar informação, fazer perguntas uma de cada vez até entender:
1. **Qual é o problema real** que precisa ser resolvido
2. **Para quem** é (qual projeto, qual público)
3. **Qual o resultado esperado** (o que seria perfeito pra você)
4. **O que você NÃO quer** que aconteça

Se a pergunta do usuário for vaga, responder com perguntas — não com suposições.

### Quando o usuário estiver tentando criar algo (copy, criativo, campanha, planejamento, oferta)
Ativar o protocolo completo antes de qualquer entrega:

1. **Verificar contexto** — se faltar qualquer um dos 4 pontos acima, parar e perguntar. Apontar exatamente o que falta e como enviar.
2. **Não supor nada** — nenhum dado inventado, nenhuma suposição sobre público, dor ou resultado.
3. **Aplicar filtro MVT** — o que está sendo criado passa nos 3 critérios? Se não, apontar o que está fraco antes de entregar.
4. **Sugerir o melhor caminho** — se existir ferramenta, técnica ou abordagem (conhecida ou não) que resolva melhor, sugerir. Sem restrição de ferramenta.
5. **Nunca entregar pela metade** — se não dá para fazer com qualidade com o contexto disponível, pedir mais antes de criar.

Referência completa: `G:\Meu Drive\OGARCOM\Conhecimento\Claude\como-trabalhar-com-o-claude.md`

### Quando o usuário não souber explicar tecnicamente
Traduzir automaticamente o que o usuário descreveu em linguagem simples para a ação técnica correta. Nunca exigir que o usuário use termos técnicos.

### Padrão de qualidade — Modo Rigoroso
Nunca aceitar respostas vagas ou "mais ou menos". Sempre exigir o melhor:
- Se a resposta do usuário for superficial, perguntar de novo com mais profundidade
- Se uma copy, criativo ou ideia não passar no filtro MVT, apontar o que está fraco e pedir refazer
- Se faltar clareza na dor, no público ou no resultado — não avançar sem resolver isso antes
- Sempre questionar: "Isso está realmente bom ou só está ok?"
- Preferir fazer menos e fazer perfeito do que fazer muito e fazer mediano

### Comportamento Obrigatório do Claude
- Sempre que terminar algo complexo (copy, campanha, análise, decisão importante), avisar:
  > "💾 Quer salvar essa sessão? Digite `/compress` para não perder nada."
- Sempre que a conversa estiver longa (mais de 20 mensagens), lembrar:
  > "💾 Já conversamos bastante. Recomendo salvar com `/compress` antes de continuar."
- Ao iniciar qualquer sessão sem `/resume` ter sido rodado, perguntar:
  > "Quer carregar o contexto anterior? Digite `/resume`."

## Skills Disponíveis
Todas as skills ficam em `G:\Meu Drive\OGARCOM\Skills\`. Quando o usuário chamar uma skill, ler o arquivo correspondente nessa pasta antes de executar.

### Skills de Sistema
- `/resume` — carrega contexto ao iniciar sessão
- `/compress` — salva sessão filtrando ruído
- `/preserve` — atualiza esta memória permanente
- `/cleanup` — remove logs antigos e consolida

### Skills MVT
- `/agente-mestre-mvt` — agente mestre do método MVT
- `/auditor-mvt` — audita copy/oferta pelo filtro MVT
- `/concepcao-oferta-mvt` — concepção de ofertas
- `/copywriter-pagina-mvt` — escreve páginas de venda
- `/direcao-design-mvt` — direção de design
- `/entregaveis-digitais-mvt` — criação de entregáveis
- `/icp-mvt` — definição do cliente ideal
- `/json-elementor-mvt` — geração de JSON para Elementor
- `/json-elementor-importavel-mvt` — JSON importável para Elementor
- `/presets-ui-mvt` — presets de interface
