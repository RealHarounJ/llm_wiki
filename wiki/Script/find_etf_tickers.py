import json

with open(r'c:\Users\jaafa\Downloads\llm_wiki-main\data\t212_instruments.json', encoding='utf-8') as f:
    data = json.load(f)

# --- Cerca ETF dividend/value/world ---
keywords = ['dividend', 'value', 'ftse 100', 'superdividend', 'select div',
            'stoxx', 'world', 'msci em', 'emerging', 'isf', 'sdiv',
            'vanguard', 'ishs', 'blackrock', 'vaneck', 'wisdom', 'ftse all']

print("=== ETF VALUE / DIVIDEND / GLOBAL (primi 60 match) ===")
matches = []
for inst in data:
    if inst.get('type') != 'ETF':
        continue
    name = inst.get('name', '').lower()
    short = inst.get('shortName', '').lower()
    if any(k in name or k in short for k in keywords):
        matches.append(inst)

matches.sort(key=lambda x: x.get('name', ''))
for m in matches[:60]:
    print(f"  {m['ticker']:<28} {m['currencyCode']:<5} {m['shortName']:<12} {m['name']}")

# --- Cerca per portfolio (posizioni attuali) ---
print()
print("=== CERCA: ISF, SDIV, IDVY, TDIV, IEMS, VHYL ===")
targets = ['ISF', 'SDIV', 'IDVY', 'TDIV', 'IEMS', 'VHYL', 'VVAL', 'IWVL',
           'IWFV', 'IDHD', 'IDV', 'HDLG', 'GBDV', 'GBDVL', 'FUSD', 'HMWO',
           'VWRL', 'VEUR', 'VFEM', 'VAPX', 'VHVE', 'VJPN', 'VUSA']
for inst in data:
    if inst.get('type') != 'ETF':
        continue
    short = inst.get('shortName', '')
    if short in targets or inst.get('ticker', '').split('_')[0].replace('l','').upper() in targets:
        print(f"  {inst['ticker']:<28} {inst['currencyCode']:<5} {inst['shortName']:<12} {inst['name']}")
