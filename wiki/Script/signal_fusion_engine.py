#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMSR Signal Fusion Engine
Combina le variabili umane calcolate per stimare una confluenza direzionale (BUY/SELL)
utilizzando pesi dinamici adattati al regime di mercato corrente.
"""

import numpy as np

# Pesi dinamici dei macro-gruppi in base al regime
REGIME_WEIGHTS = {
    "TRENDING": {
        "momentum": 0.40,
        "microstructure": 0.25,
        "behavioral": 0.20,
        "macro": 0.15
    },
    "RANGING": {
        "mean_reversion": 0.45,
        "behavioral": 0.25,
        "microstructure": 0.20,
        "macro": 0.10
    },
    "VOLATILE": {
        "macro": 0.40,
        "behavioral": 0.30,
        "momentum": 0.15,
        "microstructure": 0.15
    },
    "BREAKOUT": {
        "momentum": 0.45,
        "microstructure": 0.30,
        "behavioral": 0.15,
        "macro": 0.10
    }
}

def determine_regime(features):
    """
    Rileva il regime di mercato usando le variabili di volatilità, trend ed entropia.
    """
    vol_regime = features.get("vol_regime", 1.0)
    trend_quality = abs(features.get("trend_quality", 0.0))
    hurst = features.get("hurst_exponent", 0.5)
    entropy = features.get("entropy", 0.5)
    
    # 1. Regimi estremi
    if vol_regime > 1.5 or (entropy > 0.8 and trend_quality < 0.2):
        return "VOLATILE"
        
    # 2. Regimi di Trend vs Range
    if hurst > 0.60 or trend_quality > 0.5:
        # Se siamo vicino ai massimi/minimi donchian, potrebbe essere breakout
        price = features.get("price", 0.0)
        don_h = features.get("donchian_high", 0.0)
        don_l = features.get("donchian_low", 0.0)
        false_break_risk = features.get("false_breakout_risk", 0.5)
        
        # Vicinanza ai confini
        don_range = don_h - don_l + 1e-9
        prox_high = abs(price - don_h) / don_range
        prox_low = abs(price - don_l) / don_range
        
        if (prox_high < 0.05 or prox_low < 0.05) and false_break_risk < 0.4:
            return "BREAKOUT"
        return "TRENDING"
        
    # 3. Default a RANGING
    return "RANGING"

def fuse_signals(features):
    """
    Combina le variabili per calcolare segnali BUY e SELL e un livello di confidenza.
    Restituisce: (buy_score, sell_score, regime, confidence_interval, breakdown)
    Scores sono tra 0 e 100.
    """
    regime = determine_regime(features)
    weights = REGIME_WEIGHTS[regime]
    
    # Estrazione delle features chiave
    z_score = features.get("z_score", 0.0)
    trend = features.get("trend", 0)
    trend_qual = features.get("trend_quality", 0.0)
    fomo = features.get("fomo_index", 0.0)
    capitulation = features.get("capitulation_idx", 0.0)
    stop_hunt = features.get("stop_hunt_prob", 0.0)
    round_prox = features.get("round_num_prox", 0.0)
    herding = features.get("herding_signal", 0.0)
    delta_imbalance = features.get("delta_imbalance", 0.0)
    absorption = features.get("absorption_signal", 0.0)
    fear_greed = features.get("fear_greed_idx", 0.0)
    intermarket = features.get("intermarket_corr", 0.0)
    risk_regime = features.get("risk_regime", 0.0)
    session_qual = features.get("session_quality", 0.5)
    prop_pressure = features.get("prop_pressure", 0.0)
    overfit_guard = features.get("overfit_guard", 1.0)
    
    # ──────────────────────────────────────────────────────────────────────────
    # 1. PUNTI BUY
    # ──────────────────────────────────────────────────────────────────────────
    
    # Momentum (TF & Breakout)
    buy_mom = 0.0
    if trend > 0:
        buy_mom += 40
    if trend_qual > 0:
        buy_mom += trend_qual * 60
        
    # Mean Reversion (Z-score negativo = ipervenduto)
    buy_mr = 0.0
    if z_score < -1.5:
        buy_mr += min(100.0, abs(z_score) * 25.0)
        
    # Microstruttura (Delta positivo = acquisti aggressivi, stop hunt short = rimbalzo rialzista)
    buy_micro = 0.0
    if delta_imbalance > 0:
        buy_micro += delta_imbalance * 40
    if stop_hunt > 0 and z_score < 0: # Caccia agli stop sui minimi
        buy_micro += stop_hunt * 40
    if absorption > 0.6 and z_score < 0: # Assorbimento sellers
        buy_micro += absorption * 20
        
    # Comportamentale (Ipervenduto/Capitolazione = buy, Fear elevato = contrarian buy)
    buy_beh = 0.0
    if capitulation > 0.5:
        buy_beh += capitulation * 40
    if fear_greed < -0.3: # Paura estrema
        buy_beh += abs(fear_greed) * 30
    if round_prox > 0.7 and z_score < 0: # Supporto a numero tondo
        buy_beh += round_prox * 30
        
    # Macro / Intermarket / Sessione
    buy_macro = 50.0 # baseline neutral
    if risk_regime < 0: # Risk-on favorisce indici/gold
        buy_macro += abs(risk_regime) * 25
    if intermarket > 0.4:
        buy_macro += intermarket * 25
    buy_macro = buy_macro * session_qual
    
    # ──────────────────────────────────────────────────────────────────────────
    # 2. PUNTI SELL
    # ──────────────────────────────────────────────────────────────────────────
    
    # Momentum
    sell_mom = 0.0
    if trend < 0:
        sell_mom += 40
    if trend_qual < 0:
        sell_mom += abs(trend_qual) * 60
        
    # Mean Reversion (Z-score positivo = ipercomprato)
    sell_mr = 0.0
    if z_score > 1.5:
        sell_mr += min(100.0, z_score * 25.0)
        
    # Microstruttura
    sell_micro = 0.0
    if delta_imbalance < 0:
        sell_micro += abs(delta_imbalance) * 40
    if stop_hunt > 0 and z_score > 0: # Caccia agli stop sui massimi
        sell_micro += stop_hunt * 40
    if absorption > 0.6 and z_score > 0: # Assorbimento buyers sui massimi
        sell_micro += absorption * 20
        
    # Comportamentale (FOMO = sell contrarian, Greed elevato = sell contrarian)
    sell_beh = 0.0
    if fomo > 0.6:
        sell_beh += fomo * 40
    if fear_greed > 0.3: # Avidità estrema
        sell_beh += fear_greed * 30
    if round_prox > 0.7 and z_score > 0: # Resistenza a numero tondo
        sell_beh += round_prox * 30
        
    # Macro / Intermarket
    sell_macro = 50.0
    if risk_regime > 0: # Risk-off favorisce DXY / scende azionario
        sell_macro += risk_regime * 25
    if intermarket < -0.4:
        sell_macro += abs(intermarket) * 25
    sell_macro = sell_macro * session_qual

    # ──────────────────────────────────────────────────────────────────────────
    # FUSION IN BASE AL REGIME
    # ──────────────────────────────────────────────────────────────────────────
    
    breakdown_buy = {}
    breakdown_sell = {}
    
    if regime in ["TRENDING", "BREAKOUT"]:
        w = weights
        buy_score = (buy_mom * w["momentum"] + 
                     buy_micro * w["microstructure"] + 
                     buy_beh * w["behavioral"] + 
                     buy_macro * w["macro"])
                     
        sell_score = (sell_mom * w["momentum"] + 
                      sell_micro * w["microstructure"] + 
                      sell_beh * w["behavioral"] + 
                      sell_macro * w["macro"])
                      
        breakdown_buy = {"momentum": buy_mom, "micro": buy_micro, "behavioral": buy_beh, "macro": buy_macro}
        breakdown_sell = {"momentum": sell_mom, "micro": sell_micro, "behavioral": sell_beh, "macro": sell_macro}
        
    elif regime == "RANGING":
        w = weights
        buy_score = (buy_mr * w["mean_reversion"] + 
                     buy_beh * w["behavioral"] + 
                     buy_micro * w["microstructure"] + 
                     buy_macro * w["macro"])
                     
        sell_score = (sell_mr * w["mean_reversion"] + 
                      sell_beh * w["behavioral"] + 
                      sell_micro * w["microstructure"] + 
                      sell_macro * w["macro"])
                      
        breakdown_buy = {"mean_reversion": buy_mr, "behavioral": buy_beh, "micro": buy_micro, "macro": buy_macro}
        breakdown_sell = {"mean_reversion": sell_mr, "behavioral": sell_beh, "micro": sell_micro, "macro": sell_macro}
        
    else: # VOLATILE
        w = weights
        buy_score = (buy_macro * w["macro"] + 
                     buy_beh * w["behavioral"] + 
                     buy_mom * w["momentum"] + 
                     buy_micro * w["microstructure"])
                     
        sell_score = (sell_macro * w["macro"] + 
                      sell_beh * w["behavioral"] + 
                      sell_mom * w["momentum"] + 
                      sell_micro * w["microstructure"])
                      
        breakdown_buy = {"macro": buy_macro, "behavioral": buy_beh, "momentum": buy_mom, "micro": buy_micro}
        breakdown_sell = {"macro": sell_macro, "behavioral": sell_beh, "momentum": sell_mom, "micro": sell_micro}

    # Penalizzazione per sovrapressione psicologica (Prop Firm) & Overfit Guard
    # Più alta è la pressione, più riduciamo lo score per evitare trade forzati
    pressure_penalty = 1.0 - (prop_pressure * 0.4)
    
    buy_score = float(np.clip(buy_score * pressure_penalty * overfit_guard, 0, 100))
    sell_score = float(np.clip(sell_score * pressure_penalty * overfit_guard, 0, 100))
    
    # Confidenza basata sulla convergenza delle features (es. deviazione standard interna delle parti)
    vals_buy = list(breakdown_buy.values())
    vals_sell = list(breakdown_sell.values())
    std_buy = np.std(vals_buy) if len(vals_buy) > 0 else 50
    std_sell = np.std(vals_sell) if len(vals_sell) > 0 else 50
    
    # Bassa deviazione standard = alta convergenza = alta confidenza
    confidence_buy = max(0.0, 100.0 - std_buy * 1.5)
    confidence_sell = max(0.0, 100.0 - std_sell * 1.5)
    
    confidence = round(float((confidence_buy + confidence_sell) / 2.0), 2)

    return {
        "buy_score": round(buy_score, 2),
        "sell_score": round(sell_score, 2),
        "regime": regime,
        "confidence": confidence,
        "breakdown": {
            "regime_weights": weights,
            "buy_breakdown": {k: round(v, 2) for k, v in breakdown_buy.items()},
            "sell_breakdown": {k: round(v, 2) for k, v in breakdown_sell.items()},
            "prop_pressure_multiplier": round(pressure_penalty, 4),
            "overfit_guard_multiplier": round(overfit_guard, 4)
        }
    }
