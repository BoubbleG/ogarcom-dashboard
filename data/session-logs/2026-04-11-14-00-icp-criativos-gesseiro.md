---
type: session
date: 2026-04-11
projeto: GESSEIRO-MASTER
assunto: transcrição de criativos + ICP MVT
---

# Sessão: 2026-04-11 — ICP + Roteiros dos Criativos

## Resumo
Transcrevemos automaticamente os 6 vídeos dos top criativos do Gesseiro Master usando Whisper + FFmpeg (instalados do zero nesta sessão). Com os scripts em mãos, executamos a Skill 1 — ICP MVT — e criamos o avatar estratégico completo do público, baseado 100% em dados reais de campanha (90 dias, 7 criativos, métricas de performance).

## Decisões
- Whisper (modelo `base`) + FFmpeg instalados via `python -m pip install openai-whisper` e `winget install Gyan.FFmpeg` — funcionando no PC atual
- Biblioteca de roteiros adicionada em `Skills/criativo-mvt/GESSEIRO-MASTER-CRIATIVOS.md` na seção `## Biblioteca de Roteiros — Scripts dos Criativos`
- ICP salvo em `Conhecimento/MVT/Projetos/GESSEIRO-MASTER/ICP/ICP.md` (pasta nova criada)
- AD13 transcrito direto do .txt — único com roteiro escrito originalmente
- AD40, AD7, AD48, AD36, AD47, AD49 transcritos via Whisper dos arquivos de vídeo

## Pendências
- [ ] Confirmar faixa etária exata e região predominante via breakdown do Meta Ads Manager
- [ ] Verificar se AD49 tem problema na página (CTR 4,23% mas ROAS 1,47x — hipótese de desalinhamento LP)
- [ ] Atualizar seção "Roteiros Aprovados" do GESSEIRO-MASTER-CRIATIVOS.md com hooks e ângulos confirmados
- [ ] Rodar Skill 2 — Concepção de Oferta com base no ICP gerado

## Aprendizados

### Sobre os criativos
- **AD40 vs AD36 — mesmo hook, ROAS completamente diferente:** AD36 revela o produto logo no início ("Eu utilizo o Gesseiro Master"), AD40 mantém curiosidade. Resultado: 2,04x vs 1,26x. **Regra validada: nunca nomear o produto no hook.**
- **AD47 — paradoxo do hook perfeito:** Hook Rate 59,3% (maior da conta) mas ROAS 1,53x. O hook pergunta "quanto dinheiro você perdeu?" e o corpo nunca responde — vai direto para a demonstração. **Regra: o corpo deve responder o que o hook prometeu.**
- **AD48, AD47, AD49 compartilham o mesmo corpo de script** — só o hook muda. O que separa performance é 100% o hook. Corpo validado, testar apenas novos hooks.
- **AD49 — CTR altíssimo (4,23%), ROAS baixo:** o hook de "diferença de 3k e 10k" gera muito clique mas a conversão quebra na página. Oportunidade: reescrever LP no ângulo de status/profissionalismo.
- **Estrutura vencedora (AD40 e AD48, ROAS > 2x):** Hook resultado/dor financeira → história pessoal com número concreto → "E é por isso que uso o [produto]" (no meio, não no início) → demo em 3 passos → benefícios extras → CTA duplo ("saiba mais" + "comenta 'eu quero'").

### Sobre o ICP
- **A dor real é financeira e invisível:** não é "perder obra" — é "trabalhar e não ver o lucro que deveria". O gesseiro faz a obra, cobra, recebe, mas o lucro some porque calculou errado.
- **O desejo oculto é status, não dinheiro:** AD49 com CTR 4,23% prova que comparação de renda (3k vs 10k) ativa identidade e status mais do que qualquer outro ângulo.
- **Objeção "não preciso disso" é racionalização:** o medo real é "vou comprar e não conseguir usar". Por isso demos de 3 passos simples convertem melhor.
- **Tom validado:** direto, de igual para igual, linguagem de obra — nunca "gestão financeira", sempre "fechar a obra", "dar o preço", "orçamento no WhatsApp".

### Técnico
- Whisper modelo `base` é suficiente para transcrição em português com boa qualidade
- FFmpeg path: `C:\Users\pc\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe`
- Para usar Whisper: `os.environ['PATH']` precisa incluir o diretório do ffmpeg antes de importar whisper

---

## Log Completo

### Arquivos modificados/criados
1. `G:\Meu Drive\OGARCOM\Skills\criativo-mvt\GESSEIRO-MASTER-CRIATIVOS.md` — adicionadas seções:
   - `## Biblioteca de Roteiros — Scripts dos Criativos` (7 entradas completas)
   - `## Insights de Roteiro — O que os scripts revelam` (6 insights com tabelas)
2. `G:\Meu Drive\OGARCOM\Conhecimento\MVT\Projetos\GESSEIRO-MASTER\ICP\ICP.md` — criado do zero com ICP completo (14 seções)

### Roteiros confirmados por criativo

| Criativo | Hook | Ângulo MVT | ROAS | Hook Rate |
|----------|------|-----------|------|-----------|
| AD40 | "Depois que eu comecei a usar isso aqui, eu não perdi mais nenhuma obra." | TRANSFORMAÇÃO | 2,04x | 48,3% |
| AD48 | "Essa obra aqui deu 10.000 reais. Se eu fizesse na mão, eu cobraria 7." | DOR-FINANCEIRA | 2,01x | 42,7% |
| AD13 | "Parceiro gesseiro, você sabia que 'depois eu mando o preço' faz perder 90% das obras?" | DOR | 1,69x | 28,4% |
| AD47 | "Me diz aí, quanto dinheiro você já perdeu fazendo orçamento só de cabeça?" | DOR-FINANCEIRA | 1,53x | 59,3% |
| AD49 | "Quer saber a diferença de um gesseiro que ganha R$3.000 e outro que ganha R$10.000?" | CURIOSIDADE+STATUS | 1,47x | 52,1% |
| AD7 | "Gesseiro, você ainda está perdendo tempo fazendo conta em papel de caderno?" | DOR | 1,37x | 35,0% |
| AD36 | "Depois que eu comecei a usar isso aqui, eu não perdi mais nenhuma obra." | TRANSFORMAÇÃO | 1,26x | 48,1% |

### ICP — Perfil central
- **Persona:** Fábio, 34 anos, gesseiro autônomo, aprende na prática, faz conta de cabeça, manda orçamento por mensagem de texto, já perdeu obra esperando para calcular
- **Dor principal:** perda financeira invisível — trabalha, entrega, mas o lucro some porque calculou errado
- **Desejo oculto:** ser levado a sério, ganhar mais sem baixar preço
- **Temperatura:** morno tendendo a quente
- **Nível de consciência:** consciente da dor + consciente da solução
