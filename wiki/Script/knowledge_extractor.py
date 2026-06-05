#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMSR Knowledge Extractor
Legge tutti i file .md e .txt della cartella /raw ed estrae
variabili di trading, bias comportamentali, e alpha factors.
Esporta: data/knowledge_base.json
"""

import os
import re
import json
from pathlib import Path

RAW_DIR   = Path("raw")
OUT_FILE  = Path("data/knowledge_base.json")

# ── Sezioni chiave da cercare nei file ────────────────────────────────────────
SECTION_PATTERNS = {
    "trading_rules":     [r"rule[s]?\b", r"never\s+\w+", r"always\s+\w+", r"must\s+\w+",
                          r"regola[e]?\b", r"mai\s+\w+", r"sempre\s+\w+"],
    "risk_management":   [r"risk\b", r"stop.loss", r"drawdown", r"position.siz",
                          r"rischio\b", r"perdita\b", r"capital\b"],
    "behavioral_biases": [r"bias\b", r"fomo\b", r"fear\b", r"greed\b", r"emotion",
                          r"retail\s+trader", r"panic\b", r"euphori", r"irrazional"],
    "entry_signals":     [r"entry\b", r"setup\b", r"signal\b", r"trigger\b", r"breakout",
                          r"reversion\b", r"confluenc", r"ingresso\b"],
    "market_regimes":    [r"trend\w*\b", r"ranging\b", r"volatile\b", r"regime\b",
                          r"sideways\b", r"consolidat"],
    "alpha_factors":     [r"alpha\b", r"factor\b", r"momentum\b", r"value\b",
                          r"mean.reversion", r"carry\b", r"quality\b"],
}

# ── File di interesse (i più rilevanti per il trading) ────────────────────────
PRIORITY_FILES = [
    "20yo Italian Trader",
    "I have worked on trading floor",
    "Market Wizards",
    "Trend Following",
    "Systematic Trading",
    "Active_Portfolio_Management",
    "Advances in Financial Machine Learning",
    "Quantitative_Equity_Portfolio_Management",
    "Behavioural Investing",
    "neuronetworksbook",
    "Neural Networks in Algorithmic Trading",
    "How can I start hedgefund",
    "Quant Researcher",
    "Finding Alphas",
    "deleted by user",
]

def is_priority(filename):
    for keyword in PRIORITY_FILES:
        if keyword.lower() in filename.lower():
            return True
    return False

def extract_relevant_lines(text, max_lines=500):
    """Estrae le righe piu' rilevanti da un testo lungo."""
    lines = text.split('\n')
    relevant = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) < 15:
            continue
        line_lower = stripped.lower()
        for category, patterns in SECTION_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, line_lower):
                    relevant.append({"category": category, "text": stripped})
                    break
        if len(relevant) >= max_lines:
            break
    return relevant

def parse_trading_rules(lines):
    """Estrae regole di trading specifiche."""
    rules = []
    rule_indicators = [
        "rule", "never", "always", "must", "should", "don't", "avoid",
        "regola", "mai", "sempre", "devi", "non fare", "evita",
        "1.", "2.", "3.", "key:", "important:", "tip:"
    ]
    for item in lines:
        text_lower = item["text"].lower()
        if any(ind in text_lower for ind in rule_indicators):
            if len(item["text"]) > 20:
                rules.append(item["text"])
    return list(set(rules))[:100]  # top 100 unique rules

def parse_biases(lines):
    """Estrae bias comportamentali."""
    biases = {
        "FOMO": [],
        "loss_aversion": [],
        "anchoring": [],
        "herding": [],
        "overconfidence": [],
        "panic": [],
        "recency_bias": [],
        "confirmation_bias": [],
    }
    for item in lines:
        if item["category"] != "behavioral_biases":
            continue
        text_lower = item["text"].lower()
        if "fomo" in text_lower:                  biases["FOMO"].append(item["text"])
        if "loss" in text_lower:                   biases["loss_aversion"].append(item["text"])
        if "anchor" in text_lower:                 biases["anchoring"].append(item["text"])
        if "herd" in text_lower or "crowd" in text_lower: biases["herding"].append(item["text"])
        if "overconfid" in text_lower or "too sure" in text_lower: biases["overconfidence"].append(item["text"])
        if "panic" in text_lower:                  biases["panic"].append(item["text"])
        if "recent" in text_lower:                 biases["recency_bias"].append(item["text"])
        if "confirm" in text_lower:                biases["confirmation_bias"].append(item["text"])
    # Dedup
    return {k: list(set(v))[:10] for k, v in biases.items()}

def parse_alpha_factors(lines):
    """Estrae alpha factors menzionati."""
    factors = set()
    factor_keywords = {
        "momentum", "mean reversion", "value", "quality", "carry",
        "trend following", "breakout", "volatility", "seasonality",
        "earnings", "flow", "sentiment", "short interest",
    }
    for item in lines:
        text_lower = item["text"].lower()
        for fk in factor_keywords:
            if fk in text_lower:
                factors.add(fk)
    return list(factors)

