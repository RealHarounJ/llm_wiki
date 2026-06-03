#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, urllib.request

TOKEN   = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
CHAT_ID = "715100445"

msg = (
    "\U0001f4a4 <b>PC in spegnimento...</b>\n\n"
    "Ho fermato tutti i processi in background.\n"
    "Il PC si spegne tra pochi secondi.\n\n"
    "Buonanotte! \U0001f319"
)

data = json.dumps({"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}).encode("utf-8")
req  = urllib.request.Request(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data=data, headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req, timeout=10) as r:
    print("Sent:", json.loads(r.read().decode()).get("ok"))
