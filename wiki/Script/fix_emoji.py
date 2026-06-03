#!/usr/bin/env python3
import re

path = "wiki/Script/capture_network_cameras.py"
with open(path, encoding="utf-8") as f:
    content = f.read()

# Replace only inside print() calls - emoji -> ASCII
emoji_map = {
    "\U0001f4e1": "[SCAN]",   # 📡
    "\U0001f50d": "[TRY]",    # 🔍
    "\u2705": "[OK]",          # ✅
    "\u274c": "[FAIL]",        # ❌
    "\U0001f310": "[NET]",     # 🌐
}

# Replace in print lines only
lines = content.split("\n")
new_lines = []
for line in lines:
    if line.strip().startswith("print("):
        for emoji, repl in emoji_map.items():
            line = line.replace(emoji, repl)
    new_lines.append(line)

new_content = "\n".join(new_lines)
with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done - emoji replaced in print() calls")
