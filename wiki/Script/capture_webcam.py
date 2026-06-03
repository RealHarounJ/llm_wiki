#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📸 Real-Time Webcam Capturer & Telegram Sender
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Attiva la webcam del PC, acquisisce un fotogramma e lo invia
             all'istante come immagine sul bot Telegram dell'utente.
--------------------------------------------------------------------------------
"""

import cv2
import urllib.request
import json
import os
import time

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
PHOTO_PATH = "scratch/webcam.jpg"

def capture_photo():
    # Prova diversi indici di fotocamera
    for idx in [0, 1, 2]:
        cam = cv2.VideoCapture(idx)
        if cam.isOpened():
            time.sleep(1.0) # Riscaldamento sensore
            ret, frame = cam.read()
            if ret:
                os.makedirs(os.path.dirname(PHOTO_PATH), exist_ok=True)
                cv2.imwrite(PHOTO_PATH, frame)
                cam.release()
                return True
            cam.release()
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
    parts.append(f'Content-Disposition: form-data; name="photo"; filename="webcam.jpg"'.encode('utf-8'))
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
    except Exception:
        return False

def main():
    if capture_photo():
        send_telegram_photo("📸 Foto acquisita in tempo reale dalla webcam del PC!")

if __name__ == "__main__":
    main()
