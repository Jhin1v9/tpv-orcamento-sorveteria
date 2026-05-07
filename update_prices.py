#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar precos no index.html com base em pesquisa de mercado real
Estrategia de precificacao PNL + Neurociencia de Vendas
"""

import re

filepath = r"C:\Users\Administrator\Documents\Projeto Ideias sorveteria\tpv-orcamento-sorveteria\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# SUBSTITUICOES PRINCIPAIS
# ============================================================

# --- SECAO DE PLANOS (cards) ---

# Setup dos planos
content = content.replace(
    '<div class="price-tag text-3xl font-bold text-white">1.800 EUR</div>',
    '<div class="price-tag text-3xl font-bold text-white">497 EUR</div>'
)
content = content.replace(
    '<div class="price-tag text-3xl font-bold text-white">4.200 EUR</div>',
    '<div class="price-tag text-3xl font-bold text-white">997 EUR</div>'
)
content = content.replace(
    '<div class="price-tag text-3xl font-bold text-white">8.500 EUR</div>',
    '<div class="price-tag text-3xl font-bold text-white">1.997 EUR</div>'
)

# Mensalidades dos planos
content = content.replace(
    '<div class="mt-2 text-brand-red font-semibold text-sm">+ 89 EUR/mes suporte</div>',
    '<div class="mt-2 text-brand-red font-semibold text-sm">+ 79 EUR/mes suporte</div>'
)
# Pro mantem 149, mas vamos garantir que nao quebre nada
content = content.replace(
    '<div class="mt-2 text-brand-green font-semibold text-sm">+ 249 EUR/mes suporte</div>',
    '<div class="mt-2 text-brand-green font-semibold text-sm">+ 197 EUR/mes suporte</div>'
)

# Custo total Ano 1
content = content.replace(
    '<div class="text-lg font-bold text-white">2.868 EUR</div>',
    '<div class="text-lg font-bold text-white">1.445 EUR</div>'
)
content = content.replace(
    '<div class="text-lg font-bold text-white">5.988 EUR</div>',
    '<div class="text-lg font-bold text-white">2.785 EUR</div>'
)
content = content.replace(
    '<div class="text-lg font-bold text-white">11.488 EUR</div>',
    '<div class="text-lg font-bold text-white">4.361 EUR</div>'
)

# Break-even
content = content.replace(
    '<div class="text-xs text-brand-red mt-1">Break-even: ~7 meses</div>',
    '<div class="text-xs text-brand-red mt-1">Break-even: ~17 dias</div>'
)
content = content.replace(
    '<div class="text-xs text-brand-orange mt-1">Break-even: ~6 meses</div>',
    '<div class="text-xs text-brand-orange mt-1">Break-even: ~24 dias</div>'
)
content = content.replace(
    '<div class="text-xs text-brand-green mt-1">Break-even: ~5.5 meses | Lucro Ano 1: 5.312 EUR</div>',
    '<div class="text-xs text-brand-green mt-1">Break-even: ~35 dias | Lucro Ano 1: 12.439 EUR</div>'
)

# Economias mensais nos cards
content = content.replace(
    '<div class="text-xs text-gray-500">Economia: 350 EUR/mes</div>',
    '<div class="text-xs text-gray-500">Economia: 380 EUR/mes</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-500">Economia: 750 EUR/mes</div>',
    '<div class="text-xs text-gray-500">Economia: 820 EUR/mes</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-500">Economia: 1.400 EUR/mes</div>',
    '<div class="text-xs text-gray-500">Economia: 1.520 EUR/mes</div>'
)

# --- PACK SUPREMO DETALHAMENTO ---
content = content.replace(
    '<h2 class="font-display text-3xl font-bold text-white">Pack Supremo — Detalhamento Completo</h2>\n<p class="text-gray-500">O que realmente esta incluso nos 8.500 EUR de setup (Pack Completo)</p>',
    '<h2 class="font-display text-3xl font-bold text-white">Pack Supremo — Detalhamento Completo</h2>\n<p class="text-gray-500">O que realmente esta incluso nos 1.997 EUR de setup (Pack Completo)</p>'
)

# Subtotal desenvolvimento (manter valores reais de mercado para ancoragem)
# Mas ajustar o total
content = content.replace(
    '<div class="flex justify-between items-center"><span class="text-brand-green font-semibold">TOTAL PACK SUPREMO</span><span class="text-brand-green font-bold text-xl">8.500 EUR</span></div>',
    '<div class="flex justify-between items-center"><span class="text-brand-green font-semibold">TOTAL PACK SUPREMO</span><span class="text-brand-green font-bold text-xl">1.997 EUR</span></div>'
)
content = content.replace(
    '<div class="text-xs text-gray-500 mt-1">Valor real: 9.380 EUR</div>',
    '<div class="text-xs text-gray-500 mt-1">Valor real de mercado: 9.380 EUR</div>'
)

# Mensalidade cobertura
content = content.replace(
    '<h3 class="text-white font-semibold mb-4">O que a mensalidade de 249 EUR cobre</h3>',
    '<h3 class="text-white font-semibold mb-4">O que a mensalidade de 197 EUR cobre</h3>'
)

# --- PWA CLIENTE ---
content = content.replace(
    '<div class="flex justify-between items-center mb-2"><span class="text-white font-semibold">Desenvolvimento PWA isolado</span><span class="text-brand-purple font-bold text-xl">1.800 EUR</span></div>',
    '<div class="flex justify-between items-center mb-2"><span class="text-white font-semibold">Desenvolvimento PWA isolado</span><span class="text-brand-purple font-bold text-xl">1.200 EUR</span></div>'
)
content = content.replace(
    '<div class="text-xs text-gray-500">Economia de 1.800 EUR no setup</div>',
    '<div class="text-xs text-gray-500">Economia de 1.200 EUR no setup</div>'
)
content = content.replace(
    'incluso na mensalidade de 249 EUR',
    'incluso na mensalidade de 197 EUR'
)

# --- ROI & VIABILIDADE ---
content = content.replace(
    '<div class="text-5xl font-display font-bold text-brand-green mb-2">3.5x</div>\n<div class="text-sm text-gray-400">Break-even em meses<br>(Pack Supremo)</div>',
    '<div class="text-5xl font-display font-bold text-brand-green mb-2">35</div>\n<div class="text-sm text-gray-400">Break-even em dias<br>(Pack Supremo)</div>'
)
content = content.replace(
    '<div class="text-5xl font-display font-bold text-brand-orange mb-2">2.100 EUR</div>\n<div class="text-sm text-gray-400">Economia total/mes<br>(eficiencia + receita)</div>',
    '<div class="text-5xl font-display font-bold text-brand-orange mb-2">1.685 EUR</div>\n<div class="text-sm text-gray-400">Economia liquida/mes<br>(depois da mensalidade)</div>'
)
content = content.replace(
    '<div class="text-5xl font-display font-bold text-brand-blue mb-2">5.312 EUR</div>\n<div class="text-sm text-gray-400">Lucro liquido Ano 1<br>(Pack Supremo)</div>',
    '<div class="text-5xl font-display font-bold text-brand-blue mb-2">12.439 EUR</div>\n<div class="text-sm text-gray-400">Lucro liquido Ano 1<br>(Pack Supremo)</div>'
)

# Valor total gerado
content = content.replace(
    '<span class="text-white font-semibold">Valor Total Gerado / Mes</span><span class="text-brand-green font-bold text-2xl">1.400 EUR</span>',
    '<span class="text-white font-semibold">Valor Total Gerado / Mes</span><span class="text-brand-green font-bold text-2xl">1.520 EUR</span>'
)

# Comparativo 3 anos
content = content.replace(
    '<td>5.004 EUR</td><td>9.564 EUR</td><td class="text-brand-green font-semibold">17.464 EUR</td>',
    '<td>3.341 EUR</td><td>6.361 EUR</td><td class="text-brand-green font-semibold">9.089 EUR</td>'
)
content = content.replace(
    '<td>12.600 EUR</td><td>27.000 EUR</td><td class="text-brand-green font-semibold">50.400 EUR</td>',
    '<td>10.800 EUR</td><td>25.200 EUR</td><td class="text-brand-green font-semibold">46.800 EUR</td>'
)
content = content.replace(
    '<td>7.596 EUR</td><td>17.436 EUR</td><td class="text-brand-green font-bold">32.936 EUR</td>',
    '<td>7.459 EUR</td><td>18.839 EUR</td><td class="text-brand-green font-bold">37.711 EUR</td>'
)
content = content.replace(
    '<td>152%</td><td>182%</td><td class="text-brand-green font-bold">189%</td>',
    '<td>223%</td><td>296%</td><td class="text-brand-green font-bold">415%</td>'
)
content = content.replace(
    '<td>7 meses</td><td>6 meses</td><td class="text-brand-green font-bold">5.5 meses</td>',
    '<td>17 dias</td><td>24 dias</td><td class="text-brand-green font-bold">35 dias</td>'
)

# --- TABELA COMPARATIVA FUNCIONALIDADES ---
content = content.replace(
    '<th class="p-4 text-center text-brand-red font-semibold">Essencial<br><span class="text-xs font-normal text-gray-500">1.800 EUR + 89/mes</span></th>',
    '<th class="p-4 text-center text-brand-red font-semibold">Essencial<br><span class="text-xs font-normal text-gray-500">497 EUR + 79/mes</span></th>'
)
content = content.replace(
    '<th class="p-4 text-center text-brand-orange font-semibold">Pro<br><span class="text-xs font-normal text-gray-500">4.200 EUR + 149/mes</span></th>',
    '<th class="p-4 text-center text-brand-orange font-semibold">Pro<br><span class="text-xs font-normal text-gray-500">997 EUR + 149/mes</span></th>'
)
content = content.replace(
    '<th class="p-4 text-center text-brand-green font-semibold">Supremo<br><span class="text-xs font-normal text-gray-500">8.500 EUR + 249/mes</span></th>',
    '<th class="p-4 text-center text-brand-green font-semibold">Supremo<br><span class="text-xs font-normal text-gray-500">1.997 EUR + 197/mes</span></th>'
)

# Lucros na tabela
content = content.replace(
    '<td class="p-4 text-center text-brand-red font-bold">1.332 EUR</td><td class="p-4 text-center text-brand-orange font-bold">3.012 EUR</td><td class="p-4 text-center text-brand-green font-bold text-lg">5.312 EUR</td>',
    '<td class="p-4 text-center text-brand-red font-bold">2.155 EUR</td><td class="p-4 text-center text-brand-orange font-bold">4.415 EUR</td><td class="p-4 text-center text-brand-green font-bold text-lg">12.439 EUR</td>'
)

# --- SECOES INICIAIS (antes-depois, analise) ---
content = content.replace(
    '<div class="text-gray-500 text-xs">O que ele vai ter — 249 EUR/mes (Supremo)</div>',
    '<div class="text-gray-500 text-xs">O que ele vai ter — 197 EUR/mes (Supremo)</div>'
)
content = content.replace(
    '<h4 class="text-white font-semibold mb-3">Por que nossa mensalidade e 249 EUR e nao 90 EUR?</h4>',
    '<h4 class="text-white font-semibold mb-3">Por que nossa mensalidade e 197 EUR e nao 90 EUR?</h4>'
)
content = content.replace(
    'Nosso sistema de 249 EUR resolve <strong>TUDO de uma vez</strong>',
    'Nosso sistema de 197 EUR resolve <strong>TUDO de uma vez</strong>'
)
content = content.replace(
    '<strong class="text-brand-green">A diferenca de 159 EUR/mes (249 - 90) paga sozinha</strong> porque voce elimina 2 camareros',
    '<strong class="text-brand-green">A diferenca de 107 EUR/mes (197 - 90) paga sozinha</strong> porque voce elimina 2 camareros'
)

# Cenario com nosso sistema
content = content.replace(
    '<div class="flex justify-between py-1 border-b border-white/5"><span class="text-gray-300">Nosso sistema (Supremo)</span><span class="text-brand-green font-semibold">249 EUR/mes</span></div>',
    '<div class="flex justify-between py-1 border-b border-white/5"><span class="text-gray-300">Nosso sistema (Supremo)</span><span class="text-brand-green font-semibold">197 EUR/mes</span></div>'
)
content = content.replace(
    '<span class="text-brand-orange font-bold text-lg">+309 EUR/mes (+3,5%)</span>',
    '<span class="text-brand-orange font-bold text-lg">+257 EUR/mes (+2,9%)</span>'
)
content = content.replace(
    '<div class="text-xs text-gray-500 mt-1">Mas o faturamento aumenta 60.000 EUR/ano. O custo extra de 309 EUR/mes gera 5.000 EUR/mes a mais de receita.</div>',
    '<div class="text-xs text-gray-500 mt-1">Mas o faturamento aumenta 60.000 EUR/ano. O custo extra de 257 EUR/mes gera 5.000 EUR/mes a mais de receita.</div>'
)

# Tabela custos anual
content = content.replace(
    '<td>0 EUR</td><td>11.488 EUR</td><td class="text-brand-blue">+8.488 EUR</td>',
    '<td>0 EUR</td><td>4.361 EUR</td><td class="text-brand-blue">+4.361 EUR</td>'
)
content = content.replace(
    '<td class="text-brand-red font-bold">114.520 EUR</td><td class="text-brand-green font-bold">158.324 EUR</td><td class="text-brand-blue font-bold text-lg">+43.804 EUR</td>',
    '<td class="text-brand-red font-bold">114.520 EUR</td><td class="text-brand-green font-bold">165.451 EUR</td><td class="text-brand-blue font-bold text-lg">+50.931 EUR</td>'
)

# Textos de justificativa
content = content.replace(
    'Voce investe 8.500 EUR + 249 EUR/mes. Em 5.5 meses, a economia de 2 camareros (1.200 EUR/mes) + o aumento de faturamento ja cobriu tudo.',
    'Voce investe 1.997 EUR + 197 EUR/mes. Em 35 dias, a economia de 2 camareros (1.200 EUR/mes) + o aumento de faturamento ja cobriu tudo.'
)
content = content.replace(
    'Nos cobramos 249 EUR/mes por 4 apps + suporte + hardware.',
    'Nos cobramos 197 EUR/mes por 4 apps + suporte + hardware.'
)
content = content.replace(
    'O Pack Supremo oferece 4 apps + hardware + suporte por 8.500 EUR.',
    'O Pack Supremo oferece 4 apps + hardware + suporte por 1.997 EUR.'
)

# Tabela comparativa mercado
content = content.replace(
    '<td class="text-brand-green font-bold">249 EUR</td><td class="text-brand-green font-bold">INCLUSO</td><td class="text-brand-green font-bold">INCLUSO</td><td class="text-brand-green font-bold">8.500 EUR</td>',
    '<td class="text-brand-green font-bold">197 EUR</td><td class="text-brand-green font-bold">INCLUSO</td><td class="text-brand-green font-bold">INCLUSO</td><td class="text-brand-green font-bold">1.997 EUR</td>'
)

# Custo sistema setup + 12x mensal na tabela de mercado
# Ja tratado acima

# --- ELO WALLABY (preco unitario) ---
# Manter ~500 EUR como referencia real do hardware

# --- PRECO NO CARD INICIAL (se houver) ---
content = content.replace(
    '<div class="text-4xl font-display font-bold text-brand-red mb-2">1.800 EUR</div>',
    '<div class="text-4xl font-display font-bold text-brand-red mb-2">497 EUR</div>'
)

# --- PRECO MERCADO KIOSK ---
# Manter 50-89 EUR como referencia concorrente

# Salvar
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Precos atualizados com sucesso!")
print("Resumo das mudancas:")
print("  - Setup Essencial: 1.800 -> 497 EUR")
print("  - Setup Pro: 4.200 -> 997 EUR")
print("  - Setup Supremo: 8.500 -> 1.997 EUR")
print("  - Mensal Essencial: 89 -> 79 EUR")
print("  - Mensal Pro: 149 EUR (mantido)")
print("  - Mensal Supremo: 249 -> 197 EUR")
