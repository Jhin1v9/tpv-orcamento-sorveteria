# PROMPT MASTER EXTRAORDINÁRIO — ECOSSISTEMA TPV SORVETERIA

> **Objetivo:** Transformar o ecossistema TPV Sorveteria de "demo funcional" para "produto competitivo" baseado nas melhores referências de mercado mundial.

---

## 🎯 CONTEXTO DO PROJETO

**Empresa:** NEXO DIGITAL (Jhin1v9 Tech)
**Cliente:** Sorveteria em Sabadell, Espanha
**Stack:** React 18 + TypeScript + Vite + Tailwind CSS + Supabase (PostgreSQL + Auth + Realtime + Storage)
**Mobile:** Capacitor (Android) + PWA
**Status atual:** Demo funcional, orçamento aprovado, aguardando fechamento

### Apps do Ecossistema (4 apps)

| App | Linhas | Score vs Mercado | Diagnóstico |
|-----|--------|-----------------|-------------|
| **Cliente** (PWA) | ~3.300 | **58/100** | Mais maduro; falta loyalty/reorder |
| **Kiosk** (TPV autoatendimento) | ~1.924 | **52/100** | UX linda, mas não monetiza (sem upsell/hardware) |
| **Admin** (Back-office) | ~1.274 | **48/100** | Só mostra dados; não toma decisões |
| **KDS** (Cozinha/Disp. Board) | ~287 | **42/100** | Bottleneck operacional; não escala multi-estação |
| **Média** | ~6.785 | **50/100** | Funciona para demo; 2-3 gerações atrás dos líderes |

### Arquitetura .brain (P1-P6)

```
P1: Sync Engine (Supabase Realtime)          ✅ Funcional
P2: Menu Service (cálculo de preços)         ✅ Funcional
P3: Offline Layer (SQLite + Service Worker)  ⚠️ Parcial
P4: Notification Service (Web Push)        ⚠️ Preparado mas não usado
P5: Loyalty Engine                           ❌ Inexistente
P6: Analytics Service (Mixpanel/Google)      ❌ Inexistente
```

---

## 🔬 ANÁLISE COMPETITIVA — MELHORES DO MUNDO

### Referências Primárias

#### 1. Starbucks Mobile App (Score: 95/100)
- **Loyalty Rewards:** Programa de fidelidade com estrelas, tiers (Green/Gold), recompensas personalizadas
- **One-tap Reorder:** "Pedir de novo" em 1 toque com histórico completo
- **Push Notifications:** Promoções geo-targeted, status de pedido, ofertas personalizadas por behavior
- **Mobile Order & Pay:** Pedido antecipado + pagamento mobile + pick-up na loja
- **Personalização:** Drinks customizados salvos, favoritos, recomendações por clima/hora
- **Gamification:** Challenges sazonais, double-star days, birthday rewards

#### 2. McDonald's App (Score: 93/100)
- **Upselling Inteligente:** "Quer batata média por +€1?" — aumenta ticket 15-30%
- **AI Menu Optimization:** Itens sugeridos baseados em horário, clima, histórico
- **Drive-thru Integration:** Pedido mobile + pick-up no drive-thru
- **MyMcDonald's Rewards:** Programa de pontos simplificado
- **Deal Carousel:** Ofertas personalizadas baseadas em LTV

#### 3. Toast POS (Score: 91/100)
- **Toast AI (2025):** Predictive labor scheduling, auto-reorder de ingredientes
- **Menu Engineering:** "Magic Quadrant" — o que manter/cortar baseado em margem + velocidade
- **Ingredient-Level Inventory:** Deduz tomate por pizza vendida em tempo real
- **Labor Tracking:** Integração com 7shifts, scheduling, clock-in/out
- **Real-time Reporting:** Dashboards com drill-down, comparação YoY
- **RBAC:** Roles granular (owner/manager/server/cook)

#### 4. Lightspeed Restaurant (Score: 88/100)
- **Menu Engineering:** Classificação por popularidade vs margem (stars/plowhorses/puzzles/dogs)
- **Advanced Inventory:** Ingredient tracking, vendor management, auto-PO
- **Staff Scheduling:** Integração nativa com scheduling
- **Multi-location:** Gestão centralizada de múltiplas lojas
- **Customer Insights:** LTV, segmentação, churn prediction

