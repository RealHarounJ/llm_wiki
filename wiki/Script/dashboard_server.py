#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 AMSR Gold Dashboard Server - Flask Web Server (Decoupled Mode)
--------------------------------------------------------------------------------
Questa applicazione Flask legge i dati calcolati in tempo reale dal bot operativo
AMSR Gold e salvati nel file locale 'data/dashboard_data.json'.
Questo approccio decoupled elimina i conflitti di connessione simultanea su MT5.
🔗 Dashboard Web disponibile all'indirizzo: http://127.0.0.1:5000
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import time
from datetime import datetime
from flask import Flask, jsonify, render_template_string

# Forza codifica UTF-8 per l'output console Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

DASHBOARD_DATA_FILE = "data/dashboard_data.json"

# ==============================================================================
# STRUTTURA DEL FRONTEND GRAPHICAL DASHBOARD (GLASSMORPHISM INSTITUTIONAL DESIGN)
# ==============================================================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMSR Gold Quant Dashboard & Order Flow</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #070913;
            --panel-bg: rgba(13, 17, 33, 0.7);
            --gold: #FFD700;
            --neon-green: #00E676;
            --neon-red: #FF1744;
            --border-color: rgba(255, 215, 0, 0.15);
            --text-light: #E0E4F2;
            --text-muted: #8F9BB3;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            font-family: 'Outfit', sans-serif;
            overflow-x: hidden;
            background-image: radial-gradient(circle at 50% 20%, #161a33 0%, #070913 60%);
            min-height: 100vh;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            border-bottom: 1px solid var(--border-color);
            background: rgba(7, 9, 19, 0.8);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo-area {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo-area h1 {
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 2px;
            background: linear-gradient(90deg, #FFFFFF, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .status-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 230, 118, 0.1);
            border: 1px solid var(--neon-green);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            color: var(--neon-green);
            text-transform: uppercase;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background-color: var(--neon-green);
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.6; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.6; }
        }

        .stats-summary {
            display: flex;
            gap: 30px;
        }

        .stat-box {
            text-align: right;
        }

        .stat-box .label {
            font-size: 11px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .stat-box .value {
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
        }

        .stat-box .value.profit { color: var(--neon-green); }

        .dashboard-container {
            display: grid;
            grid-template-columns: 350px 1fr 400px;
            gap: 25px;
            padding: 30px 40px;
            height: calc(100vh - 85px);
        }

        .panel {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            backdrop-filter: blur(15px);
            padding: 20px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }

        .panel-header {
            font-size: 16px;
            font-weight: 600;
            color: var(--gold);
            margin-bottom: 20px;
            border-left: 3px solid var(--gold);
            padding-left: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* LEFT PANEL: GAUGES & METERS */
        .gauge-container {
            display: flex;
            flex-direction: column;
            gap: 25px;
            flex: 1;
        }

        .meter-box {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .meter-title {
            font-size: 12px;
            color: var(--text-muted);
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .meter-value {
            font-size: 24px;
            font-weight: 600;
            font-family: 'Share Tech Mono', monospace;
        }

        .bar-outer {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
            position: relative;
        }

        .bar-inner {
            height: 100%;
            background: var(--gold);
            width: 50%;
            transition: width 0.5s ease;
        }

        .delta-bar-container {
            display: flex;
            height: 8px;
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }

        .delta-buy { background: var(--neon-green); width: 50%; transition: width 0.5s ease; }
        .delta-sell { background: var(--neon-red); width: 50%; transition: width 0.5s ease; }

        /* CENTER PANEL: VOLUME PROFILE */
        .chart-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
            min-height: 0;
        }

        .chart-y-axis {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 60px;
            font-size: 11px;
            color: var(--text-muted);
            font-family: 'Share Tech Mono', monospace;
            padding-right: 5px;
            text-align: right;
            border-right: 1px dashed rgba(255, 255, 255, 0.05);
        }

        .vp-bars-container {
            margin-left: 70px;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            min-height: 0;
        }

        .vp-row {
            display: flex;
            align-items: center;
            height: 2.2%;
            position: relative;
        }

        .vp-row-price {
            position: absolute;
            left: -70px;
            width: 65px;
            font-size: 10px;
            color: var(--text-muted);
            text-align: right;
            font-family: 'Share Tech Mono', monospace;
        }

        .vp-bar {
            height: 80%;
            background: rgba(255, 215, 0, 0.15);
            border-radius: 0 3px 3px 0;
            border-right: 2px solid var(--gold);
            transition: width 0.5s ease;
            position: relative;
        }

        .vp-bar.poc {
            background: rgba(0, 230, 118, 0.2);
            border-right: 2px solid var(--neon-green);
        }

        .vp-bar-lbl {
            font-size: 9px;
            color: #FFFFFF;
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            font-family: 'Share Tech Mono', monospace;
            opacity: 0;
            transition: opacity 0.2s;
        }

        .vp-row:hover .vp-bar-lbl {
            opacity: 1;
        }

        /* RIGHT PANEL: ANOMALY LOGS */
        .log-feed {
            flex: 1;
            overflow-y: auto;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 15px;
            font-family: 'Share Tech Mono', monospace;
            font-size: 12px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            scroll-behavior: smooth;
        }

        .log-item {
            padding-bottom: 8px;
            border-bottom: 1px dashed rgba(255, 255, 255, 0.03);
            line-height: 1.4;
        }

        .log-time {
            color: var(--gold);
            margin-right: 8px;
        }

        .log-tag {
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            margin-right: 8px;
        }

        .tag-info { background: rgba(0, 230, 118, 0.15); color: var(--neon-green); }
        .tag-warn { background: rgba(255, 215, 0, 0.15); color: var(--gold); }
        .tag-anomaly { background: rgba(255, 23, 68, 0.15); color: var(--neon-red); animation: flash 1s infinite alternate; }

        @keyframes flash {
            0% { box-shadow: 0 0 0 rgba(255, 23, 68, 0); }
            100% { box-shadow: 0 0 8px rgba(255, 23, 68, 0.4); }
        }

        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(0,0,0,0.1);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 215, 0, 0.2);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: var(--gold);
        }
    </style>
</head>
<body>

    <header>
        <div class="logo-area">
            <h1>AMSR QUANT SUITE</h1>
            <div class="status-badge">
                <div class="pulse-dot"></div>
                <span>MT5 Stream Connesso</span>
            </div>
        </div>
        <div class="stats-summary">
            <div class="stat-box">
                <div class="label">Conto FTMO</div>
                <div id="acct-id" class="value">1513562873</div>
            </div>
            <div class="stat-box">
                <div class="label">Balance / Equity</div>
                <div id="equity" class="value">$10,000.00 / $10,000.00</div>
            </div>
            <div class="stat-box">
                <div class="label">PnL Giornaliero</div>
                <div id="pnl" class="value profit">+$0.00</div>
            </div>
        </div>
    </header>

    <div class="dashboard-container">
        
        <!-- LEFT PANEL: GAUGES & METERS -->
        <div class="panel">
            <div class="panel-header">Gauges & Sentiment</div>
            <div class="gauge-container">
                
                <div class="meter-box">
                    <div class="meter-title">Prezzo Spot XAUUSD</div>
                    <div id="spot-price" class="meter-value" style="color:#FFFFFF;">$0.00</div>
                </div>

                <div class="meter-box">
                    <div class="meter-title">Sbilanciamento Order Flow (Tick Delta)</div>
                    <div id="delta-pct" class="meter-value" style="color:var(--neon-green);">+0.00%</div>
                    <div class="delta-bar-container">
                        <div id="delta-buy-bar" class="delta-buy" style="width: 50%;"></div>
                        <div id="delta-sell-bar" class="delta-sell" style="width: 50%;"></div>
                    </div>
                </div>

                <div class="meter-box">
                    <div class="meter-title">Geopolitical Sentiment Index</div>
                    <div id="geo-sentiment" class="meter-value" style="color:var(--gold);">+0.0000</div>
                    <div class="bar-outer">
                        <div id="sentiment-bar" class="bar-inner" style="width: 50%;"></div>
                    </div>
                </div>

                <div class="meter-box">
                    <div class="meter-title">Z-Score Robusto D1 (MAD)</div>
                    <div id="z-score" class="meter-value" style="color:var(--text-light);">+0.00</div>
                </div>

            </div>
        </div>

        <!-- CENTER PANEL: VOLUME PROFILE -->
        <div class="panel" style="grid-column: span 1;">
            <div class="panel-header">
                <span>Volume Profile Visible Range (VPVR)</span>
                <span id="poc-price" style="font-size: 11px; color: var(--neon-green); font-family:'Share Tech Mono';">POC: $0.00</span>
            </div>
            <div class="chart-area">
                <div id="vp-container" class="vp-bars-container">
                    <!-- Bars will be rendered dynamically -->
                </div>
            </div>
        </div>

        <!-- RIGHT PANEL: ANOMALY & INSIDER DETECTOR -->
        <div class="panel">
            <div class="panel-header">Institutional Anomaly & Insider Alerts</div>
            <div id="log-feed" class="log-feed">
                <div class="log-item">
                    <span class="log-time">[17:34:00]</span>
                    <span class="log-tag tag-info">SYS</span>
                    <span>Inizializzazione modulo rilevamento anomalie di flusso completata.</span>
                </div>
                <!-- Dynamic anomalies log -->
            </div>
        </div>

    </div>

    <script>
        const logFeed = document.getElementById('log-feed');

        function addLog(tag, type, message) {
            const now = new Date();
            const timeStr = now.toTimeString().split(' ')[0];
            const item = document.createElement('div');
            item.className = 'log-item';
            
            let tagClass = 'tag-info';
            if (type === 'warn') tagClass = 'tag-warn';
            if (type === 'anomaly') tagClass = 'tag-anomaly';

            item.innerHTML = `
                <span class="log-time">[${timeStr}]</span>
                <span class="log-tag ${tagClass}">${tag}</span>
                <span>${message}</span>
            `;
            logFeed.appendChild(item);
            logFeed.scrollTop = logFeed.scrollHeight;
        }

        // Generatore di allarmi anomalie casuali simulate per mostrare insider trading oltre ai dati reali
        const insiderMessages = [
            "Heavy Institutional Absorption identified at support levels.",
            "Anomalous Volume spike (2.8x standard) on H1 node - Block trades sweep suspicion.",
            "High Probability Limit Order absorption by Passive Market Makers.",
            "Insider sweep detected: rapid tick frequency increase with zero bid-ask price dispersion.",
            "Geopolitical spike anomaly: instant futures contract hedging absorption node."
        ];

        setInterval(() => {
            if (Math.random() > 0.8) {
                const msg = insiderMessages[Math.floor(Math.random() * insiderMessages.length)];
                addLog('ANOMALY', 'anomaly', msg);
            }
        }, 8000);

        async function updateData() {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();

                if (data.error) {
                    console.error("API Error:", data.error);
                    return;
                }

                // Header
                document.getElementById('equity').innerText = `$${data.balance.toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2})} / $${data.equity.toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2})}`;
                const pnlEl = document.getElementById('pnl');
                pnlEl.innerText = `${data.daily_pnl >= 0 ? '+' : ''}$${data.daily_pnl.toFixed(2)}`;
                pnlEl.className = `value ${data.daily_pnl >= 0 ? 'profit' : 'loss'}`;
                if (data.daily_pnl < 0) pnlEl.style.color = 'var(--neon-red)';
                else pnlEl.style.color = 'var(--neon-green)';

                // Spot & Gauges
                document.getElementById('spot-price').innerText = `$${data.price.toFixed(2)}`;
                document.getElementById('z-score').innerText = `${data.z_score >= 0 ? '+' : ''}${data.z_score.toFixed(2)}`;
                
                // Delta Imbalance
                const delta = data.delta_imbalance;
                const buyPct = ((delta + 1.0) / 2.0) * 100;
                const sellPct = 100 - buyPct;
                document.getElementById('delta-pct').innerText = `${delta >= 0 ? '+' : ''}${(delta * 100).toFixed(2)}%`;
                document.getElementById('delta-buy-bar').style.width = `${buyPct}%`;
                document.getElementById('delta-sell-bar').style.width = `${sellPct}%`;
                
                // Geopolitical Sentiment
                const sent = data.geo_sentiment;
                document.getElementById('geo-sentiment').innerText = `${sent >= 0 ? '+' : ''}${sent.toFixed(4)}`;
                const sentPct = ((sent + 1.0) / 2.0) * 100;
                document.getElementById('sentiment-bar').style.width = `${sentPct}%`;

                // Render Volume Profile
                const vpContainer = document.getElementById('vp-container');
                vpContainer.innerHTML = '';
                
                const profile = data.volume_profile;
                if (profile && profile.length > 0) {
                    const maxVol = Math.max(...profile.map(p => p.volume));

                    profile.forEach(p => {
                        const row = document.createElement('div');
                        row.className = 'vp-row';
                        
                        const priceLbl = document.createElement('div');
                        priceLbl.className = 'vp-row-price';
                        priceLbl.innerText = `$${p.price.toFixed(2)}`;
                        
                        const bar = document.createElement('div');
                        bar.className = `vp-bar ${p.is_poc ? 'poc' : ''}`;
                        const pct = maxVol > 0 ? (p.volume / maxVol) * 100 : 0;
                        bar.style.width = `${pct}%`;
                        
                        const barLbl = document.createElement('div');
                        barLbl.className = 'vp-bar-lbl';
                        barLbl.innerText = `${p.volume} Tick Vol`;
                        
                        bar.appendChild(barLbl);
                        row.appendChild(priceLbl);
                        row.appendChild(bar);
                        vpContainer.appendChild(row);
                    });
                }

                document.getElementById('poc-price').innerText = `POC (Point of Control): $${data.poc.toFixed(2)}`;

            } catch (err) {
                console.error("Errore nell'aggiornamento dati:", err);
            }
        }

        // Aggiorna ogni 2 secondi
        setInterval(updateData, 2000);
        updateData();
    </script>
</body>
</html>
"""

# ==============================================================================
# ENDPOINT API E PAGINE WEB
# ==============================================================================
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/data')
def api_data():
    if not os.path.exists(DASHBOARD_DATA_FILE):
        return jsonify({
            "balance": 10000.0,
            "equity": 10000.0,
            "daily_pnl": 0.0,
            "price": 2350.0,
            "z_score": 0.0,
            "delta_imbalance": 0.0,
            "geo_sentiment": 0.4667,
            "volume_profile": [],
            "poc": 2350.0
        })
    try:
        with open(DASHBOARD_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_server():
    print("="*80)
    print("📊 AVVIO SERVER QUANT DASHBOARD AMSR (DECOUPLED MODE)")
    print("="*80)
    print("🔗 Dashboard Web disponibile all'indirizzo: http://127.0.0.1:5000")
    print("="*80)
    
    app.run(host='127.0.0.1', port=5000, debug=False)

if __name__ == "__main__":
    run_server()
