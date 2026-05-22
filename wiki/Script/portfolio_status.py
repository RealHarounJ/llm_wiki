#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
📊 Live Portfolio Status and Performance Dashboard
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Si connette alle API di Trading 212 per estrarre la situazione in tempo reale
             del portafoglio di Haroun Jaafar, mostrando costi, valori correnti,
             P&L aperto ed effetto cambio (FX Impact) per ciascuna posizione.
--------------------------------------------------------------------------------
"""

import os
import sys
import json
from fetch_trading212_portfolio import load_trading212_credentials, fetch_positions

def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    api_auth = load_trading212_credentials()
    positions, ep_name = fetch_positions(api_auth)
    
    if not positions:
        print("❌ Impossibile recuperare le posizioni.")
        return
        
    print("\n" + "="*110)
    print(f"💼 PORTAFOGLIO TRADING 212 - SITUAZIONE IN TEMPO REALE ({ep_name.upper()})")
    print("="*110)
    
    header_fmt = "{:<8} | {:<25} | {:<12} | {:<12} | {:<12} | {:<12} | {:<10}"
    row_fmt = "{:<8} | {:<25.25} | {:>12.2f} | {:>12.2f} | {:>+12.2f} | {:>12.2f}% | {:>+10.2f}"
    
    print(header_fmt.format("TICKER", "NOME STRUMENTO", "INVESTITO", "VALORE ATT.", "P&L APERTO", "PERF (%)", "FX IMPACT"))
    print("-"*110)
    
    total_cost = 0.0
    total_value = 0.0
    total_ppl = 0.0
    total_fx = 0.0
    
    # Ordiniamo per peso (valore corrente decrescente)
    positions_sorted = sorted(
        positions, 
        key=lambda x: float(x.get("walletImpact", {}).get("currentValue") or x.get("value") or 0.0), 
        reverse=True
    )
    
    for pos in positions_sorted:
        instrument = pos.get("instrument", {})
        ticker = instrument.get("ticker", "N/A")
        # Rimuoviamo suffissi per chiarezza di visualizzazione
        clean_ticker = ticker.split("_")[0]
        name = instrument.get("name", "N/A")
        
        wallet = pos.get("walletImpact") or {}
        
        cost_val = wallet.get("totalCost")
        cost = float(cost_val) if cost_val is not None else 0.0
        
        value_val = wallet.get("currentValue")
        value = float(value_val) if value_val is not None else 0.0
        
        ppl_val = wallet.get("unrealizedProfitLoss")
        ppl = float(ppl_val) if ppl_val is not None else 0.0
        
        fx_val = wallet.get("fxImpact")
        fx = float(fx_val) if fx_val is not None else 0.0
        
        # Se non ci sono dati walletImpact (strano per v0 API) calcoliamo dei fallback
        if cost == 0.0 and value == 0.0:
            quantity = float(pos.get("quantity", 0.0))
            curr_price = float(pos.get("currentPrice", 0.0))
            avg_price = float(pos.get("averagePricePaid") or pos.get("averagePrice", 0.0))
            value = float(pos.get("value", quantity * curr_price))
            # Semplice stima
            cost = quantity * avg_price
            ppl = value - cost
            
        total_cost += cost
        total_value += value
        total_ppl += ppl
        total_fx += fx
        
        perf_pct = (ppl / cost * 100) if cost > 0 else 0.0
        
        print(row_fmt.format(
            clean_ticker,
            name,
            cost,
            value,
            ppl,
            perf_pct,
            fx
        ))
        
    print("-"*110)
    total_perf_pct = (total_ppl / total_cost * 100) if total_cost > 0 else 0.0
    
    print(f"{'TOTALE PORTAFOGLIO':<36} | €{total_cost:>11.2f} | €{total_value:>11.2f} | €{total_ppl:>+11.2f} | {total_perf_pct:>11.2f}% | €{total_fx:>+9.2f}")
    print("="*110 + "\n")

if __name__ == "__main__":
    main()