#### 5. Peblla Kiosk (Score: 85/100)
- **AI Suggestions:** Sugestões por horário/clima/dia da semana
- **Upselling Visual:** "Complete seu pedido" com imagens
- **Accessibility (ADA):** Voice guidance, alto contraste, ajuste de altura
- **Idle Management:** Attract screen, timeout com countdown

#### 6. Chick-fil-A App (Score: 90/100)
- **Mobile Order:** Curbside, drive-thru, delivery, dine-in
- **Cow Calendar:** Gamification sazonal
- **One-tap Reorder:** "Order Again" no topo do app
- **Location Intelligence:** Escolha de loja, filas estimadas

---

## 🔴 GAPS CRÍTICOS (Análise Kimi Code)

### Gaps por App

#### Cliente App (vs Starbucks/McDonald's)
| # | Gap | Impacto | Referência |
|---|-----|---------|-----------|
| C1 | **Loyalty/Rewards** — Sem programa de fidelidade | 🔴🔴🔴🔴🔴 Crítico | Starbucks Rewards = maior programa do mundo |
| C2 | **One-tap Reorder** — Não reutiliza pedidos anteriores | 🔴🔴🔴🔴🔴 Crítico | McDonald's converte em 1 toque |
| C3 | **Push Notifications** — Web Push preparado mas não usado | 🔴🔴🔴🔴 Alto | Starbucks usa para promoções/status |
| C4 | **Multi-location** — Não escolhe loja/drive-thru | 🔴🔴🔴 Médio | Chick-fil-A location intelligence |
| C5 | **Personalização** — Sem recomendações por behavior | 🔴🔴🔴 Médio | Starbucks personaliza por clima/hora |

#### Kiosk App (vs McDonald's/Peblla)
| # | Gap | Impacto | Referência |
|---|-----|---------|-----------|
| K1 | **Upselling Inteligente** — Não sugere adicionais | 🔴🔴🔴🔴🔴 Crítico | McDonald's +15-30% ticket |
| K2 | **AI Suggestions** — Sem sugestões por horário/clima | 🔴🔴🔴🔴 Alto | Peblla sugere por contexto |
| K3 | **Hardware Integration** — Config nos types mas zero integração real | 🔴🔴🔴🔴 Alto | Toast TPV + impressora + NFC |
| K4 | **Accessibility** — Sem voice guidance/alto contraste | 🔴🔴🔴 Médio | Peblla ADA compliance |

#### Admin App (vs Toast/Lightspeed)
| # | Gap | Impacto | Referência |
|---|-----|---------|-----------|
| A1 | **Ingredient Inventory** — Só "baldes de sabor", não ingredientes | 🔴🔴🔴🔴🔴 Crítico | Lightspeed deduz por item vendido |
| A2 | **Auto-86 (Auto-desativação)** — Quando acaba, não desativa nos apps | 🔴🔴🔴🔴🔴 Crítico | Toast auto-86 em tempo real |
| A3 | **Menu Engineering** — Não ajuda a decidir o que manter/cortar | 🔴🔴🔴🔴 Alto | Lightspeed "magic quadrant" |
| A4 | **Predictive Analytics** — Sem previsão de demanda/labor | 🔴🔴🔴🔴 Alto | Toast AI predictive labor |
| A5 | **RBAC** — Login mock `123456`, sem roles | 🔴🔴🔴🔴 Alto | Toast granular roles |
| A6 | **CRM/Customer Insights** — Sem LTV, segmentação, churn | 🔴🔴🔴 Médio | Lightspeed customer analytics |

#### KDS App (vs Toast/Square)
| # | Gap | Impacto | Referência |
|---|-----|---------|-----------|
| D1 | **Item-Level Status** — Só status geral, não por item | 🔴🔴🔴🔴🔴 Crítico | Toast item-level tracking |
| D2 | **Multi-estação** — Não escala para múltiplas estações | 🔴🔴🔴🔴🔴 Crítico | Toast station routing |
| D3 | **Expo View** — Sem tela de expedição (pick-up/delivery) | 🔴🔴🔴🔴 Alto | Toast expo screen |
| D4 | **Customer Context** — KDS não vê alergias/nome/histórico | 🔴🔴🔴🔴 Alto | Chick-fil-A customer card |

