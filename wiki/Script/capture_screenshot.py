#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🖥️ Real-Time Screen Capturer & Telegram Sender
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Cattura lo schermo del PC (screenshot) e lo invia istantaneamente
             al bot Telegram dell'utente.
--------------------------------------------------------------------------------
"""

import urllib.request
import json
import os
import time
from PIL import ImageGrab

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
PHOTO_PATH = "scratch/screenshot.jpg"

def capture_screen():
    try:
        os.makedirs(os.path.dirname(PHOTO_PATH), exist_ok=True)
        img = ImageGrab.grab()
        img.save(PHOTO_PATH, "JPEG", quality=85)
        return True
    except Exception as e:
        print(f"Error capturing screen: {e}")
        return False

def send_telegram_photo(caption):
    if not os.path.exists(PHOTO_PATH):
        return False
        
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    with open(PHOTO_PATH, "rb") as f:
        photo_data = f.read()
        
    parts = []
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="chat_id"'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append(CHAT_ID.encode('utf-8'))
    
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="caption"'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append(caption.encode('utf-8'))
    
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="photo"; filename="screenshot.jpg"'.encode('utf-8'))
    parts.append('Content-Type: image/jpeg'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append(photo_data)
    
    parts.append(f"--{boundary}--".encode('utf-8'))
    
    body = b'\r\n'.join(parts)
    
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'Content-Length': str(len(body)),
            'User-Agent': 'Mozilla/5.0'
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("ok", False)
    except Exception as e:
        print(f"Error sending photo: {e}")
        return False

def main():
    if capture_screen():
        if send_telegram_photo("🖥️ Screenshot in tempo reale dello schermo del tuo PC!"):
            print("Screenshot sent successfully to Telegram!")
        else:
            print("Failed to send screenshot to Telegram.")
    else:
        print("Failed to capture screen.")

if __name__ == "__main__":
    main()
