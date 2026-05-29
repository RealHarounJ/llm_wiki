#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte Carlo Projection — Quanto tempo per arrivare a €10k?
Simulazione con contributi mensili variabili e scenari multipli.
"""
import math
import random
import datetime
import sys

# Forza codifica UTF-8 per console Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

random.seed(42)

# ── Caricamento dinamico del valore attuale dal portafoglio Trading 212 ─────────
CURRENT_VALUE = 2211.25  # Fallback di produzione
try:
    from fetch_trading212_portfolio import load_trading212_credentials, fetch_positions
    api_auth = load_trading212_credentials()
    positions, ep_name = fetch_positions(api_auth)
    if positions:
        total_val = 0.0
        for pos in positions:
            val = pos.get("walletImpact", {}).get("currentValue")
            if val is None:
                val = pos.get("value")
                if val is None:
                    quantity = float(pos.get("quantity", 0.0))
                    curr_price = float(pos.get("currentPrice", 0.0))
                    val = quantity * curr_price
            total_val += float(val)
        CURRENT_VALUE = round(total_val, 2)
        print(f"✅ Valore portafoglio Trading 212 in tempo reale caricato via API ({ep_name}): €{CURRENT_VALUE}")
except Exception as e:
    print(f"⚠️ Impossibile caricare il valore live da API ({e}). Utilizzo fallback: €{CURRENT_VALUE}")

MONTHLY_CONTRIBUTION = 100.0  # PAC mensile
TARGET = 10000.0

# ── Parametri di mercato (calibrati su dati storici) ───────────────────────────
# Il portafoglio ora è: 55% SWDA, 15% EIMI, 15% SDIV, 15% BP + vecchie posizioni

# Rendimenti annui storici (media geometrica, ultimi 10 anni)
# MSCI World: ~10.5% annuo | MSCI EM: ~5.5% | High Dividend Global: ~7.5% | BP: ~6%
# Blend pesato: 0.55*10.5 + 0.15*5.5 + 0.15*7.5 + 0.15*6 = 5.775 + 0.825 + 1.125 + 0.9 = 8.625%
ANNUAL_RETURN_BASE = 0.0862
# Volatilità annua (portafoglio diversificato globale)
# MSCI World vol: ~15% | EIMI: ~18% | SDIV: ~16% | BP: ~25%
# Blend: ~16%
ANNUAL_VOL = 0.16

# Scenario ottimizzato (se aggiungo modelli quant avanzati)
# Factor investing + momentum + mean reversion può aggiungere 2-4% lordo annuo (alpha)
# Ma realisticamente, dopo costi e slippage: +1.5-2.5% netto
QUANT_ALPHA = 0.02  # alpha annuo aggiuntivo con modelli avanzati

MONTHS_HORIZON = 60  # 5 anni di proiezione
N_SIMULATIONS = 50000

def random_normal():
    u1, u2 = random.random(), random.random()
    while u1 <= 1e-15: u1 = random.random()
    return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)

def simulate_portfolio(initial, monthly_contrib, annual_ret, annual_vol, months, n_sims):
    """
    GBM con contributi mensili. Ritorna percentili del valore finale per ogni mese.
    """
    monthly_ret = annual_ret / 12.0
    monthly_vol = annual_vol / math.sqrt(12.0)
    drift = monthly_ret - 0.5 * monthly_vol**2  # drift corretto (Itô)

    # Traccia tutti i percorsi
    paths = []
    for _ in range(n_sims):
        value = initial
        path = [value]
        for m in range(1, months + 1):
            shock = random_normal()
            value = value * math.exp(drift + monthly_vol * shock) + monthly_contrib
            path.append(max(value, 0))  # no negative
        paths.append(path)

    # Calcola percentili per ogni mese
    percentiles = {5: [], 25: [], 50: [], 75: [], 95: []}
    for m in range(months + 1):
        vals = sorted([p[m] for p in paths])
        n = len(vals)
        for pct in percentiles:
            idx = int(n * pct / 100)
            percentiles[pct].append(vals[min(idx, n-1)])

    # Probabilità di raggiungere il target per ogni mese
    prob_target = []
    for m in range(months + 1):
        count = sum(1 for p in paths if p[m] >= TARGET)
        prob_target.append(count / n_sims * 100)

    return percentiles, prob_target

def find_month_for_prob(prob_target, threshold):
    """Trova il primo mese in cui la probabilità supera la soglia."""
    for m, p in enumerate(prob_target):
        if p >= threshold:
            return m
    return None

print("=" * 75)
print("  📊 PROIEZIONE MONTE CARLO — Road to €10,000")
print(f"  Portafoglio attuale: €{CURRENT_VALUE:.0f} | PAC: €{MONTHLY_CONTRIBUTION}/mese")
print(f"  Simulazioni: {N_SIMULATIONS:,} | Orizzonte: {MONTHS_HORIZON} mesi")
print("=" * 75)

# ── SCENARIO 1: Passivo (Buy & Hold + PAC €100/mese) ──────────────────────────
print("\n\n━━━ SCENARIO 1: PASSIVO (Buy & Hold + PAC €100/mese) ━━━")
print(f"    Rendimento atteso annuo: {ANNUAL_RETURN_BASE*100:.1f}% | Volatilità: {ANNUAL_VOL*100:.0f}%")
p1, prob1 = simulate_portfolio(CURRENT_VALUE, MONTHLY_CONTRIBUTION, ANNUAL_RETURN_BASE, ANNUAL_VOL, MONTHS_HORIZON, N_SIMULATIONS)

for horizon in [3, 6, 12, 24, 36, 48, 60]:
    if horizon > MONTHS_HORIZON: break
    print(f"\n  📅 A {horizon} mesi ({datetime.date.today() + datetime.timedelta(days=horizon*30):%b %Y}):")
    print(f"     Mediana: €{p1[50][horizon]:.0f} | Range 50%: €{p1[25][horizon]:.0f}–€{p1[75][horizon]:.0f} | Range 90%: €{p1[5][horizon]:.0f}–€{p1[95][horizon]:.0f}")
    print(f"     Prob. ≥ €10k: {prob1[horizon]:.1f}%")
    contributed = CURRENT_VALUE + MONTHLY_CONTRIBUTION * horizon
    gain = p1[50][horizon] - contributed
    pct = (gain / contributed) * 100
    print(f"     Capitale investito: €{contributed:.0f} | Guadagno mediano: €{gain:.0f} ({pct:+.1f}%)")

m50 = find_month_for_prob(prob1, 50)
print(f"\n  🎯 50% probabilità di €10k: {'mese ' + str(m50) if m50 else '>60 mesi'}")

# ── SCENARIO 2: Quant Attivo (con alpha da factor investing) ──────────────────
print("\n\n━━━ SCENARIO 2: QUANT ATTIVO (+2% alpha annuo) ━━━")
ret2 = ANNUAL_RETURN_BASE + QUANT_ALPHA
print(f"    Rendimento atteso annuo: {ret2*100:.1f}% | Volatilità: {ANNUAL_VOL*100:.0f}%")
p2, prob2 = simulate_portfolio(CURRENT_VALUE, MONTHLY_CONTRIBUTION, ret2, ANNUAL_VOL, MONTHS_HORIZON, N_SIMULATIONS)

for horizon in [3, 6, 12, 24, 36, 48, 60]:
    if horizon > MONTHS_HORIZON: break
    print(f"\n  📅 A {horizon} mesi ({datetime.date.today() + datetime.timedelta(days=horizon*30):%b %Y}):")
    print(f"     Mediana: €{p2[50][horizon]:.0f} | Range 50%: €{p2[25][horizon]:.0f}–€{p2[75][horizon]:.0f}")
    print(f"     Prob. ≥ €10k: {prob2[horizon]:.1f}%")

m50_q = find_month_for_prob(prob2, 50)
print(f"\n  🎯 50% probabilità di €10k: {'mese ' + str(m50_q) if m50_q else '>60 mesi'}")

# ── SCENARIO 3: PAC Aumentato (€200/mese + quant) ─────────────────────────────
print("\n\n━━━ SCENARIO 3: PAC €200/mese + QUANT ATTIVO ━━━")
p3, prob3 = simulate_portfolio(CURRENT_VALUE, 200.0, ret2, ANNUAL_VOL, MONTHS_HORIZON, N_SIMULATIONS)

for horizon in [3, 6, 12, 24, 36, 48, 60]:
    if horizon > MONTHS_HORIZON: break
    print(f"\n  📅 A {horizon} mesi:")
    print(f"     Mediana: €{p3[50][horizon]:.0f} | Prob. ≥ €10k: {prob3[horizon]:.1f}%")

m50_3 = find_month_for_prob(prob3, 50)
print(f"\n  🎯 50% probabilità di €10k: {'mese ' + str(m50_3) if m50_3 else '>60 mesi'}")

# ── SCENARIO 4: PAC €500/mese + quant ─────────────────────────────────────────
print("\n\n━━━ SCENARIO 4: PAC €500/mese + QUANT ATTIVO ━━━")
p4, prob4 = simulate_portfolio(CURRENT_VALUE, 500.0, ret2, ANNUAL_VOL, MONTHS_HORIZON, N_SIMULATIONS)

for horizon in [3, 6, 12, 24, 36, 48, 60]:
    if horizon > MONTHS_HORIZON: break
    print(f"\n  📅 A {horizon} mesi:")
    print(f"     Mediana: €{p4[50][horizon]:.0f} | Prob. ≥ €10k: {prob4[horizon]:.1f}%")

m50_4 = find_month_for_prob(prob4, 50)
print(f"\n  🎯 50% probabilità di €10k: {'mese ' + str(m50_4) if m50_4 else '>60 mesi'}")

# ── RIEPILOGO ──────────────────────────────────────────────────────────────────
print("\n\n" + "=" * 75)
print("  📋 RIEPILOGO — Quando arrivi a €10k?")
print("=" * 75)
print(f"  {'SCENARIO':<40} {'MESE 50%':<15} {'MESE (≈ANNI)'}")
print(f"  {'─'*65}")
scenarios = [
    ("Passivo €100/mese",           m50),
    ("Quant attivo €100/mese",      m50_q),
    ("Quant attivo €200/mese",      m50_3),
    ("Quant attivo €500/mese",      m50_4),
]
for name, month in scenarios:
    if month:
        years = month / 12
        target_date = datetime.date.today() + datetime.timedelta(days=month * 30)
        print(f"  {name:<40} Mese {month:<10} ~{years:.1f} anni ({target_date:%b %Y})")
    else:
        print(f"  {name:<40} {'> 60 mesi':<15} > 5 anni")

# ── COSA SERVE A LIVELLO QUANT ─────────────────────────────────────────────────
print("\n\n" + "=" * 75)
print("  🎓 STRUMENTI QUANT CHE POSSO IMPLEMENTARE")
print("=" * 75)
quant_tools = [
    ("Factor Momentum (Jegadeesh-Titman)", "Ruota gli asset ogni mese verso quelli con momentum positivo a 6-12 mesi", "+1-3% annuo"),
    ("Mean-Variance Optimization (Markowitz)", "GIÀ IMPLEMENTATO — ribilancia i pesi ogni mese", "+0.5-1.5% annuo"),
    ("Risk Parity (Bridgewater-style)", "Equalizza il rischio tra asset class, non il capitale", "+0.5-1% annuo"),
    ("Black-Litterman Model", "Combina views di mercato con l'equilibrio CAPM", "+0.5-1.5% annuo"),
    ("Fama-French 5-Factor Screening", "Seleziona azioni per Size, Value, Profitability, Investment", "+1-2% annuo"),
    ("Regime Detection (Hidden Markov)", "Identifica bull/bear regime e cambia allocazione", "+1-2% annuo"),
    ("Pairs Trading / Stat Arb", "Sfrutta le coppie di azioni correlate che divergono temporaneamente", "+2-5% annuo (ALTO RISCHIO)"),
    ("Options Wheel Strategy", "Vendi put cash-secured su azioni che vuoi, incassa premio", "+3-8% annuo (SE DISPONIBILE)"),
    ("Dollar Cost Averaging Ottimizzato", "Investi di più quando VIX è alto (mercato in panico)", "+0.5-1% annuo"),
    ("Tail Risk Hedging (VIX-based)", "Riduci esposizione quando VIX supera soglie critiche", "Riduce drawdown 30-50%"),
]
for i, (name, desc, alpha) in enumerate(quant_tools, 1):
    print(f"\n  {i:2d}. {name}")
    print(f"      {desc}")
    print(f"      Alpha stimato: {alpha}")

print("\n\n  ⚠️  DISCLAIMER: Nessun alpha è garantito. I rendimenti passati NON garantiscono")
print("     rendimenti futuri. L'alpha stimato è basato su studi accademici e potrebbe")
print("     non replicarsi perfettamente in un portafoglio di questa dimensione.")
print("=" * 75)
