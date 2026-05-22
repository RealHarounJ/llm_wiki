#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script di deploy finale — v3.0 (Fixed pricing + correct tickers)
"""
import os, sys, json, base64, time, math, datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError

DRY_RUN      = False    # LIVE
NEW_CASH_EUR = 100.0
BASE_URL     = "https://live.trading212.com/api/v0"
POLY_URL     = "https://api.polygon.io/v2/aggs/ticker"

# ── PIANO ACQUISTI FISSO (calcolato dopo analisi catalog) ──────────────────────
# Pesi: SWDA 55%, EIMI 15%, SDIV 15%, BP 15%
# I ticker EIMI e SWDA sono già in portafoglio → usiamo il prezzo EUR dal portfolio
# SDIVm_EQ = Global X SuperDividend EUR (Euronext Milano) → prezzo EUR diretto
# BP_US_EQ = BP plc ADR USD → prezzo da Polygon convertito in EUR

def load_credentials():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path): env_path = ".env"
    ak, sk, pk = None, None, None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("TRADING212_API_KEY="): ak = s.split("=",1)[1].strip()
            elif s.startswith("TRADING212_API_SECRET="): sk = s.split("=",1)[1].strip()
            elif s.startswith("POLYGON_API_KEY="): pk = s.split("=",1)[1].strip()
    cred = base64.b64encode(f"{ak}:{sk}".encode()).decode()
    return f"Basic {cred}", pk

def t212(auth, method, endpoint, payload=None):
    url = f"{BASE_URL}{endpoint}"
    data = json.dumps(payload).encode() if payload else None
    headers = {"Authorization": auth, "User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    req = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(req) as r:
            return json.loads(r.read().decode())
    except HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"    ❌ HTTP {e.code}: {body[:300]}")
        return None
    except Exception as e:
        print(f"    ❌ {e}")
        return None

def poly_price_usd(ticker, pk):
    today = datetime.date.today()
    from_d = today - datetime.timedelta(days=7)
    url = (f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/"
           f"{from_d}/{today}?adjusted=true&sort=desc&limit=1&apiKey={pk}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as r:
            d = json.loads(r.read().decode())
            if d.get("results"): return float(d["results"][0]["c"])
    except: pass
    return 0.0

def eur_usd_rate(pk):
    """Recupera tasso EUR/USD da Polygon (quante USD per 1 EUR)."""
    today = datetime.date.today()
    from_d = today - datetime.timedelta(days=5)
    url = (f"https://api.polygon.io/v2/aggs/ticker/C:EURUSD/range/1/day/"
           f"{from_d}/{today}?adjusted=true&sort=desc&limit=1&apiKey={pk}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as r:
            d = json.loads(r.read().decode())
            if d.get("results"): return float(d["results"][0]["c"])
    except: pass
    return 1.10  # fallback

def eur_gbp_rate(pk):
    """Recupera tasso EUR/GBP da Polygon (quante GBP per 1 EUR)."""
    today = datetime.date.today()
    from_d = today - datetime.timedelta(days=5)
    url = (f"https://api.polygon.io/v2/aggs/ticker/C:EURGBP/range/1/day/"
           f"{from_d}/{today}?adjusted=true&sort=desc&limit=1&apiKey={pk}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as r:
            d = json.loads(r.read().decode())
            if d.get("results"): return float(d["results"][0]["c"])
    except: pass
    return 0.86  # fallback

def round_qty(qty, decimals=5):
    """Arrotonda la quantità a n decimali (T212 accetta max 5 per la maggior parte)."""
    factor = 10 ** decimals
    return math.floor(qty * factor) / factor

def main():
    print("=" * 70)
    print("  🌍 SMART DEPLOY v3.0 — Fixed Pricing & Correct Tickers")
    print(f"  {datetime.date.today():%d/%m/%Y} | €{NEW_CASH_EUR:.2f} | {'⚡ LIVE' if not DRY_RUN else '👁 DRY RUN'}")
    print("=" * 70)

    auth, pk = load_credentials()

    # ── Fetch portfolio ────────────────────────────────────────────────────────
    print("\n🔌 Connessione a Trading 212...")
    positions = t212(auth, "GET", "/equity/positions") or []
    pos_map = {}
    for p in positions:
        tk = p.get("instrument", {}).get("ticker") or p.get("ticker", "")
        pos_map[tk] = p
    print(f"✅ {len(pos_map)} posizioni attive")

    # ── Cambi valuta (Polygon) ─────────────────────────────────────────────────
    print("\n📡 Recupero tassi di cambio...")
    eurusd = eur_usd_rate(pk)
    eurgbp = eur_gbp_rate(pk)
    print(f"   EUR/USD = {eurusd:.4f} | EUR/GBP = {eurgbp:.4f}")
    usd_to_eur = 1.0 / eurusd
    gbp_to_eur = 1.0 / eurgbp
    gbx_to_eur = gbp_to_eur / 100.0  # GBp (pence) to EUR

    # ── Calcola prezzi EUR corretti ────────────────────────────────────────────
    print("\n📊 Calcolo prezzi EUR corretti...")

    def get_eur_price_from_portfolio(ticker, currency):
        pos = pos_map.get(ticker)
        if not pos: return 0.0
        qty = float(pos.get("quantity", 0))
        if qty <= 0: return 0.0
        # Usa il valore EUR del portafoglio diviso la quantità
        eur_val = pos.get("walletImpact", {}).get("currentValue")
        if eur_val:
            return float(eur_val) / qty
        # Fallback: currentPrice convertito
        raw_price = float(pos.get("currentPrice", 0))
        if currency == "GBX": return raw_price * gbx_to_eur
        if currency == "GBP": return raw_price * gbp_to_eur
        if currency == "USD": return raw_price * usd_to_eur
        return raw_price  # EUR

    # SWDA (GBX → EUR)
    swda_tk = next((k for k in pos_map if "SWDA" in k), "SWDAl_EQ")
    swda_eur = get_eur_price_from_portfolio(swda_tk, "GBX")
    print(f"   SWDA  ({swda_tk}): €{swda_eur:.4f}/share")

    # EIMI (USD → EUR)
    eimi_tk = next((k for k in pos_map if "EIMI" in k), "EIMIl_EQ")
    eimi_eur = get_eur_price_from_portfolio(eimi_tk, "USD")
    print(f"   EIMI  ({eimi_tk}): €{eimi_eur:.4f}/share")

    # BP ADR (USD → EUR, da Polygon)
    bp_usd = poly_price_usd("BP", pk)
    bp_eur = bp_usd * usd_to_eur
    print(f"   BP    (BP_US_EQ): ${bp_usd:.2f} → €{bp_eur:.4f}/share")

    # SDIV (EUR, Euronext Milano) → cerca nel portfolio o usa Polygon proxy
    # SDIVm_EQ = Global X SuperDividend EUR
    # Proxy Polygon: SDIV (NYSE listed USD version)
    sdiv_pos = pos_map.get("SDIVm_EQ")
    if sdiv_pos:
        qty = float(sdiv_pos.get("quantity", 0))
        eur_val = sdiv_pos.get("walletImpact", {}).get("currentValue")
        sdiv_eur = float(eur_val) / qty if qty > 0 and eur_val else 0.0
    else:
        sdiv_usd = poly_price_usd("SDIV", pk)  # USD version proxy
        sdiv_eur = sdiv_usd * usd_to_eur if sdiv_usd > 0 else 0.0
    print(f"   SDIV  (SDIVm_EQ): €{sdiv_eur:.4f}/share")

    # ── Piano di allocazione ────────────────────────────────────────────────────
    total = NEW_CASH_EUR
    alloc = {
        swda_tk:     {"name": "iShares MSCI World",          "eur": total * 0.55, "price": swda_eur, "min_qty": 0.00823713},
        eimi_tk:     {"name": "iShares MSCI EM IMI",          "eur": total * 0.15, "price": eimi_eur, "min_qty": 0.01},
        "SDIVm_EQ":  {"name": "Global X SuperDividend (EUR)", "eur": total * 0.15, "price": sdiv_eur, "min_qty": 0.01},
        "BP_US_EQ":  {"name": "BP plc ADR",                   "eur": total * 0.15, "price": bp_eur,  "min_qty": 0.01},
    }

    print(f"\n{'═'*70}")
    print(f"  PIANO ACQUISTI — Budget: €{total:.2f}")
    print(f"{'─'*70}")
    print(f"  {'TICKER':<22} {'NOME':<30} {'€':>7}  {'PREZZO':>8}  {'QTÀ':>10}")
    print(f"  {'─'*68}")

    orders = []
    for tk, info in alloc.items():
        price = info["price"]
        budget = info["eur"]
        if price <= 0:
            print(f"  ⚠️  {tk:<22} prezzo non disponibile — saltato")
            continue
        qty_raw = budget / price
        qty = round_qty(qty_raw, 5)
        if qty < info["min_qty"]:
            qty = round_qty(info["min_qty"] * 1.01, 5)  # usa il minimo + margine
        print(f"  {tk:<22} {info['name'][:28]:<30} €{budget:>5.2f}  €{price:>7.4f}  {qty:>10.5f}")
        orders.append({"ticker": tk, "name": info["name"], "qty": qty, "eur": budget})

    print(f"{'═'*70}")

    # ── Esecuzione ────────────────────────────────────────────────────────────
    print(f"\n{'─'*70}")
    print(f"  {'⚡ ESECUZIONE LIVE' if not DRY_RUN else '👁  DRY RUN'}")
    print(f"{'─'*70}")

    for o in orders:
        qty = o["qty"]
        print(f"  📥 {o['ticker']:<22} {qty:.5f} unità  (≈€{o['eur']:.2f})")
        if not DRY_RUN:
            res = t212(auth, "POST", "/equity/orders/market",
                       {"ticker": o["ticker"], "quantity": qty})
            if res:
                order_id = res.get("id", res.get("orderId", "?"))
                status   = res.get("status", res.get("type", "?"))
                print(f"     ✅ Ordine accettato! ID: {order_id} | Stato: {status}")
            else:
                # Prova con quantità arrotondata a 2 decimali
                qty2 = round(qty, 2)
                if qty2 >= 0.01:
                    print(f"     🔄 Retry con qty={qty2:.2f} (2 decimali)...")
                    res2 = t212(auth, "POST", "/equity/orders/market",
                                {"ticker": o["ticker"], "quantity": qty2})
                    if res2:
                        print(f"     ✅ OK con qty={qty2:.2f}!")
                    else:
                        print(f"     ❌ Fallito anche con {qty2:.2f}")
            time.sleep(1.5)
        else:
            print(f"     [DRY RUN]")

    print(f"\n{'═'*70}")
    if DRY_RUN:
        print("  👁  DRY RUN — nessun ordine inviato")
    else:
        print("  ✅ Deploy completato! Controlla Trading 212.")
    print("=" * 70)

if __name__ == "__main__":
    main()
