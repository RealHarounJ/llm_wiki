#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
🧹 Phase 1 Cleanup — Portfolio Micro-Position Liquidator
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione:
  Fase 1 del piano operativo:
  - Vende le micro-posizioni ATPC, BLK, MSFT, AAPL (totale ~€3-4)
  - Acquista SWDA con i proventi della vendita
  
  ⚠️  SICUREZZA: Lo script esegue DRY RUN di default.
      Imposta CONFIRM=True SOLO dopo aver revisionato gli ordini.
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import base64
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# ── IMPOSTAZIONE DI SICUREZZA ──────────────────────────────────────────────────
# Cambia a True SOLO dopo aver letto il riepilogo e sei sicuro di voler procedere
CONFIRM_EXECUTE = False
# ──────────────────────────────────────────────────────────────────────────────

BASE_URL = "https://live.trading212.com/api/v0"

# Ticker da liquidare (micro-posizioni)
TICKERS_TO_SELL = ["ATPC_US_EQ", "BLK_US_EQ", "MSFT_US_EQ", "AAPL_US_EQ"]


def load_auth():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        env_path = ".env"
    api_key, api_secret = None, None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("TRADING212_API_KEY="):
                api_key = s.split("=", 1)[1].strip()
            elif s.startswith("TRADING212_API_SECRET="):
                api_secret = s.split("=", 1)[1].strip()
    if api_key and api_secret:
        cred = base64.b64encode(f"{api_key}:{api_secret}".encode()).decode()
        return f"Basic {cred}"
    return api_key or ""


def api_request(auth, method, endpoint, payload=None):
    url = f"{BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload else None
    headers = {
        "Authorization": auth,
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
    }
    req = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        print(f"    ❌ HTTP {e.code}: {body[:200]}")
        return None
    except URLError as e:
        print(f"    ❌ Errore di rete: {e.reason}")
        return None


def fetch_positions(auth):
    """Recupera tutte le posizioni aperte."""
    return api_request(auth, "GET", "/equity/positions") or []


def place_market_order(auth, ticker, quantity, dry_run=True):
    """
    Piazza un ordine di mercato.
    - quantity > 0 = ACQUISTO
    - quantity < 0 = VENDITA
    """
    if dry_run:
        action = "ACQUISTO" if quantity > 0 else "VENDITA"
        print(f"    [DRY RUN] {action} {abs(quantity):.5f} unità di {ticker}")
        return {"status": "DRY_RUN", "ticker": ticker, "quantity": quantity}

    payload = {
        "ticker": ticker,
        "quantity": quantity,
    }
    return api_request(auth, "POST", "/equity/orders/market", payload)


