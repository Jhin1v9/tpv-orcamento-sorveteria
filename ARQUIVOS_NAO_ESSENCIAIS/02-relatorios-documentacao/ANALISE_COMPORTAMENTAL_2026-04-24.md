# Relatório de Análise Comportamental — TPV Sorveteria
**Data:** 2026-04-24  
**Método:** Observação via browser + testes API direta  
**Restrição:** Nenhuma alteração de código nesta rodada

---

## 1. AMBIENTE SUPABASE — ESTADO CRÍTICO

### Observação
O projeto Supabase `dproxlygtabihfhtxdvm` apresenta **corrupção persistente no cache PostgREST**:

| Sintoma | Evidência |
|---------|-----------|
| UPDATE retorna "OK" mas NÃO persiste | Status permanece inalterado após update |
| SELECT retorna dados inconsistentes | SQL Editor mostra tabela vazia, REST API mostra 2 rows |
| RPCs invisíveis | `create_order`, `update_order_status` → 404 |
| Schema reload não funciona | `NOTIFY pgrst, 'reload schema'` sem efeito |
| Colunas desconhecidas | `updated_at` não reconhecida em algumas queries |

### Impacto no Comportamento
- **Kiosk:** Inicializa em modo offline/standalone (barra vermelha "Sin conexión")
- **Cliente PWA:** Não consegue criar pedidos remotos → fallback para demo local
- **KDS/Admin:** Não recebe pedidos em tempo real

---

## 2. FLUXO KIOSK — OBSERVAÇÃO EM VIVO

### AttractScreen (Tela Inicial)
✅ **Corrigido:** Agora mostra carrossel de saudações internacionais:
- Hola → Hello → Bonjour → Ciao → Hallo
- CTA em espanhol: "TOCA PARA EMPEZAR"
- Crossfade funciona sem flash preto

### HolaScreen → CardapioScreen
✅ Transição funciona ao tocar
⚠️ **Observado:** Imagens de produtos falham (404) — apontam para `localhost:8788/assets/produtos/` mas servidor não serve esses arquivos

### Adicionar ao Carrinho
✅ Funciona para produtos fixos (BUG-004 já estava corrigido)
⚠️ Produtos personalizáveis podem ter problemas com `opcoes` nulo (BUG-003 parcialmente mitigado com ErrorBoundary)

### Checkout → Pagamento
⚠️ **NÃO TESTADO EM VIVO** — mas código analisado mostra:
- `ProcessandoPagamento` agora adapta animação ao método (fix aplicado)
- Fallback de tabela implementado para contornar RPCs quebradas

---

## 3. FLUXO CLIENTE PWA — OBSERVAÇÃO EM VIVO

### Tela Inicial (Cardapio)
⚠️ **Snapshot vazio no browser** — app pode estar em estado de loading ou erro de inicialização
- Console mostra 5 erros (provavelmente conexão Supabase falhando)
- Modo standalone ativado automaticamente

### ProductDetailModal
✅ ErrorBoundary envolve o modal (prevenção de WSOD)
⚠️ Null guards em `opcoesProduto` adicionados

### Carrinho → Pagamento
✅ `ProcessandoPagamento` adapta animação por método (tarjeta/bizum/efectivo)
⚠️ **Sem teste E2E real** — necessita modo standalone funcional

---

## 4. FLUXO COZINHA (KDS) — ANÁLISE DE CÓDIGO

### Comportamento Esperado
1. KDS polling/subscribe em `orders` com status `pendiente` ou `preparing`
2. Chef clica em "Aceitar" → status `preparing`
3. Chef clica em "Listo" → status `listo`
4. Cliente vê atualização em tempo real

### Observação
⚠️ **Não testado em vivo** — mas a lógica de UPDATE direto em tabela foi implementada como fallback
⚠️ Supabase quebrado impede teste real de realtime

---

## 5. COMPORTAMENTOS ESTRANHOS DETECTADOS

| # | Comportamento | Severidade | Local |
|---|---------------|------------|-------|
| 1 | PostgREST cache corrompido | 🔴 CRÍTICO | Supabase infra |
| 2 | Imagens 404 no kiosk | 🟡 Média | `public/assets/produtos/` |
| 3 | Onboarding aparece em cada reload | 🟡 Média | `useStore` persistência |
| 4 | Carousel AttractScreen em português | 🟢 Fixado | AttractScreen.tsx |
| 5 | Animação pagamento sempre tarjeta | 🟢 Fixado | ProcessandoPagamento.tsx |
| 6 | WSOD no ProductDetailModal | 🟢 Mitigado | ErrorBoundary + null guards |

---

## 6. TESTE API — FLUXO COMPLETO (MODO DIRETO)

```
=== FLUXO CLIENTE -> COZINHA -> CLIENTE ===
1. CLIENTE: Produto escolhido — Copa Bahia €8.1
1. CLIENTE: Pedido criado — #4 Status: pendiente ✅
1. CLIENTE: Item adicionado ao pedido ✅
2. COZINHA: Pedidos pendentes — 2 ✅
3. COZINHA: Status → preparing (OK mas NÃO persiste) ⚠️
4. COZINHA: Status → listo (OK mas NÃO persiste) ⚠️
5. CLIENTE: Consulta status — pendiente (stale cache) ⚠️
```

**Conclusão:** O INSERT funciona, mas UPDATE é ignorado pelo PostgREST. O pedido nasce mas não envelhece.

---

## 7. RECOMENDAÇÕES (SEM ALTERAR CÓDIGO)

1. **Supabase:** Criar ticket de suporte ou migrar para outro projeto/região
2. **Testes E2E:** Usar modo standalone até o Supabase estabilizar
3. **Deploy:** Adiar até o backend estar funcional
4. **Monitoramento:** Adicionar healthcheck de PostgREST no dashboard

---

*Relatório gerado por observação direta. Nenhum código foi alterado nesta rodada.*
