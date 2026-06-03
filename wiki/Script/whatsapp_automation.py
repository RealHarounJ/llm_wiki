#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 Automated WhatsApp Voice Note Sender & PC Screenshot Capturer
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Genera un vocale in voce femminile, apre WhatsApp Desktop,
             cerca "Ada", invia il vocale, fa uno screenshot dello schermo
             e poi chiude WhatsApp.
--------------------------------------------------------------------------------
"""

import os
import sys
import time
import subprocess
import urllib.request
import urllib.parse
import win32gui
import win32con
import win32com.client
from gtts import gTTS
from PIL import ImageGrab

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
AUDIO_PATH = r"c:\Users\jaafa\Downloads\llm_wiki-main\scratch\voice.mp3"
SCREENSHOT_PATH = r"c:\Users\jaafa\Downloads\llm_wiki-main\scratch\whatsapp_sent.jpg"

def generate_voice_note(text):
    print("[1] Genero il messaggio vocale (voce femminile gTTS)...")
    try:
        os.makedirs(os.path.dirname(AUDIO_PATH), exist_ok=True)
        tts = gTTS(text=text, lang='it', slow=False)
        tts.save(AUDIO_PATH)
        print(f"  -> Vocale salvato in {AUDIO_PATH}")
        return True
    except Exception as e:
        print(f"  -> Errore gTTS: {e}")
        return False

def copy_file_to_clipboard():
    print("[2] Copio il file audio negli appunti di Windows...")
    try:
        # Usa PowerShell per copiare il file negli appunti come FileDrop
        cmd = f'Set-Clipboard -Path "{AUDIO_PATH}"'
        subprocess.run(["powershell", "-Command", cmd], check=True)
        print("  -> File audio copiato con successo negli appunti!")
        return True
    except Exception as e:
        print(f"  -> Errore copia appunti: {e}")
        return False

def find_and_focus_whatsapp():
    print("[3] Cerco e porto in primo piano la finestra di WhatsApp...")
    hwnd_list = []
    
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "WhatsApp" in title:
                hwnd_list.append((hwnd, title))
                
    win32gui.EnumWindows(winEnumHandler, None)
    
    if not hwnd_list:
        print("  -> WhatsApp non trovato nei processi visibili. Lo avvio...")
        subprocess.run(["powershell", "-Command", 'Start-Process "whatsapp:"'])
        time.sleep(4.0)
        win32gui.EnumWindows(winEnumHandler, None)
        
    if not hwnd_list:
        print("  -> Impossibile trovare la finestra di WhatsApp!")
        return None
        
    # Scegliamo la finestra principale di WhatsApp Desktop
    target_hwnd = None
    for hwnd, title in hwnd_list:
        if title == "WhatsApp":
            target_hwnd = hwnd
            break
            
    if not target_hwnd:
        target_hwnd = hwnd_list[0][0]
        
    title = win32gui.GetWindowText(target_hwnd)
    print(f"  -> Trovata finestra: HWND={target_hwnd}, Titolo='{title}'")
    
    # Portiamo in primo piano
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%') # Trucco Alt key per cedere il focus
        win32gui.ShowWindow(target_hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(target_hwnd)
        time.sleep(1.5)
        return target_hwnd
    except Exception as e:
        print(f"  -> Errore focus finestra: {e}")
        return target_hwnd

def automate_whatsapp_sending():
    hwnd = find_and_focus_whatsapp()
    if not hwnd:
        return False
        
    print("[4] Avvio automazione ibrida per cercare Ada ed inviare il file...")
    shell = win32com.client.Dispatch("WScript.Shell")
    
    # Ottieni le coordinate della finestra
    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = rect
    print(f"  -> Coordinate finestra: left={left}, top={top}, right={right}, bottom={bottom}")
    
    # 1. Clicca sulla barra di ricerca
    x_search = left + 140
    y_search = top + 140
    print(f"  -> Clicco sulla barra di ricerca a ({x_search}, {y_search})...")
    import win32api
    import win32con
    win32api.SetCursorPos((x_search, y_search))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_search, y_search, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_search, y_search, 0, 0)
    time.sleep(0.8)
    
    # Cancella testo precedente
    shell.SendKeys("^a")
    time.sleep(0.2)
    shell.SendKeys("{BACKSPACE}")
    time.sleep(0.5)
    
    # 2. Scriviamo "Ada"
    print("  -> Scrivo 'Ada'...")
    shell.SendKeys("Ada")
    time.sleep(2.0) # Attendi caricamento risultati
    
    # 3. Clicca sul primo risultato (Ada)
    x_chat = left + 140
    y_chat = top + 220
    print(f"  -> Clicco sul primo risultato della chat a ({x_chat}, {y_chat})...")
    win32api.SetCursorPos((x_chat, y_chat))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_chat, y_chat, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_chat, y_chat, 0, 0)
    time.sleep(2.0)
    
    # 4. Incolliamo il file (Ctrl+V)
    print("  -> Incollo il file audio (Ctrl+V)...")
    shell.SendKeys("^v")
    time.sleep(3.0) # WhatsApp impiega un attimo a preparare l'allegato
    
    # 5. Invio per inviare il file incollato
    print("  -> Invio per confermare l'invio dell'allegato...")
    shell.SendKeys("{ENTER}")
    time.sleep(4.0)
    
    print("  -> Automazione completata!")
    return True

def capture_pc_screenshot():
    print("[5] Catturo lo screenshot del PC...")
    try:
        img = ImageGrab.grab()
        img.save(SCREENSHOT_PATH, "JPEG", quality=85)
        print(f"  -> Screenshot salvato in {SCREENSHOT_PATH}")
        return True
    except Exception as e:
        print(f"  -> Errore screenshot: {e}")
        return False

def send_telegram_screenshot(caption):
    print("[6] Invio lo screenshot a Telegram...")
    if not os.path.exists(SCREENSHOT_PATH):
        return False
        
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    with open(SCREENSHOT_PATH, "rb") as f:
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
    parts.append(f'Content-Disposition: form-data; name="photo"; filename="whatsapp_sent.jpg"'.encode('utf-8'))
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
            import json
            res = json.loads(response.read().decode('utf-8'))
            return res.get("ok", False)
    except Exception as e:
        print(f"  -> Errore invio Telegram: {e}")
        return False

def close_whatsapp():
    print("[7] Chiudo l'applicazione WhatsApp...")
    # Chiude sia WhatsApp desktop UWP che WhatsApp classico
    subprocess.run(["powershell", "-Command", "Stop-Process -Name WhatsApp.Root -Force -ErrorAction SilentlyContinue"], shell=True)
    subprocess.run(["powershell", "-Command", "Stop-Process -Name WhatsApp -Force -ErrorAction SilentlyContinue"], shell=True)
    print("  -> WhatsApp chiuso con successo.")

def main():
    text_message = (
        "Ciao Ada! Sono ancora io. Haroun mi ha chiesto di dirti che si sta allenando duramente in palestra, ma pensa a te! Volevamo solo mandarti un saluto veloce. A dopo!"
    )
    
    if generate_voice_note(text_message):
        if copy_file_to_clipboard():
            if automate_whatsapp_sending():
                # Cattura screenshot MENTRE la finestra è ancora aperta per dimostrazione
                capture_pc_screenshot()
                
                # Invia screenshot su Telegram
                send_telegram_screenshot("🖥️ Ecco lo screenshot che mostra l'invio del messaggio vocale su WhatsApp ad Ada!")
                
                # Chiude WhatsApp come richiesto
                close_whatsapp()
                print("Operazione completata con successo!")
                return
                
    print("Operazione fallita!")

if __name__ == "__main__":
    main()
