#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔊 PC Speaker Voice Player
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Genera una nota vocale gTTS in inglese britannico (Cambridge Accent),
             la converte in WAV e la riproduce ad alta voce direttamente dagli
             altoparlanti (speaker) del PC dell'utente usando winsound.
--------------------------------------------------------------------------------
"""

import sys
import os
import json
import soundfile as sf
from gtts import gTTS
import winsound

MP3_PATH = "scratch/temp_voice.mp3"
WAV_PATH = "scratch/temp_voice.wav"

def play_voice_on_pc(text):
    try:
        # 1. Genera l'audio TTS in inglese britannico (Cambridge accent)
        tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
        os.makedirs(os.path.dirname(MP3_PATH), exist_ok=True)
        tts.save(MP3_PATH)
        
        # 2. Converte MP3/OGG in WAV
        data, samplerate = sf.read(MP3_PATH)
        sf.write(WAV_PATH, data, samplerate)
        
        # 3. Riproduce l'audio tramite gli altoparlanti di sistema
        winsound.PlaySound(WAV_PATH, winsound.SND_FILENAME)
        
        # 4. Pulisce i file temporanei
        if os.path.exists(MP3_PATH):
            os.remove(MP3_PATH)
        if os.path.exists(WAV_PATH):
            os.remove(WAV_PATH)
        return True
        
    except Exception as e:
        print(f"Error in play_voice_on_pc: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        play_voice_on_pc(text)
