#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📹 Real-Time Video Recorder & Telegram Sender
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Attiva la webcam, registra un video di 10 secondi ad alta definizione,
             lo salva come file MP4 e lo invia direttamente su Telegram.
--------------------------------------------------------------------------------
"""

import cv2
import time
import os
import urllib.request
import json

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
VIDEO_PATH = "scratch/video.mp4"

def record_video():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        return False
        
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    os.makedirs(os.path.dirname(VIDEO_PATH), exist_ok=True)
    out = cv2.VideoWriter(VIDEO_PATH, fourcc, fps, (width, height))
    
    start_time = time.time()
    frames_recorded = 0
    
    while (time.time() - start_time) < 10.0:
        ret, frame = cam.read()
        if ret:
            out.write(frame)
            frames_recorded += 1
            time.sleep(0.045)
        else:
            break
            
    cam.release()
    out.release()
    return True

def send_telegram_video():
    if not os.path.exists(VIDEO_PATH):
        return False
        
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    with open(VIDEO_PATH, "rb") as f:
        video_data = f.read()
        
    parts = []
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="chat_id"'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append(CHAT_ID.encode('utf-8'))
    
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="caption"'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append("📹 Ecco il tuo video di 10 secondi registrato in tempo reale dalla webcam!".encode('utf-8'))
    
    parts.append(f"--{boundary}".encode('utf-8'))
    parts.append(f'Content-Disposition: form-data; name="video"; filename="video.mp4"'.encode('utf-8'))
    parts.append('Content-Type: video/mp4'.encode('utf-8'))
    parts.append(''.encode('utf-8'))
    parts.append(video_data)
    
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
        with urllib.request.urlopen(req, timeout=60) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("ok", False)
    except Exception:
        return False

def main():
    if record_video():
        send_telegram_video()

if __name__ == "__main__":
    main()
