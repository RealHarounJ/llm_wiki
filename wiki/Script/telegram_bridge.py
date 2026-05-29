#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📶 Telegram Bridge Inbox Checker
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Scarica gli ultimi messaggi inviati dall'utente al bot Telegram,
             filtrando per Chat ID, e li scrive in un file inbox locale per
             consentire all'agente AI di leggerli ed elaborarli da remoto.
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import urllib.request

# Configurazione credenziali Telegram dell'utente
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

    # 1. Carica l'ultimo update_id elaborato
    last_id = 0
    os.makedirs("data", exist_ok=True)
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
                last_id = state.get("last_processed_update_id", 0)
        except Exception:
            pass

    # 2. Richiedi gli aggiornamenti a Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    # Se abbiamo un last_id, richiediamo solo i nuovi messaggi successivi
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
                    # Filtra solo i messaggi di testo inviati dall'utente autorizzato
                    if message and message.get("chat", {}).get("id") == CHAT_ID:
                        new_messages.append({
                            "text": message.get("text"),
                            "date": message.get("date"),
                            "update_id": update_id
                        })
                
                if new_messages:
                    # Salva i nuovi messaggi nell'inbox locale per l'AI
                    with open(INBOX_FILE, "w", encoding="utf-8") as f:
                        json.dump(new_messages, f, indent=4, ensure_ascii=False)
                    print(json.dumps({"status": "new_messages", "count": len(new_messages)}, indent=2))
                else:
                    # Pulisce l'inbox se non ci sono nuovi messaggi
                    if os.path.exists(INBOX_FILE):
                        try:
                            os.remove(INBOX_FILE)
                        except Exception:
                            pass
                    print(json.dumps({"status": "no_new_messages"}, indent=2))
                
                # Salva lo stato con l'ultimo update_id
                if max_update_id > last_id:
                    with open(STATE_FILE, "w", encoding="utf-8") as f:
                        json.dump({"last_processed_update_id": max_update_id}, f)
            else:
                if os.path.exists(INBOX_FILE):
                    try:
                        os.remove(INBOX_FILE)
                    except Exception:
                        pass
                print(json.dumps({"status": "no_updates"}, indent=2))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    main()
