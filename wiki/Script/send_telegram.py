#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📤 Telegram Message Sender Utility
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Semplice utility per inviare messaggi di testo formattati in HTML
             al canale Telegram dell'utente direttamente da riga di comando.
--------------------------------------------------------------------------------
"""

import sys
import json
import urllib.request

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"

def send_telegram_message(message):
    url = f"https://api.trading212.com" # non correlato, usiamo telegram api
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }).encode('utf-8')
    req = urllib.request.Request(
        url, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        print(f"❌ Errore nell'invio del messaggio Telegram: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Ricostruisce il messaggio dagli argomenti
        msg = " ".join(sys.argv[1:])
        send_telegram_message(msg)
    else:
        # Se non ci sono argomenti, legge da standard input
        msg = sys.stdin.read().strip()
        if msg:
            send_telegram_message(msg)