### Gaps Sistêmicos (Cross-App)

| # | Gap | Descrição | Apps Afetados |
|---|-----|-----------|---------------|
| GS-1 | KDS não sabe quem é o cliente | Cliente tem alergias/histórico; KDS vê só `tpv` vs `pwa` | Cliente + KDS |
| GS-2 | Admin vê mas não age | Mostra que acabou mas não desativa automaticamente | Admin + Cliente + Kiosk |
| GS-3 | Kiosk desperdiça dados do Cliente | Cliente tem favoritos; Kiosk não usa | Cliente + Kiosk |
| GS-4 | Analytics fragmentados | Cada app vê só sua parte; sem correlação cross-app | Todos |

---

## 🚀 ROADMAP — 3 QUICK WINS IMIATOS + 4 FASES

### QUICK WIN 1: Auto-86 (Semana 1)
**Descrição:** Quando um sabor acaba no Admin, desativa automaticamente em Cliente + Kiosk
**Referência:** Toast auto-86 em tempo real
**Técnico:**
- Trigger no Supabase: `inventory.quantity <= 0` → `menu_item.available = false`
- Broadcast via Realtime para Cliente + Kiosk
- Badge "Esgotado" em tempo real nos apps
- **Impacto:** Nunca vende o que não tem → zero insatisfação

### QUICK WIN 2: Upselling Básico (Semana 1-2)
**Descrição:** "Quer adicionar topping por +€0.50?" no carrinho do Kiosk
**Referência:** McDonald's upselling inteligente (+15-30% ticket)
**Técnico:**
- Hook no `addToCart`: detectar item base → sugerir topping relacionado
- UI: Modal/carrossel de "Complete seu pedido" com imagens
- Preço incremental claro (+€0.50)
- **Impacto:** +15% ticket médio imediato

### QUICK WIN 3: One-tap Reorder (Semana 2-3)
**Descrição:** Card "Pedir de novo" no topo do cardápio do Cliente
**Referência:** McDonald's "Order Again" em 1 toque
**Técnico:**
- Query último pedido do usuário (Supabase `orders` + `order_items`)
- Card no topo do menu: "Seu último pedido: [itens]"
- 1 toque → recria carrinho → checkout
- **Impacto:** Retenção rápida, reduz friction de reordenar

### FASE 1: Fundação Operacional (Semanas 4-7)
- **C1 → Loyalty Básico:** Pontos por € gasto, resgate de recompensas
- **C3 → Push Notifications:** Promoções, status de pedido, lembrete de reordenar
- **D1 → Item-Level KDS:** Cada item com status independente (preparando/pronto/entregue)
- **D2 → Multi-estação KDS:** Routing por tipo (sorvete/bubble tea/waffle)
- **K1 → Upselling Avançado:** Sugestões por horário/clima/temperatura

### FASE 2: Inteligência de Negócio (Semanas 8-11)
- **A1 → Ingredient Inventory:** Rastreamento por ingrediente, auto-dedução
- **A3 → Menu Engineering:** Quadrante popularidade vs margem
- **A5 → RBAC:** Roles (owner/manager/cozinheiro/atendente)
- **GS-4 → Analytics Unificado:** Dashboard cross-app (correlação KDS tempo + margem + vendas)

### FASE 3: Automação Avançada (Semanas 12-16)
- **A4 → Predictive Analytics:** Previsão de demanda por dia/hora/clima
- **A2 → Auto-86 Inteligente:** Previsão de esgotamento antes de acabar
- **K3 → Hardware Integration:** TPV, impressora de tickets, leitor NFC
- **C4 → Multi-location:** Gestão de múltiplas lojas

### FASE 4: AI-Driven (Semanas 17-24)
- **C5 → AI Personalização:** Recomendações por behavior, clima, horário
- **K2 → AI Kiosk Suggestions:** Sugestões dinâmicas por contexto
- **A6 → CRM/Customer Insights:** LTV, segmentação, churn prediction
- **D3 → Expo View:** Tela de expedição com routing por tipo de entrega

---

## 🎨 DESIGN SYSTEM .brain

