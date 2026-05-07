# AGENTS.md — TPV Self-Service Sorveteria

> Arquivo de orientação para agentes de codificação. A linguagem principal do projeto é o **português (pt-BR)**.

---

## Visão Geral do Projeto

Este projeto é uma **landing page estática e demonstrativa** para um sistema de TPV (Terminal de Ponto de Venda) self-service destinado à *Sorveteria Sabadell Nord*. Ele funciona como uma apresentação comercial e protótipo interativo do fluxo de pedidos em um kiosk.

**Características principais:**
- Arquivo único: `tpv_sorveteria_v2.html`.
- Página 100% frontend, sem backend próprio neste repositório.
- Inclui uma **simulação interativa de kiosk** (tablet roxo na seção "Demo Interativa") onde o usuário pode navegar por telas de pedido: idioma → base do sorvete → sabores → carrinho → pagamento → confirmação.
- Também apresenta mockups visuais de um Dashboard de Cozinha e um Dashboard Administrativo.

> **Nota importante:** o arquivo atual é uma **proposta/protótipo de apresentação**, não o sistema completo em produção. O documento descreve uma arquitetura futura (Flutter, Supabase, VeriFactu), mas o código existente se limita a este HTML estático.

---

## Stack Tecnológico

O projeto não possui gerenciador de pacotes (nenhum `package.json`, `pyproject.toml`, `Cargo.toml`, etc.). Todas as dependências são carregadas via CDN:

| Recurso | Origem |
|---------|--------|
| CSS utilitário | [Tailwind CSS v3](https://cdn.tailwindcss.com) |
| Ícones | [Font Awesome 6.4.0](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css) |
| Fonte tipográfica | [Google Fonts — Poppins](https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap) |
| Gráficos (importado, não utilizado no código atual) | [Chart.js](https://cdn.jsdelivr.net/npm/chart.js) |

- **Linguagem:** HTML5 + CSS3 (embed) + JavaScript vanilla (embed).
- **Não há:** framework JS reativo, build step, bundler, transpiler, testes automatizados, ou servidor backend neste repositório.

---

## Estrutura do Projeto

```
Projeto Ideias sorveteria/
└── tpv_sorveteria_v2.html   ← único arquivo do projeto
```

O arquivo `tpv_sorveteria_v2.html` contém:
1. **`<head>`** — metadados, importações de CDN e bloco `<style>` com animações customizadas e utilidades visuais.
2. **`<body>`** — landing page dividida em seções semânticas:
   - Hero (apresentação do sistema).
   - Análise Elo Wallaby (comparativo de hardware).
   - Demo Interativa (tablet cliente + tablet admin).
   - Dashboard da Cozinha (mockup estático).
   - Sistema de Administração Total (cards de funcionalidades futuras).
   - Orçamento Completo (tabela de preços).
   - CTA / Footer.
3. **`<script>`** — lógica da demo interativa: navegação entre telas do kiosk, seleção de sabores, cálculo de total e confirmação de pedido.

---

## Como Executar

Como se trata de um arquivo HTML estático, basta abri-lo em qualquer navegador moderno. Não requer servidor local, mas se preferir:

```bash
# Com Python (exemplo)
python -m http.server 8000
# Acesse http://localhost:8000/tpv_sorveteria_v2.html
```

Ou simplesmente abra o arquivo diretamente no navegador.

---

## Convenções e Estilo de Código

- **Indentação:** 4 espaços (tanto em HTML, CSS quanto JS).
- **Classes CSS:** mistura de utilitários do Tailwind e classes customizadas definidas no `<style>` (ex: `.gradient-bg`, `.hover-scale`, `.demo-tablet`).
- **Nomenclatura JS:** funções e variáveis em português, estilo `camelCase`.
- **IDs das telas:** prefixo `tela` (ex: `telaInicial`, `telaCardapio`, `telaSabores`).
- **IDs de elementos interativos:** prefixo descritivo (ex: `sabor-vainilla`, `btnContinuar`, `resumoPedido`).

### Padrão de navegação entre telas (JavaScript)

A demo utiliza um padrão manual de troca de visibilidade:

```javascript
function esconderTodas() {
    document.getElementById('telaInicial').classList.add('hidden');
    // ... demais telas
}

function mostrarTela(id) {
    esconderTodas();
    document.getElementById(id).classList.remove('hidden');
    document.getElementById(id).classList.add('fade-in');
}
```

Se for expandir a demo, mantenha esse padrão ou migre para um framework reativo, pois não há estado de roteamento real.

---

## Testes

**Não há testes automatizados** neste projeto. A validação é 100% manual:

1. Abra o arquivo no navegador.
2. Role até a seção "Demo Interativa do Sistema".
3. Clique em "Iniciar Pedido" no tablet roxo.
4. Simule um pedido completo: escolha base → escolha 1-3 sabores → verifique o carrinho → clique em pagar → confirme a tela de sucesso.
5. Verifique se o botão "Novo Pedido" retorna à tela inicial e limpa o estado.

---

## Considerações de Segurança

- **Não há dados sensíveis** hardcoded no HTML (apenas mockups de preços e nomes de sabores).
- **Não há comunicação com backend** real neste arquivo; toda a lógica é cliente-side e em memória.
- Se futuramente for implementar o backend descrito no documento (Supabase, VeriFactu, AEAT), será necessário:
  - Gerenciar chaves de API em variáveis de ambiente (nunca no frontend público).
  - Implementar autenticação e autorização no dashboard admin.
  - Garantir conformidade com a LGPD/GDPR para dados de clientes.
  - Validar integrações fiscais (VeriFactu) em ambiente de homologação antes de produção.

---

## Notas para Agentes

- Este projeto é um **ponto de partida visual e conceitual**. Qualquer modificação deve respeitar o tom de apresentação comercial e o idioma **português (pt-BR)**.
- Se o usuário solicitar "adicionar backend", "criar app Flutter" ou "implementar dashboard admin", lembre-se de que esses componentes **não existem ainda** no repositório — você estará criando algo novo, e não editando código existente.
- Para mudanças na demo interativa, prefira manter a simplicidade do JavaScript vanilla, a menos que o usuário peça explicitamente por um framework ou arquitetura diferente.
