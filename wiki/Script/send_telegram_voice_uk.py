#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🇬🇧 British English Telegram Voice Message Sender (Cambridge Accent)
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Genera un file audio in inglese britannico (UK accent) usando gTTS
             con il TLD 'co.uk' e lo invia al bot Telegram.
--------------------------------------------------------------------------------
"""

import sys
import json
import urllib.request
import urllib.parse
import os
from gtts import gTTS

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
AUDIO_PATH = "scratch/voice.mp3"

def send_telegram_voice_uk(text):
    try:
        # 1. Genera l'audio TTS in inglese britannico (tld='co.uk')
        tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
        os.makedirs(os.path.dirname(AUDIO_PATH), exist_ok=True)
        tts.save(AUDIO_PATH)
        
        # 2. Invia l'audio tramite sendVoice
        url = f"https://api.telegram.org/bot{TOKEN}/sendVoice"
        
        boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        
        with open(AUDIO_PATH, "rb") as f:
            audio_data = f.read()
            
        parts = []
        parts.append(f"--{boundary}".encode('utf-8'))
        parts.append(f'Content-Disposition: form-data; name="chat_id"'.encode('utf-8'))
        parts.append(''.encode('utf-8'))
        parts.append(CHAT_ID.encode('utf-8'))
        
        parts.append(f"--{boundary}".encode('utf-8'))
        parts.append(f'Content-Disposition: form-data; name="voice"; filename="voice.mp3"'.encode('utf-8'))
        parts.append('Content-Type: audio/mpeg'.encode('utf-8'))
        parts.append(''.encode('utf-8'))
        parts.append(audio_data)
        
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
        
        with urllib.request.urlopen(req, timeout=30) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("ok", False)
                
    except Exception as e:
        print(f"Error in send_telegram_voice_uk: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        send_telegram_voice_uk(text)
