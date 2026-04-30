---
type: session
date: 2026-04-15
projeto: SINDICO-PRO
assunto: copy primeira dobra + biblioteca de landing pages
---

# Sessão: 2026-04-15 — LP Síndico + Biblioteca de Componentes

## Resumo
Sessão focada em duas frentes: (1) criação da copy da primeira dobra da página do Síndico Pro com base no ICP v2.0 validado, e (2) construção de uma biblioteca completa de componentes HTML+CSS reutilizáveis para Landing Pages low ticket.

---

## Decisões

- **ICP Síndico Pro** lido do arquivo `F:\Usarios\Downloads\ICP_Sindico_v2_Validado.docx` — validado com 150+ comentários reais do YouTube. Referência permanente para copy do projeto.
- **Produto Síndico Pro** confirmado: Kit com 15 documentos prontos em `F:\Usarios\Desktop\SINDICO\KIT SINDICO PRO`
- **Tom da copy definido:** direto, pessoal ("você"), sem perguntas, afirmações de erro e consequência
- **Ângulo da primeira dobra:** dinheiro + medo de processo + conflito com morador
- **Biblioteca de LPs criada** em `G:\Meu Drive\OGARCOM\Conhecimento\Landing-Pages\`
- **Regra permanente:** sempre que um HTML for criado ou recebido → salvar `index.html` + `mockup.html` automaticamente

---

## Copy da Primeira Dobra — Versão Final Aprovada

**H1:**
> "Você está gerindo o condomínio do jeito errado — e isso está saindo do seu bolso."

**H2:**
> "Prestador sem contrato pode te processar. Inadimplente sem notificação formal não paga. Morador sem regulamento faz o que quer. E quando qualquer um desses vira processo — é o seu nome lá. E às vezes, é o seu dinheiro que paga."

**H3:**
> "O Kit Síndico Pro tem os 15 documentos que você precisava ter desde o primeiro dia — prontos para baixar e usar agora."

**CTA:**
> "Quero meu Kit Síndico Pro agora →"

---

## Biblioteca de Landing Pages — O que foi criado

**Localização:** `G:\Meu Drive\OGARCOM\Conhecimento\Landing-Pages\`

**Arquivos de referência:**
- `ESTRUTURA-MASTER.md` — ordem dos blocos e função estratégica
- `GUIA-DESIGN.md` — resolução 1200px, breakpoints, CSS variables, tipografia
- `MOCKUPS-CANVA.md` — repositório de links do Canva por projeto

**11 componentes HTML+CSS** (cada um com `index.html` + `style.css` + `mockup.html`):

| # | Componente |
|---|---|
| 01 | Hero (primeira dobra) |
| 02 | Demonstrativo de produto |
| 03 | Pack / Bundle |
| 04 | Dor / Agitação |
| 05 | Prova Social |
| 06 | Oferta / Preço |
| 07 | Garantia |
| 08 | FAQ (accordion JS puro) |
| 09 | CTA Final |
| 10 | Botões (5 variações) |
| 11 | Vitrine Carrossel infinito (3 fileiras LTR/RTL) |

O componente 11 foi adicionado a partir de um HTML de referência enviado pelo usuário (omanualdoenem.com) — recriado limpo sem Swiper/Elementor, CSS animation puro.

---

## ICP Síndico Pro — Pontos-chave para copy

**Dois perfis:**
- Síndico orgânico (voluntário): urgência alta, problema já aconteceu, medo de processo
- Síndico profissional: quer captar clientes, se formou mas não sabe prospectar

**3 dores centrais para copy:**
1. Medo de processo + responsabilidade pessoal (financeira)
2. Inadimplente sem notificação correta → dinheiro perdido
3. Morador sem regulamento → conflito semanal

**Gatilhos mais fortes:** segurança jurídica, caos herdado, praticidade ("baixe e use hoje")

**Tom validado:** direto, pessoal, "você", afirmações de erro e consequência — sem perguntas

**Frases reais da persona:**
- "Me tornei síndico há pouco tempo, estou sucedendo uma gestão de 10 anos. Está difícil."
- "O jardineiro precisa ter contrato? Quais os riscos que eu corro?"
- "Fui eleito síndico em condomínio que há 13 longos anos não tinha assembleia."

---

## Pendências

- [ ] Criar copy do Bloco 2 (Dor/Agitação) da página do Síndico Pro
- [ ] Tirar prints dos documentos do Kit para usar no componente vitrine-carrossel
- [ ] Preencher mockup.html do Hero com as cores reais do Síndico Pro
- [ ] Salvar ICP do Síndico Pro dentro da pasta do projeto em `Conhecimento/MVT/Projetos/SINDICO-PRO/`

---

## Aprendizados

- Copy com **afirmações diretas de erro** converte melhor que perguntas para o público síndico — ele já sabe que tem problema, não precisa ser questionado
- **Micro-contextos específicos** ("Prestador sem contrato pode te processar. Inadimplente sem notificação não paga.") geram identificação muito mais forte que afirmações genéricas
- Biblioteca de componentes com `mockup.html` separado do `index.html` é o fluxo correto — um para adaptar, um como referência funcional
- Carrossel infinito com CSS animation puro (sem Swiper) é mais leve e sem dependência — usar sempre que possível
