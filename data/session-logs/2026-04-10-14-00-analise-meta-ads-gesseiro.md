---
type: session
date: 2026-04-10
projeto: GESSEIRO-MASTER
assunto: analise completa meta ads + estrutura campanhas
---

# Sessão: 2026-04-10 — Análise Meta Ads + Estrutura de Campanhas

## Resumo
Análise completa das métricas do Gesseiro Master via Utmify (últimos 7 e 15 dias). Auditoria cirúrgica de todas as campanhas, conjuntos e criativos da conta `act_1398408144771165`. Definição da estrutura correta de campanhas baseada nas diretrizes do Meta Ads 2026 (Andromeda). Guia completo salvo no Obsidian.

---

## Métricas — Últimos 15 dias (27/03 a 10/04/2026)

| Métrica | Valor |
|---|---|
| Faturamento Bruto | R$ 6.942,69 |
| Investimento | R$ 4.358,58 |
| Lucro Líquido | R$ 2.061,08 |
| ROAS | 1,59x |
| Margem | 32,1% |
| CPA | R$ 14,20 |
| Vendas aprovadas | 307 |

**Queda na semana 2 (04-10/04):** ROAS caiu de ~1,69x para 1,46x. Lucro caiu de R$ 1.438 para R$ 622. Sinal de fadiga de criativos.

---

## Campanhas Ativas

### CBO — `[VENDAS] - [TESTES] - [CBO] - [3-2-2] - [ADS - (LAB)]`
- ID: `120240415657520177`
- Budget diário: R$ 100
- ROAS 15 dias: 1,66x | Margem: 35,1% | CPA: R$ 13,45

### ABO — `[VENDAS] - [LAB] - [ABO] - [3-2-2]`
- ID: `120241349763020177`
- Budget por conjunto
- ROAS 15 dias: 1,53x | Margem: 28,9% | CPA: R$ 15,03

---

## Criativos Vencedores (manter e proteger)

| Criativo | Campanha/Conjunto | ROAS | CPA | Margem |
|---|---|---|---|---|
| **AD51** | ABO — conjunto AD51 | 2,29x | R$ 10,34 | 53,9% |
| **AD48** | CBO — conjunto PACK AUD | 2,02x | R$ 10,02 | 47,3% |
| **AD40 - HOOK CURIOSIDADE** | CBO — conjunto TESTE | 2,03x | R$ 10,70 | 47,7% |

---

## Pausas Executadas (feitas pelo usuário no Gerenciador)

**CBO — Conjunto PACK AUD:**
- AD47 pausado (ROAS 1,04, margem -8,9%)

**CBO — Conjunto TESTE:**
- AD41, AD42, AD44, AD45 pausados (0 vendas)

**CBO — Conjunto CONTROLE (conjunto inteiro pausado):**
- ID: `120240790784360177`
- Criativos: AD3, AD7, AD31, AD36, AD40, AD48
- Motivo: Hook rates baixos (11-31%), R$ 65 gastos com apenas 3 vendas

**ABO — Conjunto AD49 pausado:**
- ID: `120241758410250177`
- AD49 pausado (ROAS 1,25, margem 11%)

---

## Estrutura Definida

### Papel de cada campanha
- **ABO = Laboratório** — testa criativos novos com R$ 30/dia por conjunto
- **CBO = Escala** — só roda criativos validados (estrutura 1-1-X)

### Critério de validação (ABO → CBO)
- ROAS > 1,8x + mínimo 5 vendas em 7 dias = migra para CBO
- Menos de 3 vendas em 7 dias = pausa e descarta

### Como escalar budget (CBO)
- Máximo +20% por vez
- Aguardar 3-4 dias entre aumentos
- Nunca escalar com ROAS em queda

---

## Decisões Tomadas

- Estrutura ABO/CBO validada e definida como padrão permanente
- AD51 identificado como melhor criativo — candidato a aumentar budget na ABO (+20% = R$ 60/dia)
- Problema de AD48 rodando em 3 lugares ao mesmo tempo (CBO PACK AUD + CBO CONTROLE + ABO) — resolvido com pause do conjunto CONTROLE
- Sistema de produção de criativos: gravar a cada 2 semanas, 3 variações por sessão, 1 ângulo por vez
- Guia completo de Meta Ads salvo em `Conhecimento/META-ADS-ESTRUTURA-COMPLETA.md`

---

## Pendências

- [ ] Aumentar orçamento do AD51 (ABO) em 20% — de R$ 50 para R$ 60/dia
- [ ] Subir AD51 no conjunto PACK AUD da CBO (melhor criativo da estrutura)
- [ ] Produzir 2-3 criativos novos para o conjunto PACK AUD (CBO está com poucos criativos ativos)
- [ ] Validar se AD49 e AD46 (CBO) merecem continuar após limpeza — reavaliar em 7 dias
- [ ] Criar sistema de nomenclatura de criativos: `GM-AD[num]-ANGULO-DATA`
- [ ] Replicar estrutura ABO/CBO para Pintor Pro e Síndico Pro

---

## Aprendizados

- **Andromeda (out/2025):** algoritmo do Meta agora escolhe o criativo certo para cada pessoa — criativo é o novo targeting, público amplo funciona melhor que segmentado
- **Estrutura 1-1-X no CBO:** 1 campanha, 1 conjunto, vários criativos — melhor estrutura para o Andromeda
- **Fase de aprendizado:** 50 conversões/semana por conjunto para sair da fase. Qualquer mudança > 20% de budget reseta
- **ABO antes da CBO:** nunca colocar criativo novo diretamente na CBO com vencedores — o algoritmo ignora. Validar na ABO primeiro
- **Frequência > 2,0** = sinal de saturação — produzir criativos novos antes de a campanha morrer
- **AD3 com Hook Rate 11,3%** = pior criativo identificado. Hook abaixo de 25% = pausa imediata

---

## Referências Salvas

- `Conhecimento/META-ADS-ESTRUTURA-COMPLETA.md` — guia completo de estrutura, teste e escala no Meta Ads 2026
