---
tags: [ai, llm, rag, retrieval, embedding]
date_created: 2026-05-07
source: "raw/How is LLM Changing Search on the Web.md, wiki/Fonti/Where teams and agents work together *.md"
---

# 📚 RAG — Retrieval-Augmented Generation

## 🎯 Problema che Risolve
I LLM "chiusi" (closed-book) hanno una **data di taglio** (cutoff date) — non sanno nulla di eventi recenti. Inoltre, possono **allucinare** fatti. RAG risolve entrambi i problemi.

## 🏗️ Come Funziona RAG

```
┌─────────────────────────────────────────────────┐
│                  QUERY UTENTE                   │
│         "Qual è il fatturato Q1 2026?"          │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│              RETRIEVAL COMPONENT                │
│  1. Converti query in vettore (embedding)       │
│  2. Cerca nel database vettoriale i doc          │
│     più simili alla query                       │
│  3. Recupera i top-k documenti rilevanti        │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│             GENERATION COMPONENT               │
│  Costruisci prompt = query + documenti recuperati│
│  Invia all'LLM → genera risposta contestualizzata│
└─────────────────────────────────────────────────┘
```

## 📐 Componenti Tecnici

### Vector Embeddings
Un **embedding** è una rappresentazione numerica (vettore ad alta dimensione) di un testo che codifica il suo significato semantico.
- Testi simili → vettori vicini nello spazio vettoriale
- Misura di similarità: **cosine similarity**

### Vector Database
Db ottimizzato per ricerche di similarità vettoriale. Esempi: Pinecone, Weaviate, Chroma, pgvector.

### Chunking
I documenti lunghi vengono divisi in **chunks** (spezzoni) prima dell'indicizzazione. La scelta della dimensione ottimale del chunk è critica per la qualità del retrieval.

## 🔑 RAG vs Fine-Tuning vs Prompt Engineering

| Approccio | Quando usarlo | Costo |
|---|---|---|
| **Prompt Engineering** | Task semplici, poche istruzioni | Minimo |
| **RAG** | Knowledge base dinamica, fatti aggiornati | Medio |
| **Fine-Tuning** | Stile specifico, task molto specializzati | Alto |

## ✅ Vantaggi di RAG
- Dati aggiornabili senza re-training del modello
- Riduzione drastica delle allucinazioni
- Tracciabilità delle fonti (citazioni)
- Costo contenuto rispetto al fine-tuning

## 🔗 Collegato a
- [[GPT_Models]]
- [[Semantic_Search]]
- [[LLM_Hub]]
- [[LLM_Changing_Search]]

## Fonti
* [[wiki/Fonti/Wikipedia_GPT.md]]