```
Cores:
- 🟢 Verde (#2ed573): OK, funcionando, aprovado
- 🔴 Vermelho (#ff4757): ERRO, quebrado, crítico
- 🟠 Laranja (#ffa502): ATENÇÃO, revisar, pendente
- 🔵 Azul (#3742fa): INFO, contexto, observação

Stack:
- React 18 + TypeScript + Vite + Tailwind CSS
- Supabase (PostgreSQL + Auth + Realtime + Storage)
- Capacitor (Android) / PWA
- Vercel (frontend)

Filosofia: Funciona > Perfeito > Bonito > Nada
```

---

## 📝 INSTRUÇÕES DE IMPLEMENTAÇÃO

### Estrutura de Prompts por Fase

Cada fase deve gerar prompts separados para Kimi Code, seguindo:

1. **FASE [N]** → Contexto + Requisitos + Referências
2. **App [X]** → Componentes + Types + Supabase Schema + Tests
3. **Cross-App** → Sync points + Realtime subscriptions + State management

### Regras de Implementação

1. **Nunca quebrar P1 (Sync Engine):** Todas as mudanças devem manter Supabase Realtime funcional
2. **Offline-first:** Novas features devem funcionar offline (SQLite + Service Worker)
3. **i18n:** Todos os textos via `t()` (ja, en, es, pt, de, fr, zh, ko, ar)
4. **Acessibilidade:** ARIA labels, keyboard navigation, screen reader support
5. **Mobile-first:** Capacitor + PWA, touch-optimized, performance < 3s FCP
6. **Testes:** Cada feature com testes unitários + teste de integração

### Checklist de Entrega

- [ ] Código funciona (zero bugs)
- [ ] Testes passam
- [ ] Offline funciona
- [ ] Mobile responsivo
- [ ] i18n completo
- [ ] Acessibilidade OK
- [ ] Documentação .brain atualizada
- [ ] Métricas de impacto medidas

---

## 🧠 MANDAMENTOS .brain

1. **Zero placeholders.** Toda UI usa dados reais do Supabase.
2. **Nunca o mesmo erro duas vezes.** Bug detectado → fix + test + documentação.
3. **Funciona > Perfeito > Bonito > Nada.** Demo funcional vence mock bonito.
4. **Simplificar sem permissão = traição.** Nunca remova feature sem autorização.
5. **Métricas ou não aconteceu.** Toda feature mede impacto (ticket médio, retenção, tempo).
6. **Stack lock.** React + Vite + Tailwind + Supabase. Sem exceções.
7. **Mobile-native.** Tudo funciona no celular. Desktop é bônus.
8. **Segurança.** Nunca expõe secrets. Nunca hardcode tokens.
9. **Documentação.** Cada decisão é uma linha no .brain.
10. **Owner-first.** Quem manda é o Jhin. Eu só executo.

---

## 📊 MÉTRICAS DE SUCESSO

| Métrica | Atual | Meta Fase 1 | Meta Fase 4 |
|---------|-------|-------------|-------------|
| Score vs Mercado | 50/100 | 70/100 | 90/100 |
| Ticket Médio | €4.50 | €5.20 (+15%) | €6.30 (+40%) |
| Retenção (30 dias) | ? | 35% | 60% |
| Tempo KDS (médio) | ? | < 3 min | < 2 min |
| Taxa de Auto-86 | Manual | 100% auto | Predictivo |
| NPS (satisfação) | ? | > 50 | > 70 |

---

## 🦀 NOTA DA LUNA

> Este prompt foi gerado após análise competitiva detalhada do ecossistema TPV Sorveteria vs as melhores referências de mercado mundial (Starbucks, McDonald's, Toast, Lightspeed, Peblla, Chick-fil-A).
> 
> O ecossistema atual está no patamar "operacional mas não extraordinário" — score 50/100. Os 3 quick wins (Auto-86 + Upselling + One-tap Reorder) são fixes críticos de negócio que desbloqueiam as fases seguintes.
> 
> Quem manda é o Jhin. Eu só executo. 🫡

---

**Gerado em:** 2026-04-29
**Versão:** 1.0
**Fonte:** Análise Kimi Code + Pesquisa de Mercado (Starbucks, McDonald's, Toast, Lightspeed, Peblla, Chick-fil-A)