def extract_numerical_params(text):
    """Estrae soglie numeriche menzionate nel testo."""
    params = {}
    # RSI levels
    rsi_matches = re.findall(r'rsi\s*[<>]=?\s*(\d+)', text.lower())
    if rsi_matches:
        params["rsi_thresholds"] = [int(x) for x in rsi_matches]
    # ATR multiples
    atr_matches = re.findall(r'(\d+\.?\d*)\s*[x*]\s*atr', text.lower())
    if atr_matches:
        params["atr_multiples"] = [float(x) for x in atr_matches]
    # Risk percentages
    risk_matches = re.findall(r'(\d+\.?\d*)\s*%\s*(?:risk|of\s+(?:account|capital|balance))', text.lower())
    if risk_matches:
        params["risk_pct"] = [float(x) for x in risk_matches]
    # Win rate mentions
    wr_matches = re.findall(r'win\s*rate\s*(?:of|:)?\s*(\d+\.?\d*)\s*%', text.lower())
    if wr_matches:
        params["win_rates"] = [float(x) for x in wr_matches]
    return params

def run_extraction():
    print("=" * 60)
    print("AMSR KNOWLEDGE EXTRACTOR")
    print("=" * 60)
    
    if not RAW_DIR.exists():
        print(f"[ERROR] Cartella '{RAW_DIR}' non trovata.")
        return {}
    
    knowledge_base = {
        "metadata": {
            "sources": [],
            "total_rules": 0,
            "total_lines_processed": 0,
        },
        "trading_rules":      [],
        "behavioral_biases":  {},
        "alpha_factors":      [],
        "market_regimes":     [],
        "risk_rules":         [],
        "entry_signals":      [],
        "numerical_params":   {},
        "prop_trader_insights": [],
        "institutional_insights": [],
    }
    
    total_lines = 0
    files_processed = 0
    
    for filepath in sorted(RAW_DIR.glob("*.md")) :
        if not is_priority(filepath.name):
            continue
        try:
            text = filepath.read_text(encoding="utf-8", errors="ignore")
            lines = extract_relevant_lines(text)
            total_lines += len(lines)
            files_processed += 1
            
            fname = filepath.name[:60]
            print(f"  [OK] {fname} -> {len(lines)} righe rilevanti")
            
            # Aggiungi source
            knowledge_base["metadata"]["sources"].append(filepath.name)
            
            # Estrai elementi
            rules    = parse_trading_rules(lines)
            biases   = parse_biases(lines)
            alphas   = parse_alpha_factors(lines)
            params   = extract_numerical_params(text[:50000])  # prime 50k chars
            
            knowledge_base["trading_rules"].extend(rules)
            
            for bias_key, bias_vals in biases.items():
                if bias_key not in knowledge_base["behavioral_biases"]:
                    knowledge_base["behavioral_biases"][bias_key] = []
                knowledge_base["behavioral_biases"][bias_key].extend(bias_vals)
            
            knowledge_base["alpha_factors"].extend(alphas)
            
            for param_key, param_vals in params.items():
                if param_key not in knowledge_base["numerical_params"]:
                    knowledge_base["numerical_params"][param_key] = []
                knowledge_base["numerical_params"][param_key].extend(param_vals)
            
            # File speciali
            fname_lower = filepath.name.lower()
            if "20yo" in fname_lower or "italian trader" in fname_lower:
                knowledge_base["prop_trader_insights"].extend(rules[:30])
            if "trading floor" in fname_lower:
                knowledge_base["institutional_insights"].extend(rules[:30])
            
            # Market regime mentions
            for line in lines:
                if line["category"] == "market_regimes":
                    knowledge_base["market_regimes"].append(line["text"])
            
            # Entry signals
            for line in lines:
                if line["category"] == "entry_signals":
                    knowledge_base["entry_signals"].append(line["text"])
            
            # Risk rules
            for line in lines:
                if line["category"] == "risk_management":
                    knowledge_base["risk_rules"].append(line["text"])
                    
        except Exception as e:
            print(f"  [SKIP] {filepath.name}: {e}")
    
    # Dedup tutto
    knowledge_base["trading_rules"]   = list(set(knowledge_base["trading_rules"]))[:200]
    knowledge_base["alpha_factors"]   = list(set(knowledge_base["alpha_factors"]))
    knowledge_base["market_regimes"]  = list(set(knowledge_base["market_regimes"]))[:100]
    knowledge_base["risk_rules"]      = list(set(knowledge_base["risk_rules"]))[:100]
    knowledge_base["entry_signals"]   = list(set(knowledge_base["entry_signals"]))[:100]
    
    for bk in knowledge_base["behavioral_biases"]:
        knowledge_base["behavioral_biases"][bk] = list(set(knowledge_base["behavioral_biases"][bk]))[:20]
    
    knowledge_base["metadata"]["total_rules"] = len(knowledge_base["trading_rules"])
    knowledge_base["metadata"]["total_lines_processed"] = total_lines
    knowledge_base["metadata"]["files_processed"] = files_processed
    
    # Salva
    OUT_FILE.parent.mkdir(exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
    
    print(f"\n[OK] Knowledge Base salvata: {OUT_FILE}")
    print(f"  File processati: {files_processed}")
    print(f"  Righe analizzate: {total_lines}")
    print(f"  Regole estratte: {knowledge_base['metadata']['total_rules']}")
    print(f"  Alpha factors:   {len(knowledge_base['alpha_factors'])}")
    print(f"  Bias catalogati: {sum(len(v) for v in knowledge_base['behavioral_biases'].values())}")
    
    return knowledge_base

if __name__ == "__main__":
    run_extraction()
