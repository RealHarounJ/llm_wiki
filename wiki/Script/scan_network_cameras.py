#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📶 Local Network IP Camera Scanner
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Identifica il subnet locale, effettua una scansione ultra-veloce multi-thread
             sulle porte standard delle IP camera (554 RTSP, 80/8080 HTTP, 81/88 MJPEG)
             e invia la lista dei dispositivi attivi trovati a Telegram.
--------------------------------------------------------------------------------
"""

import socket
import json
import urllib.request
import sys
from concurrent.futures import ThreadPoolExecutor

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"

CAMERA_PORTS = {
    554: "RTSP Video Stream",
    80: "HTTP Web/MJPEG Interface",
    8080: "HTTP Alternative/MJPEG Stream",
    81: "MJPEG Video Port",
    88: "IP Camera Web Port"
}

def get_local_subnet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        parts = local_ip.split(".")
        subnet = ".".join(parts[:-1])
        return subnet, local_ip
    except Exception:
        return "192.168.1", "127.0.0.1"

def scan_host_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.6)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            return port
    except Exception:
        pass
    finally:
        sock.close()
    return None

def scan_ip(ip):
    open_ports = []
    for port in CAMERA_PORTS.keys():
        open_port = scan_host_port(ip, port)
        if open_port:
            open_ports.append(open_port)
    if open_ports:
        return ip, open_ports
    return None

def send_telegram_message(message):
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
    except Exception:
        return False

def main():
    subnet, local_ip = get_local_subnet()
    
    ips_to_scan = [f"{subnet}.{i}" for i in range(1, 255)]
    found_devices = []
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(scan_ip, ips_to_scan)
        for r in results:
            if r:
                found_devices.append(r)
                
    if found_devices:
        report = f"📸 <b>RISULTATI SCANSIONE TELECAMERE RETE LOCALE</b> 📸\n\n"
        report += f"Trovati {len(found_devices)} host attivi con servizi video:\n\n"
        for ip, ports in found_devices:
            report += f"🖥️ <b>Host:</b> <code>{ip}</code>\n"
            for p in ports:
                report += f"  └ Port <code>{p}</code>: {CAMERA_PORTS[p]}\n"
                if p == 554:
                    report += f"    👉 RTSP URL: <code>rtsp://{ip}:554/stream1</code>\n"
                elif p in [80, 8080, 81, 88]:
                    report += f"    👉 Web URL: <a href='http://{ip}:{p}'>http://{ip}:{p}</a>\n"
            report += "\n"
    else:
        report = (
            f"ℹ️ <b>SCANSIONE COMPLETATA</b>\n"
            f"Nessuna telecamera IP standard o flusso video (RTSP/MJPEG) rilevato nel subnet <code>{subnet}.X</code>.\n"
        )
        
    send_telegram_message(report)

if __name__ == "__main__":
    main()
