#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📶 Local Network Comprehensive Scanner (Ping Sweep & Port Scan)
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Rileva il subnet, esegue un ping sweep parallelo su tutti i 254 IP
             locali per trovare TUTTI i dispositivi connessi, ne risolve il nome
             host e scansiona le porte principali per identificarne i servizi.
             Invia un report completo e strutturato su Telegram.
--------------------------------------------------------------------------------
"""

import os
import sys
import socket
import subprocess
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"

COMMON_PORTS = {
    80: "HTTP (Interfaccia Web / Router / Camera)",
    443: "HTTPS (Web Sicuro / Router)",
    445: "SMB/Microsoft-DS (PC Windows / File Share / NAS)",
    139: "NetBIOS (PC Windows / Condivisione)",
    22: "SSH (PC Linux / Raspberry Pi / Dispositivo Smart)",
    8080: "HTTP Alternativo (Web / Stream Video)",
    554: "RTSP (Streaming Video Telecamera IP)"
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

def ping_host(ip):
    cmd = f"ping -n 1 -w 250 {ip}"
    startupinfo = None
    if sys.platform.startswith('win'):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
    try:
        res = subprocess.run(cmd, shell=True, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0:
            return ip
    except Exception:
        pass
    return None

def scan_ports(ip):
    open_ports = []
    for port in COMMON_PORTS.keys():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.15)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_hostname(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except Exception:
        return "Dispositivo Sconosciuto"

def process_active_host(ip):
    ports = scan_ports(ip)
    hostname = get_hostname(ip)
    return {
        "ip": ip,
        "hostname": hostname,
        "ports": ports
    }

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
    
    ips = [f"{subnet}.{i}" for i in range(1, 255)]
    active_ips = []
    
    with ThreadPoolExecutor(max_workers=80) as executor:
        results = executor.map(ping_host, ips)
        for ip in results:
            if ip:
                active_ips.append(ip)
                
    devices = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(process_active_host, active_ips)
        for r in results:
            if r:
                devices.append(r)
                
    devices.sort(key=lambda x: [int(num) for num in x["ip"].split(".")])
    
    report = f"🖥️ <b>DISPOSITIVI CONNESSI ALLA TUA RETE LOCALE ({len(devices)})</b> 🖥️\n\n"
    for dev in devices:
        ip = dev["ip"]
        hostname = dev["hostname"]
        ports = dev["ports"]
        
        is_pc = ip == local_ip
        pc_label = " <b>(QUESTO PC)</b>" if is_pc else ""
        
        report += f"🌐 <b>IP:</b> <code>{ip}</code>{pc_label}\n"
        report += f"  ├ <b>Nome:</b> <code>{hostname}</code>\n"
        
        if ports:
            report += f"  └ <b>Porte aperte:</b>\n"
            for p in ports:
                report += f"    • Port <code>{p}</code>: {COMMON_PORTS[p]}\n"
        else:
            report += f"  └ <b>Servizi:</b> Nessun servizio standard rilevato\n"
        report += "\n"
        
    send_telegram_message(report)

if __name__ == "__main__":
    main()
