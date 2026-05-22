---
tags: [data-mining, associazione, apriori, ml]
date_created: 2026-05-07
source: "wiki/Fonti/Data Mining Techniques.md, wiki/Fonti/‎Google Gemini.md"
---

# 🛒 Regole di Associazione & Algoritmo Apriori

## 🎯 Cos'è?
Le regole di associazione trovano correlazioni tra elementi in grandi dataset di transazioni.
> **Market Basket Analysis:** "I clienti che comprano pannolini comprano anche birra nel weekend."

## 📐 Metriche Fondamentali

### Supporto (Support)
Frequenza con cui un insieme di items appare nelle transazioni:
$$Support(A \Rightarrow B) = \frac{\text{Transazioni con A e B}}{\text{Totale transazioni}}$$

### Confidence (Confidenza)
Quanto spesso B appare quando c'è A:
$$Confidence(A \Rightarrow B) = \frac{Support(A \cup B)}{Support(A)}$$

### Lift
Quanto l'associazione è più forte del caso:
$$Lift(A \Rightarrow B) = \frac{Confidence(A \Rightarrow B)}{Support(B)}$$
- **Lift > 1:** Associazione positiva (non casuale)
- **Lift = 1:** Indipendenza statistica
- **Lift < 1:** Associazione negativa

## ⚙️ Algoritmo Apriori
```
1. Trova tutti i frequent itemset (Support ≥ min_support)
   - Inizia da itemset di 1 elemento
   - Usa la proprietà ANTI-MONOTONA: se {A,B} è frequente,
     anche {A} e {B} lo sono → potatura
2. Genera le regole di associazione (Confidence ≥ min_conf)
3. Filtra per Lift > 1
```

**Proprietà Anti-Monotona (Apriori Principle):**
> Un itemset non può essere frequente se contiene un sottoinsieme non frequente.

## 💡 Esempio Pratico
| Transazione | Items |
|---|---|
| T1 | Latte, Pane, Burro |
| T2 | Latte, Pannolini, Birra |
| T3 | Pane, Burro, Caffè |
| T4 | Latte, Pane, Pannolini, Birra |

Regola trovata: `{Pannolini} → {Birra}` con Support=0.5, Confidence=1.0, Lift=2.0

## 🔗 Collegato a
- [[Clustering_KMeans]]
- [[Classificazione_Decision_Tree]]
- [[Data_Mining_Hub]]

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
