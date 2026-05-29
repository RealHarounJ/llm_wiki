#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
👂 Telegram Real-Time Event Listener
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Gira in background ed effettua un polling rapido (ogni 5 secondi)
             sulle API di Telegram. Non appena rileva un nuovo messaggio inviato
             dall'utente, lo salva nell'inbox locale ed ESCE dal programma.
             La sua terminazione attiva istantaneamente l'agente AI in Antigravity
             (Reactive Wakeup), garantendo risposte sub-10 secondi sul cellulare.
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import time
import urllib.request

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = 715100445

STATE_FILE = "data/telegram_bridge_state.json"
INBOX_FILE = "data/telegram_inbox.json"

def main():
    # Forza codifica UTF-8
    if sys.platform.startswith('win'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("🤖 Telegram Event Listener avviato... In attesa di messaggi...")
    
    last_id = 0
    os.makedirs("data", exist_ok=True)
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
                last_id = state.get("last_processed_update_id", 0)
        except Exception:
            pass

    while True:
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
        if last_id > 0:
            url += f"?offset={last_id + 1}"
            
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                res = json.loads(response.read().decode('utf-8'))
                if res.get("ok") and res.get("result"):
                    new_messages = []
                    max_update_id = last_id
                    
                    for update in res["result"]:
                        update_id = update["update_id"]
                        if update_id > max_update_id:
                            max_update_id = update_id
                            
                        message = update.get("message")
                        if message and message.get("chat", {}).get("id") == CHAT_ID:
                            new_messages.append({
                                "text": message.get("text"),
                                "date": message.get("date"),
                                "update_id": update_id
                            })
                    
                    if new_messages:
                        # Scrive i messaggi nell'inbox locale
                        with open(INBOX_FILE, "w", encoding="utf-8") as f:
                            json.dump(new_messages, f, indent=4, ensure_ascii=False)
                        
                        # Aggiorna lo stato persistente
                        with open(STATE_FILE, "w", encoding="utf-8") as f:
                            json.dump({"last_processed_update_id": max_update_id}, f)
                            
                        print(f"✅ Rilevati {len(new_messages)} nuovi messaggi. Esco per attivare l'AI.")
                        sys.exit(0) # Termina con successo per scatenare il Reactive Wakeup!
                    
                    # Se ci sono stati aggiornamenti ma nessuno per noi, aggiorna comunque l'ID
                    if max_update_id > last_id:
                        last_id = max_update_id
                        with open(STATE_FILE, "w", encoding="utf-8") as f:
                            json.dump({"last_processed_update_id": max_update_id}, f)
        except Exception as e:
            print(f"⚠️ Errore nel loop di ascolto: {e}")
            
        # Polling ogni 1 secondo per garantire reattività ultra-veloce
        time.sleep(1)

if __name__ == "__main__":
    main()
