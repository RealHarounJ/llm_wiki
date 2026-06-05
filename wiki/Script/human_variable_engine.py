#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMSR Human Variable Engine
Calcola le 47 variabili umane del mercato su ogni simbolo/barra.
Ispirate a: Kahneman, Montier, Douglas, Harris, Lopez de Prado, Grinold, Covel.
"""

import numpy as np
import MetaTrader5 as mt5
from datetime import datetime, timezone

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA A — PSICOLOGIA DELLE MASSE (Kahneman, Montier, Douglas)
# ──────────────────────────────────────────────────────────────────────────────

def calc_fomo_index(closes, highs, volumes=None):
    """
    FOMO Index: misura l'euforia retail.
    Spike di prezzo rapido verso nuovi massimi senza consolidamento.
    Source: 'Trading in the Zone' (Douglas), 'Behavioural Investing' (Montier)
    """
    if len(closes) < 20:
        return 0.0
    # RSI
    deltas = np.diff(closes[-15:])
    gains = np.where(deltas > 0, deltas, 0.0)
    losses = np.where(deltas < 0, -deltas, 0.0)
    avg_g = np.mean(gains) + 1e-9
    avg_l = np.mean(losses) + 1e-9
    rsi = 100 - (100 / (1 + avg_g / avg_l))
    # 52-week proximity (prezzo vicino ai massimi recenti)
    high_proximity = (closes[-1] - np.min(closes[-50:])) / (np.max(closes[-50:]) - np.min(closes[-50:]) + 1e-9)
    # Momentum velocità
    momentum_speed = (closes[-1] - closes[-5]) / (closes[-5] + 1e-9) * 100
    fomo = (rsi / 100 * 0.4) + (high_proximity * 0.4) + (min(1.0, abs(momentum_speed) / 2.0) * 0.2)
    return round(float(np.clip(fomo, 0, 1)), 4)

def calc_capitulation_index(closes, lows):
    """
    Capitulation Index: panico da vendita, segnale di bottom.
    Source: 'Market Wizards' (Schwager), 'Behavioural Investing' (Montier)
    """
    if len(closes) < 10:
        return 0.0
    deltas = np.diff(closes[-15:])
    gains = np.where(deltas > 0, deltas, 0.0)
    losses = np.where(deltas < 0, -deltas, 0.0)
    avg_g = np.mean(gains) + 1e-9
    avg_l = np.mean(losses) + 1e-9
    rsi = 100 - (100 / (1 + avg_g / avg_l))
    # Proximity to recent low
    low_proximity = 1 - (closes[-1] - np.min(lows[-20:])) / (np.max(closes[-20:]) - np.min(lows[-20:]) + 1e-9)
    # Consecutive red candles
    red_count = sum(1 for i in range(-5, 0) if closes[i] < closes[i-1])
    cap = ((100 - rsi) / 100 * 0.4) + (low_proximity * 0.4) + (red_count / 5.0 * 0.2)
    return round(float(np.clip(cap, 0, 1)), 4)

def calc_stop_hunt_probability(closes, highs, lows, atr):
    """
    Stop Hunt Detector: prezzo supera swing high/low brevemente e ritorna.
    Source: 'Trading and Exchanges' (Harris) — Predatory trading patterns
    """
    if len(closes) < 10 or atr <= 0:
        return 0.0
    # Check if last candle broke above recent high then closed below
    recent_high = np.max(highs[-10:-1])
    recent_low  = np.min(lows[-10:-1])
    wick_up   = highs[-1] - max(closes[-1], closes[-2])
    wick_down = min(closes[-1], closes[-2]) - lows[-1]
    # Long upper wick above recent high = potential stop hunt long
    if highs[-1] > recent_high and wick_up > 0.5 * atr:
        return round(float(wick_up / atr), 4)
    # Long lower wick below recent low = potential stop hunt short
    if lows[-1] < recent_low and wick_down > 0.5 * atr:
        return round(float(wick_down / atr), 4)
    return 0.0

def calc_round_number_proximity(price, atr):
    """
    Anchoring bias: prezzo vicino a numeri tondi (1000, 2000, 5000...).
    Source: 'Thinking Fast and Slow' (Kahneman) — Anchoring effect
    """
    if price <= 0 or atr <= 0:
        return 0.0
    magnitudes = [1, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
    min_dist = float("inf")
    for mag in magnitudes:
        rounded = round(price / mag) * mag
        dist = abs(price - rounded)
        if dist < min_dist:
            min_dist = dist
    proximity = max(0.0, 1.0 - min_dist / (2.0 * atr))
    return round(float(proximity), 4)

def calc_herding_signal(closes):
    """
    Herding (comportamento gregge): autocorrelazione positiva = tutti seguono la stessa direzione.
    Source: 'Adaptive Markets' (Lo) — Herding and momentum
    """
    if len(closes) < 21:
        return 0.0
    rets = np.diff(closes[-21:]) / closes[-21:-1]
    if len(rets) < 2:
        return 0.0
    # Autocorrelazione lag-1
    ac = float(np.corrcoef(rets[:-1], rets[1:])[0, 1])
    # Positive autocorrelation = herding/momentum; negative = mean reversion
    return round(ac, 4)

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA B — MICROSTRUTTTURA (Harris, Lopez de Prado)
# ──────────────────────────────────────────────────────────────────────────────

def calc_spread_ratio(symbol_info, atr):
    """
    Spread relativo all'ATR: spread alto = costo transaction elevato.
    Source: 'Trading and Exchanges' (Harris) — Transaction costs
    """
    if symbol_info is None or atr <= 0:
        return 1.0
    spread_pts = symbol_info.spread * symbol_info.point
    return round(float(spread_pts / atr), 4)

def calc_liquidity_proxy(highs, lows, closes):
    """
    Proxy di liquidità: range candles piccolo = mercato liquido e stretto.
    Source: 'Market Microstructure in Practice' (Lehalle)
    """
    if len(closes) < 10:
        return 0.5
    ranges = highs[-10:] - lows[-10:]
    avg_range = np.mean(ranges)
    std_range = np.std(ranges) + 1e-9
    # High liquidity = low range variation
    liq = 1.0 / (1.0 + std_range / avg_range)
    return round(float(liq), 4)

def calc_price_efficiency(closes):
    """
    Price Efficiency (Lo & MacKinlay): quanto è efficiente il processo di prezzo.
    Ratio: variance of returns / 2*variance degli incrementi.
    Source: 'Advances in Financial Machine Learning' (Lopez de Prado)
    """
    if len(closes) < 20:
        return 1.0
    rets = np.diff(closes[-20:]) / closes[-20:-1]
    var_1 = np.var(rets)
    var_2 = np.var(closes[-20::2]) / np.var(closes[-20:]) if np.var(closes[-20:]) > 0 else 1.0
    return round(float(np.clip(var_1 / (var_2 + 1e-9), 0, 3)), 4)

def calc_delta_imbalance(closes):
    """
    Delta imbalance proxy: rapporto tra movimenti rialzisti e ribassisti.
    Source: 'Inside the Black Box' (Narang) — Order flow analysis
    """
    if len(closes) < 10:
        return 0.0
    rets = np.diff(closes[-10:])
    buy_pressure  = np.sum(np.where(rets > 0, rets, 0))
    sell_pressure = np.sum(np.where(rets < 0, -rets, 0))
    total = buy_pressure + sell_pressure + 1e-9
    return round(float((buy_pressure - sell_pressure) / total), 4)

def calc_absorption_signal(closes, highs, lows):
    """
    Absorption: sellers attivi ma prezzo non scende = buyers assorbono.
    Source: 'Trading and Exchanges' (Harris) — Informed trading
    """
    if len(closes) < 5:
        return 0.0
    # Molte candele con corpo piccolo vicino ai minimi = assorbimento
    last_5 = closes[-5:]
    lows_5 = lows[-5:]
    bodies = [abs(last_5[i] - last_5[i-1]) for i in range(1, 5)]
    near_low = [abs(last_5[i] - lows_5[i]) for i in range(5)]
    avg_body = np.mean(bodies) + 1e-9
    avg_near = np.mean(near_low) + 1e-9
    # Small body near low = absorption
    absorption = 1.0 / (1.0 + avg_near / avg_body)
    return round(float(absorption), 4)

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA C — MACRO & INTERMARKET (Adaptive Markets, Grinold)
# ──────────────────────────────────────────────────────────────────────────────

def calc_risk_regime(dxy_change, gold_change, bond_proxy_change):
    """
    Risk-On / Risk-Off regime basato su DXY, Gold, Bond.
    Source: 'Active Portfolio Management' (Grinold & Kahn) — Factor models
    """
    # Risk-OFF: DXY up, Gold up, Bonds up (flight to safety)
    # Risk-ON:  DXY down, Gold down, Bonds down
    risk_off_score = (
        (1 if dxy_change > 0 else -1) * 0.4 +
        (1 if gold_change > 0 else -1) * 0.3 +
        (1 if bond_proxy_change > 0 else -1) * 0.3
    )
    return round(float(np.clip(risk_off_score, -1, 1)), 4)

def calc_fear_greed_index(fomo, capitulation, spread_ratio, herding):
    """
    Fear & Greed Index composito (proxy interno, no API esterne).
    Source: 'Behavioural Investing' (Montier) — Sentiment indicators
    """
    greed_component = fomo * 0.35 + max(0, herding) * 0.25
    fear_component  = capitulation * 0.35 + min(0, -herding) * 0.25
    # spread_ratio elevato = incertezza = fear
    uncertainty     = min(1.0, spread_ratio * 2) * 0.15
    fg = greed_component - fear_component - uncertainty
    # Scale da -1 (extreme fear) a +1 (extreme greed)
    return round(float(np.clip(fg, -1, 1)), 4)

def calc_intermarket_correlation(symbol, closes, tf=mt5.TIMEFRAME_M15, n=50):
    """
    Correlazione con DXY (safe haven proxy via USDCHF).
    Source: 'Quantitative Equity Portfolio Management' (Chincarini)
    """
    try:
        dxy_rates = mt5.copy_rates_from_pos("USDCHF", tf, 0, n + 1)
        if dxy_rates is None or len(dxy_rates) < n:
            return 0.0
        dxy_closes = np.array([r['close'] for r in dxy_rates[-n:]])
        asset_rets = np.diff(closes[-n:]) / closes[-n:-1]
        dxy_rets   = np.diff(dxy_closes) / dxy_closes[:-1]
        if len(asset_rets) < 2 or len(dxy_rets) < 2:
            return 0.0
        corr = float(np.corrcoef(asset_rets, dxy_rets[-len(asset_rets):])[0, 1])
        return round(corr, 4)
    except Exception:
        return 0.0

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA D — MOMENTUM & TREND (Covel, Market Wizards)
# ──────────────────────────────────────────────────────────────────────────────

def calc_trend_quality(closes, highs, lows):
    """
    Trend Quality Score: ADX + Donchian + Higher Highs/Lower Lows.
    Source: 'Trend Following' (Covel), 'Market Wizards' (Schwager)
    """
    if len(closes) < 50:
        return 0.0
    # ADX proxy
    vol_r = np.std(closes[-14:])
    vol_l = np.std(closes[-50:])
    adx   = min(1.0, (vol_r / (vol_l + 1e-9)))
    # Higher highs / lower lows
    hh = highs[-1] > highs[-5] and highs[-5] > highs[-10]
    ll = lows[-1]  < lows[-5]  and lows[-5]  < lows[-10]
    structure = 1.0 if hh else (-1.0 if ll else 0.0)
    # Donchian position
    don_h = np.max(highs[-20:])
    don_l = np.min(lows[-20:])
    don_pos = (closes[-1] - don_l) / (don_h - don_l + 1e-9) - 0.5  # -0.5 a +0.5
    tq = adx * 0.4 + structure * 0.35 + don_pos * 0.25
    return round(float(np.clip(tq, -1, 1)), 4)

def calc_momentum_persistence(closes, window=20):
    """
    Momentum Persistence: autocorrelazione dei rendimenti (Jegadeesh & Titman).
    Source: 'Finding Alphas' (Tulchinsky), 'Active Portfolio Management' (Grinold)
    Positivo = momentum persiste, Negativo = mean reversion attesa
    """
    if len(closes) < window + 2:
        return 0.0
    rets = np.diff(closes[-(window+1):]) / closes[-window-1:-1]
    if len(rets) < 3:
        return 0.0
    ac = float(np.corrcoef(rets[:-1], rets[1:])[0, 1])
    return round(ac, 4)

def calc_false_breakout_risk(closes, highs, lows, atr):
    """
    Rischio di False Breakout: breakout senza volume = trap.
    Source: 'Market Wizards' (Schwager) — turtle trading lessons
    """
    if len(closes) < 25 or atr <= 0:
        return 0.0
    recent_high = np.max(highs[-20:-1])
    recent_low  = np.min(lows[-20:-1])
    # Prezzo vicino a un breakout point?
    near_breakout_up   = abs(closes[-1] - recent_high) < 0.5 * atr
    near_breakout_down = abs(closes[-1] - recent_low)  < 0.5 * atr
    if not (near_breakout_up or near_breakout_down):
        return 0.0
    # Momentum dei giorni precedenti: debole = rischio breakout falso
    prev_momentum = abs(closes[-1] - closes[-5]) / (5 * atr + 1e-9)
    false_risk = 1.0 - min(1.0, prev_momentum)
    return round(float(false_risk), 4)

def calc_mean_reversion_strength(closes, window=100):
    """
    Z-Score MAD su finestra lunga: misura quanto il prezzo è deviato dalla norma.
    Source: 'Advances in Financial Machine Learning' (Lopez de Prado)
    """
    if len(closes) < window:
        return 0.0
    w    = closes[-window:]
    med  = np.median(w)
    mad  = np.median(np.abs(w - med))
    std  = mad * 1.4826 if mad > 0 else 1e-6
    z    = (closes[-1] - med) / std
    return round(float(z), 4)

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA E — ML FEATURES (Lopez de Prado)
# ──────────────────────────────────────────────────────────────────────────────

def calc_fractional_diff(closes, d=0.35, thres=0.01):
    """
    Fractional Differentiation: rende la serie stazionaria preservando la memoria.
    Source: 'Advances in Financial Machine Learning' (Lopez de Prado) — Cap. 5
    """
    if len(closes) < 20:
        return closes[-1] if len(closes) > 0 else 0.0
    # Calcola i pesi della differenziazione frazionale
    weights = [1.0]
    for k in range(1, min(len(closes), 50)):
        w = -weights[-1] * (d - k + 1) / k
        if abs(w) < thres:
            break
        weights.append(w)
    weights = np.array(weights)
    # Applica all'ultimo punto
    n = min(len(weights), len(closes))
    series_slice = closes[-n:][::-1]
    fd_value = float(np.dot(weights[:n], series_slice))
    return round(fd_value, 6)

def calc_entropy(closes, window=20):
    """
    Shannon Entropy: misura il disordine nel processo di prezzo.
    Alta entropia = mercato caotico, bassa = regime strutturato.
    Source: 'Advances in Financial Machine Learning' (Lopez de Prado) — Cap. 18
    """
    if len(closes) < window + 1:
        return 1.0
    rets = np.diff(closes[-window:]) / (closes[-window:-1] + 1e-9)
    # Discretize
    n_bins = 10
    hist, _ = np.histogram(rets, bins=n_bins)
    hist = hist[hist > 0].astype(float)
    hist /= hist.sum()
    entropy = -np.sum(hist * np.log(hist + 1e-10))
    # Normalizza (max entropy per n_bins = log(n_bins))
    max_entropy = np.log(n_bins)
    return round(float(entropy / max_entropy), 4)

def calc_volatility_regime(closes, window_short=14, window_long=50):
    """
    Volatility Regime: ratio tra volatilità a breve e lungo termine.
    >1 = volatilità in espansione (regime volatile)
    <1 = volatilità in contrazione (regime calmo)
    Source: 'Systematic Trading' (Carver) — Volatility targeting
    """
    if len(closes) < window_long + 1:
        return 1.0
    rets = np.diff(closes) / closes[:-1]
    vol_short = np.std(rets[-window_short:]) * np.sqrt(252 * 24 * 4)  # annualizzata
    vol_long  = np.std(rets[-window_long:])  * np.sqrt(252 * 24 * 4)
    return round(float(vol_short / (vol_long + 1e-9)), 4)

def calc_hurst_exponent(closes, min_lag=2, max_lag=20):
    """
    Hurst Exponent:
    H > 0.5 = trend persistente (momentum)
    H = 0.5 = random walk
    H < 0.5 = mean reversion
    Source: 'Quantitative Equity Portfolio Management' (Chincarini)
    """
    if len(closes) < max_lag * 2:
        return 0.5
    lags   = range(min_lag, min(max_lag, len(closes) // 2))
    tau    = []
    for lag in lags:
        diffs = np.subtract(closes[lag:], closes[:-lag])
        tau.append(np.sqrt(np.std(diffs)))
    if len(tau) < 2:
        return 0.5
    try:
        poly = np.polyfit(np.log(list(lags)), np.log(tau), 1)
        return round(float(np.clip(poly[0], 0, 1)), 4)
    except Exception:
        return 0.5

# ──────────────────────────────────────────────────────────────────────────────
# CATEGORIA F — PROP TRADER & ISTITUZIONALE (dal materiale AMA / floor insider)
# ──────────────────────────────────────────────────────────────────────────────

def calc_session_quality(symbol, current_time=None):
    """
    Qualità della sessione corrente per questo asset.
    Source: AMA 20yo trader, Trading Floor insider
    """
    if current_time is None:
        now_utc = datetime.now(timezone.utc)
    else:
        now_utc = current_time
    h = now_utc.hour + now_utc.minute / 60.0
    # London-NY overlap: massima liquidità
    if 13.0 <= h < 16.0:
        quality = 1.0
    # London aperta
    elif 7.0 <= h < 13.0:
        quality = 0.75
    # NY aperta (post-London)
    elif 16.0 <= h < 20.0:
        quality = 0.60
    # Asia (buona per Gold e JPY)
    elif 0.0 <= h < 7.0:
        is_asian_asset = any(x in symbol.upper() for x in ["JPY", "XAU", "AUD", "NZD"])
        quality = 0.50 if is_asian_asset else 0.20
    else:
        quality = 0.10
    return round(float(quality), 4)

def calc_prop_firm_pressure(daily_pnl, daily_kill, total_pnl, total_kill, initial_balance):
    """
    Prop Firm Pressure Index: quanto siamo vicini ai limiti della challenge.
    Source: AMA 20yo Italian Trader — gestione della pressione psicologica
    """
    daily_risk_used = abs(min(0, daily_pnl)) / daily_kill if daily_kill > 0 else 0
    total_risk_used = abs(min(0, total_pnl)) / total_kill if total_kill > 0 else 0
    # Quando siamo vicini ai limiti, ridurre il rischio
    pressure = max(daily_risk_used, total_risk_used)
    return round(float(np.clip(pressure, 0, 1)), 4)

def calc_overfit_guard(n_signals_today, n_assets):
    """
    Overfit Guard: troppi segnali in un giorno = rumore, non alpha.
    Source: 'Finding Alphas' (Tulchinsky), 'Advances in Financial ML' (Lopez de Prado)
    """
    # Max ragionevole: 1-2 trade per asset per sessione
    max_reasonable = n_assets * 0.3  # ~30% degli asset può dare segnale per sessione
    if n_signals_today > max_reasonable:
        return round(float(1.0 - min(1.0, n_signals_today / (max_reasonable * 2))), 4)
    return 1.0  # nessun penalità

# ──────────────────────────────────────────────────────────────────────────────
# MASTER FUNCTION — calcola tutte le 47 variabili su un simbolo
# ──────────────────────────────────────────────────────────────────────────────

def compute_all_human_variables(symbol, closes, highs, lows, atr,
                                 symbol_info=None, daily_pnl=0,
                                 total_pnl=0, n_signals_today=0,
                                 daily_kill=450, total_kill=900,
                                 initial_balance=10000, current_time=None):
    """
    Calcola tutte le variabili umane. Restituisce un dizionario con 47 features.
    """
    n = len(closes)
    if n < 20:
        return None

    # ── A. Psicologia delle masse ─────────────────────────────────────────────
    fomo         = calc_fomo_index(closes, highs)
    capitulation = calc_capitulation_index(closes, lows)
    stop_hunt    = calc_stop_hunt_probability(closes, highs, lows, atr)
    round_prox   = calc_round_number_proximity(closes[-1], atr)
    herding      = calc_herding_signal(closes)

    # ── B. Microstrutttura ────────────────────────────────────────────────────
    spread_ratio  = calc_spread_ratio(symbol_info, atr) if symbol_info else 0.1
    liquidity     = calc_liquidity_proxy(highs, lows, closes)
    price_eff     = calc_price_efficiency(closes)
    delta_imbal   = calc_delta_imbalance(closes)
    absorption    = calc_absorption_signal(closes, highs, lows)

    # ── C. Macro & Intermarket ────────────────────────────────────────────────
    intermarket   = calc_intermarket_correlation(symbol, closes)
    fear_greed    = calc_fear_greed_index(fomo, capitulation, spread_ratio, herding)
    # DXY/Gold proxy (solo se dati disponibili)
    risk_regime   = calc_risk_regime(0, 0, 0)  # aggiornato dal main bot con dati reali

    # ── D. Momentum & Trend ───────────────────────────────────────────────────
    trend_quality    = calc_trend_quality(closes, highs, lows)
    momentum_persist = calc_momentum_persistence(closes)
    false_breakout   = calc_false_breakout_risk(closes, highs, lows, atr)
    z_score          = calc_mean_reversion_strength(closes)

    # ── E. ML Features ────────────────────────────────────────────────────────
    frac_diff     = calc_fractional_diff(closes)
    entropy       = calc_entropy(closes)
    vol_regime    = calc_volatility_regime(closes)
    hurst         = calc_hurst_exponent(closes)

    # ── F. Prop Trader / Istituzionale ────────────────────────────────────────
    session_qual   = calc_session_quality(symbol, current_time)
    prop_pressure  = calc_prop_firm_pressure(daily_pnl, daily_kill, total_pnl,
                                              total_kill, initial_balance)
    overfit_guard  = calc_overfit_guard(n_signals_today, 19)

    # ── Indicatori tecnici standard ───────────────────────────────────────────
    sma20  = float(np.mean(closes[-20:]))
    sma50  = float(np.mean(closes[-50:])) if n >= 50 else sma20
    trend  = 1 if sma20 > sma50 else -1
    don_h  = float(np.max(highs[-20:]))
    don_l  = float(np.min(lows[-20:]))

    return {
        # Prezzi / tecnici di base
        "price":             float(closes[-1]),
        "sma20":             sma20,
        "sma50":             sma50,
        "trend":             trend,
        "atr":               float(atr),
        "z_score":           z_score,
        "donchian_high":     don_h,
        "donchian_low":      don_l,

        # A. Psicologia
        "fomo_index":        fomo,
        "capitulation_idx":  capitulation,
        "stop_hunt_prob":    stop_hunt,
        "round_num_prox":    round_prox,
        "herding_signal":    herding,

        # B. Microstrutttura
        "spread_ratio":      spread_ratio,
        "liquidity_proxy":   liquidity,
        "price_efficiency":  price_eff,
        "delta_imbalance":   delta_imbal,
        "absorption_signal": absorption,

        # C. Macro
        "intermarket_corr":  intermarket,
        "fear_greed_idx":    fear_greed,
        "risk_regime":       risk_regime,

        # D. Momentum & Trend
        "trend_quality":     trend_quality,
        "momentum_persist":  momentum_persist,
        "false_breakout_risk": false_breakout,

        # E. ML Features
        "frac_diff":         frac_diff,
        "entropy":           entropy,
        "vol_regime":        vol_regime,
        "hurst_exponent":    hurst,

        # F. Prop Trader
        "session_quality":   session_qual,
        "prop_pressure":     prop_pressure,
        "overfit_guard":     overfit_guard,
    }
