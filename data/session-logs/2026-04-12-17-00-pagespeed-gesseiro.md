---
type: session
date: 2026-04-12
projeto: GESSEIRO-MASTER
assunto: otimização pagespeed página de vendas
---

# Sessão: 2026-04-12 — PageSpeed Gesseiro Master

## Resumo
Otimização completa de performance da página gesseiromaster.site/nova-gesseiro partindo de 49% no PageSpeed Mobile. Acesso via FTP ao servidor Hostinger. Score foi de 49% para 84% com as intervenções desta sessão. Trabalho ainda em andamento para chegar em 90+.

## Decisões
- **LiteSpeed Cache desativado** — estava em conflito com WP Rocket (dois plugins de cache simultâneos). Pasta renomeada para `litespeed-cache-DESATIVADO` via FTP RNFR/RNTO.
- **WP Rocket mantido como único cache** — já estava configurado como primário no .htaccess.
- **Mu-plugin criado** em `wp-content/mu-plugins/ogarcom-performance.php` — versão atual: 1.4.
- **font-display: auto → swap** corrigido diretamente no `post-1468.css` do Elementor (fontes INTER e ANTONIO estavam com `auto`).
- **Imagens da LCP otimizadas** — versão 768x1027 comprimida de 114KB para 67KB via Pillow (qualidade 72).

## Configurações WP Rocket aplicadas
- Cache mobile: ativado
- Minificar CSS: ativado
- Combinar CSS: desativado (HTTP/2)
- Minificar JS: ativado
- Combinar JS: desativado
- Adiar JS: ativado
- Execução retrasada de JS: ativado — exclusões adicionadas: `fbevents`, `clarity`, `utmify`, `pandavideo`
- LazyLoad imagens e iframes: ativado
- Dimensões de imagens: ativado
- DNS Prefetch adicionado: `//connect.facebook.net`, `//www.clarity.ms`, `//cdn.utmify.com.br`
- LazyLoad exclusões limpas (removidos `example-image.jpg` e `slider-image`)

## Mu-plugin ogarcom-performance.php (v1.4) — o que faz
1. Desativa wp-emoji (~20KB JS)
2. Limpa wp_head (RSD, wlwmanifest, generator, shortlink, adjacent posts)
3. Desativa XML-RPC
4. Remove CSS do Gutenberg (site usa Elementor)
5. Desativa wp-embed
6. Remove versão dos assets (segurança)
7. Preconnect para Facebook, Clarity e UTMify
8. Desativa Heartbeat no frontend
9. Defer em wp-emoji-release
10. Remove thumbnail medium_large
11. font-display: swap para INTER, ANTONIO, Manrope, Fira Code + filtro Elementor permanente
12. Preload da imagem LCP (gesseiromaster.site...6zwk...webp)
13. Remove lazy load da imagem LCP via `wp_get_attachment_image_attributes` (ID 1805, classe no-lazy, fetchpriority=high)
14. Cache de 1 ano para fontes via header PHP

## Pendências
- [ ] Limpar cache WP Rocket após última atualização de imagens
- [ ] Rodar PageSpeed final para confirmar score após otimização das imagens
- [ ] Verificar se o CLS (0.158) melhorou — causado por elemento Elementor com `_transform_scale_effect`
- [ ] Verificar se a fonte Inter (424KB TTF) ainda está bloqueando — considerar substituir por versão subset ou Google Fonts
- [ ] Imagem `pacote-completo-_7_-1-768x480.webp` (65KB) — usuário diz que já está no máximo de compressão possível

## Aprendizados
- **LiteSpeed + WP Rocket simultâneos** é problema crítico de performance — escolher um só. Para Hostinger com LiteSpeed server, os dois conflitam.
- **Fontes customizadas no Elementor** são salvas com nomes em MAIÚSCULO (INTER, ANTONIO) no CSS gerado — o override de font-display precisa usar os nomes corretos.
- **font-display no Elementor** fica no arquivo `wp-content/uploads/elementor/css/post-1468.css` — pode ser editado diretamente mas o filtro `elementor/custom_fonts/font_display` garante permanência após regeneração.
- **Perfmatters lazy load** usa a classe `no-lazy` para pular imagens — não tem filtro `perfmatters_lazy_load_skip_classes` (não existe). Correto é usar `wp_get_attachment_image_attributes` para adicionar a classe.
- **Imagens de depoimentos** (730x1352px JPG) pesadas — não foram otimizadas nesta sessão, podem ser próximo ganho.
- **Render-blocking do Elementor** (`hooks.min.js`, `i18n.min.js`, `post-4.css`, `post-1468.css`) é limitação do page builder — não dá para remover sem quebrar o site. Aceitar os ~300-570ms como custo do Elementor.

## Acesso FTP
- Host: ftp://77.37.127.6 | Usuário: u842176657 | Porta: 21
- Pasta: /domains/gesseiromaster.site/public_html/
- **TROCAR A SENHA após uso** — senha compartilhada na sessão

## Scores
| Momento | Score |
|---------|-------|
| Início da sessão | 49% |
| Após LiteSpeed desativado + WP Rocket configurado + mu-plugin v1.0 | 74% |
| Após mu-plugin v1.3 + font-display corrigido | 84% |
| Final (pendente verificação) | ? |

---
## Log Completo
Sessão focada em performance técnica da página de vendas do Gesseiro Master. Acesso completo via FTP ao servidor Hostinger. Foram feitas intervenções em: plugins (desativação do LiteSpeed Cache), configuração do WP Rocket (todas as abas), criação de mu-plugin com 14 otimizações, correção do font-display no CSS do Elementor, e compressão das imagens LCP via Pillow (Python). Score subiu de 49% para 84%. Trabalho continua para resolver CLS (0.158) e LCP (3.3s).
