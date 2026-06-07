#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 AMSR AI PWA Control Dashboard Server - Flask Web Server (Decoupled & Control Mode)
--------------------------------------------------------------------------------
Questa applicazione Flask gestisce la dashboard e l'interfaccia di controllo
del bot trading AMSR AI Brain v4. È configurata come Progressive Web App (PWA)
per poter essere scaricata e installata sia su telefono che su computer.

🔗 Dashboard Web: http://127.0.0.1:5000 (o tramite IP locale della LAN)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import socket
from datetime import datetime
from flask import Flask, jsonify, request, render_template_string, make_response, send_from_directory

# Forza codifica UTF-8 per l'output console Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Risolve l'IP locale per permettere all'utente di connettersi da telefono
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Non è necessario che sia raggiungibile
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

# Configura cartella statica
base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, 'static')
app = Flask(__name__, static_folder=static_dir)

DASHBOARD_DATA_FILE = "data/dashboard_data.json"
CONTROL_FILE = "data/bot_control.json"

# ==============================================================================
# STRUTTURA DEL FRONTEND (GLASSMORPHISM CYBERPUNK INSTITUTIONAL PWA DESIGN)
# ==============================================================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AMSR Quant Suite & Control</title>
    
    <!-- Meta tag per PWA & iOS Mobile -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#FFD700">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="AMSR Quant">
    <link rel="apple-touch-icon" href="/static/icon-192.png">
    
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;800&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-dark: #050714;
            --panel-bg: rgba(16, 20, 38, 0.55);
            --gold: #FFD700;
            --gold-glow: rgba(255, 215, 0, 0.35);
            --neon-green: #00E676;
            --neon-green-glow: rgba(0, 230, 118, 0.25);
            --neon-red: #FF1744;
            --neon-red-glow: rgba(255, 23, 68, 0.25);
            --neon-blue: #00B0FF;
            --border-color: rgba(255, 215, 0, 0.1);
            --text-light: #E2E6F3;
            --text-muted: #8F9BB3;
            --panel-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            font-family: 'Outfit', sans-serif;
            min-height: 100vh;
            background-image: radial-gradient(circle at 50% 10%, #151a35 0%, var(--bg-dark) 70%);
            padding-bottom: 40px;
        }

        /* HEADER */
        header {
            display: flex;
            flex-direction: column;
            gap: 15px;
            padding: 20px;
            background: rgba(7, 9, 21, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        @media(min-width: 768px) {
            header {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
                padding: 20px 40px;
            }
        }

        .logo-area {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
        }

        .logo-area h1 {
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 1.5px;
            background: linear-gradient(90deg, #FFFFFF, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .connection-status {
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 230, 118, 0.08);
            border: 1px solid var(--neon-green);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            color: var(--neon-green);
            text-transform: uppercase;
        }

        .connection-status.offline {
            background: rgba(255, 23, 68, 0.08);
            border-color: var(--neon-red);
            color: var(--neon-red);
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            background-color: var(--neon-green);
            border-radius: 50%;
            animation: pulse 1.6s infinite;
        }

        .connection-status.offline .pulse-dot {
            background-color: var(--neon-red);
        }

        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.5; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.5; }
        }

        .metrics-summary {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        @media(min-width: 768px) {
            .metrics-summary {
                display: flex;
                gap: 30px;
            }
        }

        .metric-box {
            text-align: left;
        }

        @media(min-width: 768px) {
            .metric-box {
                text-align: right;
            }
        }

        .metric-box .lbl {
            font-size: 10px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 2px;
        }

        .metric-box .val {
            font-size: 16px;
            font-weight: 600;
            color: #FFFFFF;
            font-family: 'Share Tech Mono', monospace;
        }

        .metric-box .val.profit { color: var(--neon-green); text-shadow: 0 0 10px var(--neon-green-glow); }
        .metric-box .val.loss { color: var(--neon-red); text-shadow: 0 0 10px var(--neon-red-glow); }

        /* MAIN CONTAINER */
        .container {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 25px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .layout-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 25px;
        }

        @media(min-width: 1024px) {
            .layout-grid {
                grid-template-columns: 380px 1fr;
            }
        }

        /* CARDS / PANELS */
        .glass-panel {
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            padding: 20px;
            box-shadow: var(--panel-shadow);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        .glass-panel-header {
            font-size: 15px;
            font-weight: 600;
            color: var(--gold);
            margin-bottom: 18px;
            border-left: 3px solid var(--gold);
            padding-left: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* CONTROLS CARD */
        .control-group {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .control-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.02);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }

        .control-info {
            display: flex;
            flex-direction: column;
            gap: 3px;
        }

        .control-label {
            font-size: 14px;
            font-weight: 500;
            color: #FFFFFF;
        }

        .control-desc {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* TOGGLE SWITCH */
        .switch {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 26px;
        }

        .switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #2c324e;
            transition: .3s;
            border-radius: 34px;
        }

        .slider:before {
            position: absolute;
            content: "";
            height: 20px;
            width: 20px;
            left: 3px;
            bottom: 3px;
            background-color: white;
            transition: .3s;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: var(--neon-green);
            box-shadow: 0 0 8px var(--neon-green-glow);
        }

        input:checked + .slider:before {
            transform: translateX(24px);
        }

        /* EMERGENCY STOP BUTTON */
        .btn-emergency {
            background: linear-gradient(135deg, #d32f2f, #ff1744);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px;
            font-size: 15px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(255, 23, 68, 0.35);
            transition: all 0.2s ease;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
        }

        .btn-emergency:active {
            transform: scale(0.97);
            box-shadow: 0 2px 5px rgba(255, 23, 68, 0.2);
        }

        /* SLIDER / INPUTS */
        .parameter-block {
            display: flex;
            flex-direction: column;
            gap: 12px;
            background: rgba(255, 255, 255, 0.02);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }

        .parameter-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .parameter-val {
            font-family: 'Share Tech Mono', monospace;
            font-size: 14px;
            color: var(--gold);
            font-weight: 600;
        }

        .range-slider {
            width: 100%;
            height: 6px;
            background: #2c324e;
            border-radius: 3px;
            outline: none;
            -webkit-appearance: none;
        }

        .range-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--gold);
            cursor: pointer;
            box-shadow: 0 0 5px var(--gold-glow);
        }

        .input-number {
            background: #14172a;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            color: #FFFFFF;
            padding: 8px;
            font-family: 'Share Tech Mono', monospace;
            font-size: 14px;
            width: 100px;
            text-align: center;
        }

        .btn-save {
            background: rgba(255, 215, 0, 0.12);
            border: 1px solid var(--gold);
            color: var(--gold);
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            text-transform: uppercase;
            transition: all 0.2s;
        }

        .btn-save:hover {
            background: var(--gold);
            color: var(--bg-dark);
            box-shadow: 0 0 10px var(--gold-glow);
        }

        /* ACTIVE POSITIONS */
        .positions-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .no-positions {
            text-align: center;
            color: var(--text-muted);
            font-size: 13px;
            padding: 30px 10px;
            border: 1px dashed rgba(255, 255, 255, 0.08);
            border-radius: 10px;
        }

        .position-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 12px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            position: relative;
        }

        .pos-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .pos-title {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .pos-symbol {
            font-weight: 800;
            font-size: 16px;
            color: #FFFFFF;
        }

        .pos-badge {
            font-size: 10px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 4px;
            text-transform: uppercase;
        }

        .pos-badge.buy { background: rgba(0, 230, 118, 0.15); color: var(--neon-green); }
        .pos-badge.sell { background: rgba(255, 23, 68, 0.15); color: var(--neon-red); }

        .pos-pnl {
            font-family: 'Share Tech Mono', monospace;
            font-size: 16px;
            font-weight: 800;
        }

        .pos-pnl.profit { color: var(--neon-green); }
        .pos-pnl.loss { color: var(--neon-red); }

        .pos-details {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            background: rgba(0, 0, 0, 0.15);
            padding: 10px;
            border-radius: 6px;
        }

        .pos-det-item {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .pos-det-lbl {
            font-size: 8px;
            color: var(--text-muted);
            text-transform: uppercase;
        }

        .pos-det-val {
            font-family: 'Share Tech Mono', monospace;
            font-size: 11px;
            color: #E2E6F3;
        }

        .btn-close-trade {
            background: rgba(255, 23, 68, 0.1);
            border: 1px solid var(--neon-red);
            color: var(--neon-red);
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            text-transform: uppercase;
            align-self: flex-end;
            transition: all 0.2s;
        }

        .btn-close-trade:hover {
            background: var(--neon-red);
            color: white;
            box-shadow: 0 0 8px var(--neon-red-glow);
        }

        /* WATCHLIST GRID */
        .watchlist-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 15px;
        }

        .asset-card {
            background: rgba(255, 255, 255, 0.015);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 10px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            transition: all 0.3s ease;
        }

        .asset-card.highlight {
            border-color: var(--gold);
            box-shadow: 0 0 12px rgba(255, 215, 0, 0.15);
            background: rgba(255, 215, 0, 0.02);
            animation: borderGlow 2s infinite alternate;
        }

        @keyframes borderGlow {
            0% { border-color: rgba(255, 215, 0, 0.4); }
            100% { border-color: rgba(255, 215, 0, 0.9); }
        }

        .asset-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .asset-name {
            font-weight: 700;
            font-size: 13px;
            color: #FFFFFF;
        }

        .asset-regime {
            font-size: 8px;
            font-weight: 800;
            padding: 1px 4px;
            border-radius: 3px;
            text-transform: uppercase;
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-muted);
        }

        .regime-trending { background: rgba(0, 176, 255, 0.15) !important; color: var(--neon-blue) !important; }
        .regime-ranging { background: rgba(255, 215, 0, 0.15) !important; color: var(--gold) !important; }
        .regime-volatile { background: rgba(255, 23, 68, 0.15) !important; color: var(--neon-red) !important; }
        .regime-breakout { background: rgba(0, 230, 118, 0.15) !important; color: var(--neon-green) !important; }

        .asset-price {
            font-family: 'Share Tech Mono', monospace;
            font-size: 14px;
            font-weight: 600;
            color: #FFFFFF;
        }

        .confluence-label {
            font-size: 8px;
            font-weight: 800;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            animation: flashText 1s infinite alternate;
        }

        @keyframes flashText {
            0% { opacity: 0.4; }
            100% { opacity: 1; }
        }

        .asset-scores {
            display: flex;
            flex-direction: column;
            gap: 4px;
            margin-top: 4px;
        }

        .score-bar-lbl {
            display: flex;
            justify-content: space-between;
            font-size: 9px;
            color: var(--text-muted);
        }

        .score-bar-outer {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 2px;
            overflow: hidden;
        }

        .score-bar-inner {
            height: 100%;
            border-radius: 2px;
        }

        .score-bar-inner.buy { background: var(--neon-green); }
        .score-bar-inner.sell { background: var(--neon-red); }

        /* LOG FEED */
        .log-feed {
            height: 180px;
            overflow-y: auto;
            background: rgba(0, 0, 0, 0.25);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.04);
            padding: 12px;
            font-family: 'Share Tech Mono', monospace;
            font-size: 11px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            scroll-behavior: smooth;
        }

        .log-line {
            line-height: 1.3;
            border-bottom: 1px dashed rgba(255, 255, 255, 0.02);
            padding-bottom: 4px;
        }

        .log-time { color: var(--gold); margin-right: 5px; }
        .log-type {
            padding: 1px 4px;
            border-radius: 2px;
            font-size: 9px;
            font-weight: 800;
            text-transform: uppercase;
            margin-right: 5px;
        }

        .lt-info { background: rgba(0, 176, 255, 0.15); color: var(--neon-blue); }
        .lt-alert { background: rgba(255, 23, 68, 0.15); color: var(--neon-red); }
        .lt-action { background: rgba(0, 230, 118, 0.15); color: var(--neon-green); }

        /* INSTALL BANNER */
        .install-guide {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.05) 0%, rgba(0, 176, 255, 0.05) 100%);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            box-shadow: var(--panel-shadow);
        }

        .install-guide-title {
            font-size: 14px;
            font-weight: 600;
            color: var(--gold);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .install-steps {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }

        @media(min-width: 768px) {
            .install-steps {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        .step-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 10px;
            padding: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .step-icon {
            font-size: 20px;
        }

        .step-text {
            font-size: 11px;
            line-height: 1.4;
            color: var(--text-light);
        }

        .step-text strong {
            color: var(--gold);
        }

        /* CUSTOM TOAST NOTIFICATION */
        .toast {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: rgba(16, 20, 38, 0.95);
            border: 1px solid var(--gold);
            color: #FFFFFF;
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 500;
            box-shadow: 0 5px 20px rgba(0,0,0,0.5);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
        }
    </style>
</head>
<body>

    <!-- HEADER -->
    <header>
        <div class="logo-area">
            <h1>AMSR QUANT SUITE</h1>
            <div id="status-badge" class="connection-status">
                <div class="pulse-dot"></div>
                <span id="status-text">Stream Connesso</span>
            </div>
        </div>
        
        <div class="metrics-summary">
            <div class="metric-box">
                <div class="lbl">Conto FTMO Challenge</div>
                <div class="val">1513562873 (Demo)</div>
            </div>
            <div class="metric-box">
                <div class="lbl">Balance / Equity</div>
                <div id="equity" class="val">$10,000.00 / $10,000.00</div>
            </div>
            <div class="metric-box">
                <div class="lbl">Daily PnL</div>
                <div id="pnl" class="val profit">+$0.00</div>
            </div>
            <div class="metric-box">
                <div class="lbl">Operazioni Aperte</div>
                <div id="trades-count" class="val">0</div>
            </div>
        </div>
    </header>

    <!-- CONTENT -->
    <div class="container">
        
        <div class="layout-grid">
            
            <!-- LEFT PANEL: CONTROLS & METERS -->
            <div class="glass-panel" style="gap: 20px;">
                <div class="glass-panel-header">PANNELLO DI CONTROLLO</div>
                
                <div class="control-group">
                    
                    <!-- MASTER SWITCH -->
                    <div class="control-row">
                        <div class="control-info">
                            <span class="control-label">Master Trading</span>
                            <span class="control-desc">Abilita o disabilita il trigger automatico</span>
                        </div>
                        <label class="switch">
                            <input type="checkbox" id="master-switch" onchange="toggleTrading()">
                            <span class="slider"></span>
                        </label>
                    </div>

                    <!-- EMERGENCY STOP -->
                    <button class="btn-emergency" onclick="triggerEmergencyStop()">
                        ⚠️ EMERGENCY STOP (CLOSE ALL)
                    </button>

                    <!-- CONFLUENCE THRESHOLD SLIDER -->
                    <div class="parameter-block">
                        <div class="parameter-header">
                            <span class="control-label" style="font-size:13px;">Confluence Threshold</span>
                            <span id="threshold-val" class="parameter-val">75%</span>
                        </div>
                        <input type="range" id="threshold-slider" class="range-slider" min="50" max="95" value="75" oninput="updateSliderVal(this.value)">
                        <button class="btn-save" onclick="saveParameters()">Salva Parametri</button>
                    </div>

                    <!-- RISK LIMIT FIELD -->
                    <div class="parameter-block">
                        <div class="parameter-header">
                            <span class="control-label" style="font-size:13px;">Rischio per Operazione ($)</span>
                            <input type="number" id="risk-input" class="input-number" min="5" max="200" value="40">
                        </div>
                        <button class="btn-save" onclick="saveParameters()">Salva Rischio</button>
                    </div>

                </div>
            </div>

            <!-- RIGHT PANEL: ACTIVE TRADES & WATCHLIST -->
            <div style="display: flex; flex-direction: column; gap: 25px;">
                
                <!-- ACTIVE TRADES -->
                <div class="glass-panel">
                    <div class="glass-panel-header">POSIZIONI ATTIVE (MT5)</div>
                    <div id="positions-container" class="positions-container">
                        <div class="no-positions">Nessuna posizione attiva a mercato.</div>
                    </div>
                </div>

                <!-- WATCHLIST GRID -->
                <div class="glass-panel">
                    <div class="glass-panel-header">WATCHLIST DI CONFLUENZA (19 ASSETS)</div>
                    <div id="watchlist-grid" class="watchlist-grid">
                        <!-- Generato dinamicamente -->
                    </div>
                </div>

                <!-- ANOMALY FEED -->
                <div class="glass-panel">
                    <div class="glass-panel-header">SYSTEM EVENTS & ALERTS LOG</div>
                    <div id="log-feed" class="log-feed">
                        <div class="log-line">
                            <span class="log-time">18:30:00</span>
                            <span class="log-type lt-info">SYS</span>
                            <span>Inizializzazione interfaccia di monitoraggio completata.</span>
                        </div>
                    </div>
                </div>

                <!-- INSTALL GUIDE PWA -->
                <div class="install-guide">
                    <div class="install-guide-title">
                        <span>📲 SCARICA L'APP SUL TELEFONO</span>
                    </div>
                    <div class="install-steps">
                        <div class="step-card">
                            <span class="step-icon">🤖</span>
                            <span class="step-text">Su <strong>Android / Chrome</strong>: Premi il tasto menu (tre punti) e seleziona <strong>"Installa applicazione"</strong>.</span>
                        </div>
                        <div class="step-card">
                            <span class="step-icon">🍎</span>
                            <span class="step-text">Su <strong>iOS / Safari</strong>: Premi l'icona Condividi (quadrato con freccia) e seleziona <strong>"Aggiungi alla schermata Home"</strong>.</span>
                        </div>
                        <div class="step-card">
                            <span class="step-icon">💻</span>
                            <span class="step-text">Su <strong>Desktop / Chrome</strong>: Clicca sull'icona di installazione "+" presente a destra della barra degli indirizzi.</span>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- TOAST NOTIFICATION -->
    <div id="toast" class="toast">
        <span id="toast-icon">ℹ️</span>
        <span id="toast-msg">Notifica di sistema</span>
    </div>

    <!-- CLIENT SCRIPT -->
    <script>
        // Registrazione del Service Worker per supporto PWA (Download su Homescreen)
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/service-worker.js')
                    .then(reg => console.log('Service Worker registrato con successo:', reg.scope))
                    .catch(err => console.error('Errore registrazione Service Worker:', err));
            });
        }

        const toast = document.getElementById('toast');
        const toastMsg = document.getElementById('toast-msg');
        const toastIcon = document.getElementById('toast-icon');

        function showToast(msg, type = 'info') {
            toastMsg.innerText = msg;
            if (type === 'success') {
                toastIcon.innerText = '✅';
                toast.style.borderColor = 'var(--neon-green)';
            } else if (type === 'error') {
                toastIcon.innerText = '❌';
                toast.style.borderColor = 'var(--neon-red)';
            } else {
                toastIcon.innerText = 'ℹ️';
                toast.style.borderColor = 'var(--gold)';
            }
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }

        function addLog(type, typeLabel, msg) {
            const logFeed = document.getElementById('log-feed');
            const now = new Date();
            const timeStr = now.toTimeString().split(' ')[0];
            const line = document.createElement('div');
            line.className = 'log-line';
            line.innerHTML = `
                <span class="log-time">${timeStr}</span>
                <span class="log-type ${type}">${typeLabel}</span>
                <span>${msg}</span>
            `;
            logFeed.appendChild(line);
            logFeed.scrollTop = logFeed.scrollHeight;
        }

        function updateSliderVal(val) {
            document.getElementById('threshold-val').innerText = val + '%';
        }

        // Variabile globale per tracciare lo stato dei parametri ed evitare sovrascritture durante la digitazione
        let inputsFocused = false;
        
        document.getElementById('threshold-slider').addEventListener('focus', () => { inputsFocused = true; });
        document.getElementById('threshold-slider').addEventListener('blur', () => { inputsFocused = false; });
        document.getElementById('risk-input').addEventListener('focus', () => { inputsFocused = true; });
        document.getElementById('risk-input').addEventListener('blur', () => { inputsFocused = false; });

        async function updateDashboard() {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();

                if (data.error) {
                    document.getElementById('status-badge').className = 'connection-status offline';
                    document.getElementById('status-text').innerText = 'Errore API';
                    return;
                }

                document.getElementById('status-badge').className = 'connection-status';
                document.getElementById('status-text').innerText = 'Stream Connesso';

                // Update Header
                const pnl = data.daily_pnl;
                const pnlEl = document.getElementById('pnl');
                pnlEl.innerText = `${pnl >= 0 ? '+' : ''}$${pnl.toFixed(2)}`;
                pnlEl.className = `val ${pnl >= 0 ? 'profit' : 'loss'}`;
                
                document.getElementById('equity').innerText = `$${data.balance.toLocaleString('en-US', {minimumFractionDigits:2})} / $${data.equity.toLocaleString('en-US', {minimumFractionDigits:2})}`;
                
                const activeCount = data.active_positions ? data.active_positions.length : 0;
                document.getElementById('trades-count').innerText = activeCount;

                // Sync Controls (solo se l'utente non ci sta interagendo)
                if (!inputsFocused) {
                    document.getElementById('master-switch').checked = data.trading_enabled;
                    document.getElementById('threshold-slider').value = data.confluence_threshold;
                    document.getElementById('threshold-val').innerText = data.confluence_threshold + '%';
                    document.getElementById('risk-input').value = data.portfolio_risk_limit_usd;
                }

                // Render Active Positions
                const posContainer = document.getElementById('positions-container');
                posContainer.innerHTML = '';
                
                if (data.active_positions && data.active_positions.length > 0) {
                    data.active_positions.forEach(pos => {
                        const card = document.createElement('div');
                        card.className = 'position-card';
                        
                        const pnlVal = pos.pnl;
                        const pnlClass = pnlVal >= 0 ? 'profit' : 'loss';
                        
                        card.innerHTML = `
                            <div class="pos-header">
                                <div class="pos-title">
                                    <span class="pos-symbol">${pos.symbol}</span>
                                    <span class="pos-badge ${pos.type.toLowerCase()}">${pos.type}</span>
                                </div>
                                <span class="pos-pnl ${pnlClass}">${pnlVal >= 0 ? '+' : ''}$${pnlVal.toFixed(2)}</span>
                            </div>
                            <div class="pos-details">
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Lotti</span>
                                    <span class="pos-det-val">${pos.volume.toFixed(2)}</span>
                                </div>
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Prezzo Apertura</span>
                                    <span class="pos-det-val">${pos.open_price.toFixed(5)}</span>
                                </div>
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Prezzo Corrente</span>
                                    <span class="pos-det-val">${pos.current_price.toFixed(5)}</span>
                                </div>
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Stop Loss</span>
                                    <span class="pos-det-val">${pos.sl > 0 ? pos.sl.toFixed(5) : 'N/A'}</span>
                                </div>
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Take Profit</span>
                                    <span class="pos-det-val">${pos.tp > 0 ? pos.tp.toFixed(5) : 'N/A'}</span>
                                </div>
                                <div class="pos-det-item">
                                    <span class="pos-det-lbl">Ticket ID</span>
                                    <span class="pos-det-val">${pos.ticket}</span>
                                </div>
                            </div>
                            <button class="btn-close-trade" onclick="closePosition(${pos.ticket}, '${pos.symbol}')">Chiudi Operazione</button>
                        `;
                        posContainer.appendChild(card);
                    });
                } else {
                    posContainer.innerHTML = '<div class="no-positions">Nessuna posizione attiva a mercato.</div>';
                }

                // Render Watchlist
                const wlGrid = document.getElementById('watchlist-grid');
                wlGrid.innerHTML = '';
                
                const watchlist = data.watchlist;
                const threshold = data.confluence_threshold;
                
                if (watchlist && Object.keys(watchlist).length > 0) {
                    Object.keys(watchlist).forEach(sym => {
                        const item = watchlist[sym];
                        const maxScore = Math.max(item.buy_score, item.sell_score);
                        const isHighConfluence = maxScore >= threshold;
                        
                        const card = document.createElement('div');
                        card.className = `asset-card ${isHighConfluence ? 'highlight' : ''}`;
                        
                        let regimeClass = 'regime-ranging';
                        if (item.regime === 'TRENDING') regimeClass = 'regime-trending';
                        if (item.regime === 'VOLATILE') regimeClass = 'regime-volatile';
                        if (item.regime === 'BREAKOUT') regimeClass = 'regime-breakout';
                        
                        let signalTag = '';
                        if (isHighConfluence) {
                            signalTag = `<span class="confluence-label">⚡ SEGNALE ATTIVO (${maxScore.toFixed(0)}%)</span>`;
                        }

                        // Trova la predizione ML in testo
                        let mlText = 'HOLD';
                        if (item.ml_pred > 0) mlText = 'BUY';
                        if (item.ml_pred < 0) mlText = 'SELL';
                        const mlProb = (Math.max(...item.ml_probs) * 100).toFixed(0);

                        card.innerHTML = `
                            <div class="asset-header">
                                <span class="asset-name">${sym}</span>
                                <span class="asset-regime ${regimeClass}">${item.regime}</span>
                            </div>
                            <div class="asset-price">$${item.price.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 5})}</div>
                            ${signalTag}
                            <div class="asset-scores">
                                <div>
                                    <div class="score-bar-lbl">
                                        <span>BUY SCORE</span>
                                        <span>${item.buy_score.toFixed(0)}%</span>
                                    </div>
                                    <div class="score-bar-outer">
                                        <div class="score-bar-inner buy" style="width: ${item.buy_score}%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="score-bar-lbl">
                                        <span>SELL SCORE</span>
                                        <span>${item.sell_score.toFixed(0)}%</span>
                                    </div>
                                    <div class="score-bar-outer">
                                        <div class="score-bar-inner sell" style="width: ${item.sell_score}%"></div>
                                    </div>
                                </div>
                                <div style="display:flex; justify-content:space-between; font-size:9px; color:var(--neon-blue); margin-top:2px;">
                                    <span>ML PRED:</span>
                                    <span>${mlText} (${mlProb}%)</span>
                                </div>
                            </div>
                        `;
                        wlGrid.appendChild(card);
                    });
                } else {
                    wlGrid.innerHTML = '<div style="color:var(--text-muted); font-size:12px; grid-column:span 4; text-align:center;">Attesa sincronizzazione dati watchlist dal bot...</div>';
                }

            } catch (err) {
                console.error("Errore AJAX:", err);
                document.getElementById('status-badge').className = 'connection-status offline';
                document.getElementById('status-text').innerText = 'Offline';
            }
        }

        // COMANDI API IN VIA POST
        async function sendControl(payload) {
            try {
                const response = await fetch('/api/control', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const res = await response.json();
                if (res.status === 'success') {
                    showToast("Comando trasmesso con successo", "success");
                    updateDashboard();
                } else {
                    showToast("Errore trasmissione: " + res.error, "error");
                }
            } catch (err) {
                showToast("Errore di connessione al server", "error");
            }
        }

        function toggleTrading() {
            const isChecked = document.getElementById('master-switch').checked;
            sendControl({ trading_enabled: isChecked });
            addLog('lt-action', 'CMD', `Stato master trading impostato a: ${isChecked ? 'ATTIVO' : 'DISATTIVATO'}`);
        }

        function triggerEmergencyStop() {
            if (confirm("⚠️ SEI SICURO? Questa azione chiuderà TUTTE le operazioni e disabiliterà il bot.")) {
                sendControl({ emergency_stop: true });
                addLog('lt-alert', 'EMERGENZA', "Inviato comando EMERGENCY STOP! Chiusura totale in corso...");
            }
        }

        function saveParameters() {
            const threshold = document.getElementById('threshold-slider').value;
            const risk = document.getElementById('risk-input').value;
            sendControl({
                confluence_threshold: parseInt(threshold),
                portfolio_risk_limit_usd: parseFloat(risk)
            });
            addLog('lt-action', 'CMD', `Parametri salvati: Soglia = ${threshold}%, Rischio = $${risk}`);
        }

        function closePosition(ticket, symbol) {
            if (confirm(`Vuoi davvero richiedere la chiusura del ticket ${ticket} (${symbol})?`)) {
                sendControl({ close_ticket: ticket });
                addLog('lt-action', 'CMD', `Richiesta chiusura manuale per Ticket: ${ticket} (${symbol})`);
            }
        }

        // Loop di polling (ogni 2 secondi)
        setInterval(updateDashboard, 2000);
        updateDashboard();
    </script>
</body>
</html>
"""

# ==============================================================================
# ROUTE ENDPOINTS FLASK
# ==============================================================================
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(app.static_folder, 'manifest.json')

@app.route('/service-worker.js')
def serve_service_worker():
    response = make_response(send_from_directory(app.static_folder, 'service-worker.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/api/data')
def api_data():
    if not os.path.exists(DASHBOARD_DATA_FILE):
        return jsonify({
            "balance": 10000.0,
            "equity": 10000.0,
            "daily_pnl": 0.0,
            "daily_trades_count": 0,
            "active_positions": [],
            "watchlist": {},
            "trading_enabled": True,
            "confluence_threshold": 75,
            "portfolio_risk_limit_usd": 40.0,
            "last_updated": datetime.now().isoformat()
        })
    try:
        with open(DASHBOARD_DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/control', methods=['POST'])
def api_control():
    try:
        req_data = request.json
        if not req_data:
            return jsonify({"error": "Nessun dato fornito"}), 400

        # Carica il file bot_control.json esistente
        if os.path.exists(CONTROL_FILE):
            try:
                with open(CONTROL_FILE, 'r', encoding='utf-8') as f:
                    control = json.load(f)
            except Exception:
                control = {}
        else:
            control = {}

        # Default valori se non presenti
        if "trading_enabled" not in control: control["trading_enabled"] = True
        if "confluence_threshold" not in control: control["confluence_threshold"] = 75
        if "portfolio_risk_limit_usd" not in control: control["portfolio_risk_limit_usd"] = 40.0
        if "manual_close_tickets" not in control: control["manual_close_tickets"] = []
        if "emergency_stop" not in control: control["emergency_stop"] = False

        # Applica modifiche
        if "trading_enabled" in req_data:
            control["trading_enabled"] = bool(req_data["trading_enabled"])

        if "confluence_threshold" in req_data:
            control["confluence_threshold"] = int(req_data["confluence_threshold"])

        if "portfolio_risk_limit_usd" in req_data:
            control["portfolio_risk_limit_usd"] = float(req_data["portfolio_risk_limit_usd"])

        if "emergency_stop" in req_data:
            if req_data["emergency_stop"]:
                control["emergency_stop"] = True
                control["trading_enabled"] = False  # Spegne il trading

        if "close_ticket" in req_data:
            ticket = int(req_data["close_ticket"])
            if ticket not in control["manual_close_tickets"]:
                control["manual_close_tickets"].append(ticket)

        # Salva in bot_control.json
        os.makedirs(os.path.dirname(CONTROL_FILE), exist_ok=True)
        with open(CONTROL_FILE, 'w', encoding='utf-8') as f:
            json.dump(control, f, indent=4)

        return jsonify({"status": "success", "control": control})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_server():
    local_ip = get_local_ip()
    port = 5000
    
    print("\n" + "="*80)
    print(" 📊 AVVIO SERVER QUANT SUITE DASHBOARD & PWA CONTROL")
    print("="*80)
    print(f" 🔗 Indirizzo Locale (PC):     http://127.0.0.1:{port}")
    print(f" 🔗 Indirizzo LAN (Telefono):   http://{local_ip}:{port}")
    print("="*80)
    print(" Per installarlo sul telefono, connetti il telefono allo stesso Wi-Fi")
    print(" del computer, visita l'indirizzo LAN indicato e premi 'Aggiungi a Home'.")
    print("="*80 + "\n")
    
    # Esegue in ascolto su tutte le interfacce per permettere l'accesso da rete locale
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    run_server()