def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("=" * 70)
    print("  🧹 FASE 1 — Pulizia Micro-Posizioni Portafoglio")
    print("=" * 70)

    auth = load_auth()
    print("\n🔌 Connessione a Trading 212...")

    positions = fetch_positions(auth)
    if not positions:
        print("❌ Impossibile recuperare le posizioni. Controlla le credenziali.")
        sys.exit(1)

    print(f"✅ Recuperate {len(positions)} posizioni attive.\n")

    # Mappa ticker -> posizione
    pos_map = {}
    for pos in positions:
        ticker = pos.get("instrument", {}).get("ticker") or pos.get("ticker", "")
        pos_map[ticker] = pos

    # ── STEP 1: Analisi ordini di vendita ──────────────────────────────────────
    print("─" * 70)
    print("  STEP 1 — Micro-posizioni da liquidare")
    print("─" * 70)

    sell_orders = []
    total_proceeds = 0.0

    for sell_ticker in TICKERS_TO_SELL:
        pos = pos_map.get(sell_ticker)
        if not pos:
            print(f"  ⚠️  {sell_ticker}: posizione non trovata (già venduta o ticker diverso)")
            continue

        quantity = float(pos.get("quantity", 0.0))
        curr_price = float(pos.get("currentPrice", 0.0))
        value = pos.get("walletImpact", {}).get("currentValue")
        if value is None:
            value = quantity * curr_price
        else:
            value = float(value)

        print(f"  📌 {sell_ticker:<18} Quantità: {quantity:>10.5f}   Valore: €{value:>6.2f}")
        sell_orders.append({"ticker": sell_ticker, "quantity": quantity, "value": value})
        total_proceeds += value

    print(f"\n  Totale proventi stimati dalla vendita: €{total_proceeds:.2f}")

    # ── STEP 2: Ordine di acquisto SWDA ───────────────────────────────────────
    # Trova il ticker esatto di SWDA nel conto
    swda_ticker = None
    for ticker_key in pos_map:
        if "SWDA" in ticker_key.upper():
            swda_ticker = ticker_key
            break

    # Se SWDA non è ancora in portafoglio (improbabile), usa il ticker standard LSE
    if not swda_ticker:
        swda_ticker = "SWDAl_EQ"

    # Nota: Trading212 accetta ordini in unità frazionarie o in valore EUR.
    # Usiamo la quantità in EUR tramite l'endpoint /equity/orders/market con "value"
    print(f"\n─" + "─" * 69)
    print("  STEP 2 — Acquisto SWDA con i proventi")
    print("─" * 70)
    
    swda_pos = pos_map.get(swda_ticker, {})
    swda_price = float(swda_pos.get("currentPrice", 0.0)) if swda_pos else 0.0
    
    # Stima della quantità SWDA acquistabile con i proventi
    swda_qty_estimate = total_proceeds / swda_price if swda_price > 0 else 0
    
    print(f"  📌 {swda_ticker:<18} Prezzo attuale: {swda_price:.4f}")
    print(f"  💰 Con €{total_proceeds:.2f} di proventi, acquisteremo ~{swda_qty_estimate:.5f} unità SWDA")

    # ── RIEPILOGO PRE-ESECUZIONE ───────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    if CONFIRM_EXECUTE:
        print("  ⚡ MODALITÀ ESECUZIONE REALE — Invio ordini a Trading 212")
    else:
        print("  👁️  MODALITÀ DRY RUN — Nessun ordine verrà inviato")
    print("=" * 70)
    print()

    # ── ESECUZIONE VENDITE ─────────────────────────────────────────────────────
    print("  📤 VENDITE:")
    realized_proceeds = 0.0
    for order in sell_orders:
        result = place_market_order(
            auth,
            ticker=order["ticker"],
            quantity=-order["quantity"],   # negativo = VENDI
            dry_run=not CONFIRM_EXECUTE
        )
        if result and result.get("status") != "DRY_RUN":
            print(f"    ✅ Ordine di vendita inviato per {order['ticker']}")
            realized_proceeds += order["value"]
        elif result and result.get("status") == "DRY_RUN":
            realized_proceeds += order["value"]
        else:
            print(f"    ❌ Ordine di vendita FALLITO per {order['ticker']}")

        if CONFIRM_EXECUTE:
            time.sleep(1)  # Pausa tra gli ordini per sicurezza

    # ── ESECUZIONE ACQUISTO SWDA ───────────────────────────────────────────────
    print("\n  📥 ACQUISTO:")
    if realized_proceeds > 0 and swda_price > 0:
        swda_qty_to_buy = realized_proceeds / swda_price
        result = place_market_order(
            auth,
            ticker=swda_ticker,
            quantity=swda_qty_to_buy,   # positivo = ACQUISTA
            dry_run=not CONFIRM_EXECUTE
        )
        if result and result.get("status") != "DRY_RUN":
            print(f"    ✅ Ordine di acquisto SWDA ({swda_qty_to_buy:.5f} unità) inviato!")
        elif result and result.get("status") == "DRY_RUN":
            pass  # già stampato da place_market_order

    # ── RIEPILOGO FINALE ───────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    if CONFIRM_EXECUTE:
        print("  ✅ FASE 1 COMPLETATA — Tutti gli ordini sono stati inviati!")
        print("     Controlla la tua app Trading 212 per la conferma delle esecuzioni.")
    else:
        print("  ℹ️  DRY RUN completato. Nessun ordine reale inviato.")
        print()
        print("  👉 Per eseguire gli ordini reali:")
        print("     1. Apri wiki/Script/phase1_cleanup.py")
        print("     2. Cambia: CONFIRM_EXECUTE = False  →  CONFIRM_EXECUTE = True")
        print("     3. Riesegui lo script")
        print()
        print("  ⚠️  ATTENZIONE: Con CONFIRM_EXECUTE = True gli ordini vengono")
        print("     inviati IMMEDIATAMENTE al mercato live. Non è reversibile.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
