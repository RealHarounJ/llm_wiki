---
tags: [data-mining, classificazione, decision-tree, ml]
date_created: 2026-05-07
source: "wiki/Fonti/‎Google Gemini.md (Capitolo 28.3 Elmasri)"
---

# 🌳 Classificazione & Decision Tree

## 🎯 Cos'è la Classificazione?
La classificazione è **apprendimento supervisionato**: si usa un training set già etichettato per costruire un modello che classifichi i nuovi dati.

> Esempio: Data la storia bancaria di un cliente, è **buon rischio** o **cattivo rischio** per un credito?

## 🏗️ L'Albero Decisionale (Decision Tree)
Un albero decisionale è una struttura grafica che rappresenta le regole di classificazione:
- **Nodo radice:** Il primo attributo discriminante
- **Nodi interni:** Ulteriori domande sugli attributi
- **Nodi foglia:** La classe finale assegnata

## 📐 Information Gain & Entropia
L'algoritmo sceglie l'attributo migliore (quello con più **Information Gain**).

### Entropia (misura del caos)
$$I(s_1, ..., s_n) = -\sum_{i=1}^{n} p_i \cdot \log_2(p_i)$$
- Se tutti i record appartengono alla stessa classe → Entropia = 0 (ordine perfetto)
- Se record distribuiti equamente tra classi → Entropia massima (caos totale)

### Information Gain
$$Gain(A) = I(s_1,...,s_n) - E(A)$$

**Esempio dal testo (Elmasri Ch.28):**
- Gain(Salary) = **0.67** → La domanda migliore! Diventa la radice.
- Gain(Age) = 0.46
- Gain(Married) = 0.08 → Domanda inutile

## ⚙️ Algoritmo ID3 (semplificato)
```
1. Se tutti i record appartengono alla stessa classe → foglia
2. Calcola Information Gain per ogni attributo
3. Scegli l'attributo con Gain massimo come nodo
4. Dividi i record e ripeti ricorsivamente
```

## ✅ Pro & Contro
| Pro | Contro |
|---|---|
| Completamente interpretabile | Overfitting su dataset piccoli |
| Non richiede scaling dei dati | Instabile (piccole variazioni → albero diverso) |
| Gestisce dati categorici | Difficile per relazioni lineari complesse |

## 🔗 Collegato a
- [[Clustering_KMeans]]
- [[Tecniche_di_Data_Mining]]
- [[Fonte_Database_Systems_Elmasri]]

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
