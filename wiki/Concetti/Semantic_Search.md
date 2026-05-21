---
tags: [ai, llm, semantic-search, embedding, nlp]
date_created: 2026-05-07
source: "raw/How is LLM Changing Search on the Web.md"
---

# 🧭 Semantic Search — Ricerca Semantica

## 🎯 Keyword Search vs Semantic Search

| | Keyword Search | Semantic Search |
|---|---|---|
| **Come funziona** | Matching esatto delle parole | Matching del significato (vettori) |
| **Query: "auto economica"** | Cerca solo "auto" + "economica" | Trova anche "vettura low-cost", "automobile conveniente" |
| **Limitazione** | Miss semantica, synonym problem | Costo computazionale maggiore |
| **Esempio** | Google classico (2000s) | Google Search attuale, ChatGPT search |

## 📐 Come Funziona Tecnicamente

### 1. Embedding
Ogni testo (query o documento) viene trasformato in un **vettore numerico** tramite un modello di embedding:
```
"automobile economica" → [0.23, -0.45, 0.87, ..., 0.12]  (768 o 1536 dimensioni)
"vettura low-cost"     → [0.25, -0.43, 0.85, ..., 0.11]  (vicino al precedente!)
```

### 2. Cosine Similarity
Misura la **vicinanza semantica** tra due vettori:
$$similarity = \cos(\theta) = \frac{A \cdot B}{\|A\| \cdot \|B\|}$$
- **1.0** = identici semanticamente
- **0.0** = ortogonali (nessuna relazione)
- **-1.0** = opposti

### 3. Vector Database
Il database indicizza i vettori e permette di trovare i k documenti più simili alla query (**kNN search** — k-Nearest Neighbors).

## 🏗️ Pipeline di una Semantic Search
```
Query → Embedding Model → Query Vector
                                ↓
Database Vettoriale ← kNN Search → Top-k Documenti Simili
                                ↓
                    [Opzionale] LLM genera risposta dai documenti (= RAG)
```

## 💼 Applicazioni Pratiche
- **Motori di ricerca:** Google, Bing AI, Perplexity
- **Chatbot enterprise:** Ricerca in knowledge base aziendali
- **E-commerce:** Ricerca prodotti per descrizione semantica
- **Obsidian:** Il Graph View usa similarità concettuale tra note!

## 🔗 Collegato a
- [[RAG]] — Semantic Search è il cuore del Retrieval in RAG
- [[LLM_Changing_Search]]
- [[GPT_Models]]

## Fonti
* [[wiki/Fonti/Wikipedia_GPT.md]]
