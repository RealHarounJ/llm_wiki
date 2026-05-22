---
tags: [ai, llm, transformer, deep-learning]
aliases: [Transformer, Architettura Transformer, Attention Is All You Need]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# 🧠 Architettura Transformer

L'**Architettura Transformer** è una struttura di rete neurale profonda introdotta nel 2017 da Google nel celebre paper *"Attention Is All You Need"* (Vaswani et al.). Ha rivoluzionato l'elaborazione del linguaggio naturale (NLP) e costituisce la base tecnologica di tutti i moderni **[[Large_Language_Models]] (LLM)** come **[[GPT_Models]] (GPT)**, Claude e Gemini.

---

## 1. Il Meccanismo di Self-Attention (Autore attenzione)

Prima dei Transformer, le reti ricorrenti (RNN e LSTM) elaboravano il testo in modo sequenziale (parola per parola), rendendo difficile l'addestramento su GPU e la memorizzazione di dipendenze a lungo termine. Il Transformer risolve questo problema grazie alla **Self-Attention**, che consente al modello di esaminare l'intera sequenza di input contemporaneamente e calcolare l'importanza relazionale di ciascuna parola rispetto a tutte le altre.

### I Vettori Q, K, V (Query, Key, Value)
Per ogni parola (rappresentata come embedding), il modello calcola tre vettori:
*   **Query ($Q$):** Rappresenta la parola corrente che sta "cercando" informazioni.
*   **Key ($K$):** Rappresenta le etichette di tutte le altre parole nella sequenza per indicare cosa offrono.
*   **Value ($V$):** Contiene l'effettivo contenuto informativo associato a ciascuna parola.

La formula matematica per il calcolo dell'attenzione standard (Scaled Dot-Product Attention) è:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Dove $\sqrt{d_k}$ è un fattore di scala basato sulla dimensione dei vettori per evitare che i gradienti svaniscano.

---

## 2. Multi-Head Attention (Attenzione Multi-Testa)

Invece di calcolare l'attenzione una sola volta, il Transformer divide i vettori Query, Key e Value in molteplici sotto-spazi, eseguendo il calcolo dell'attenzione in parallelo (teste).
*   **Vantaggio:** Teste diverse possono focalizzarsi su relazioni diverse contemporaneamente (es. una testa analizza le relazioni grammaticali, un'altra i riferimenti ai pronomi, un'altra i soggetti logici).

---

## 3. Positional Encoding (Codifica Posizionale)

Poiché il Transformer elabora tutti i token contemporaneamente (senza ricorrenza), non ha una nozione intrinseca dell'ordine delle parole. Per ovviare a questo, viene sommato un **Positional Encoding** (vettori basati su funzioni sinusoidali o apprese) agli embedding delle parole in ingresso. Questo consente al modello di sapere dove si trova ciascuna parola nella frase.

---

## 4. Varianti Architetturali

Il Transformer originale è composto da due blocchi speculari:
1.  **Encoder (Codificatore):** Analizza la sequenza di input per estrarre una rappresentazione semantica ricca (usato da modelli come BERT).
2.  **Decoder (Decodificatore):** Genera la sequenza di output in modo auto-regressivo (usato da modelli come GPT).

> [!NOTE]
> I modelli **GPT** (Generative Pre-trained Transformer) utilizzano un'architettura **Decoder-only** (solo decodificatore con maschera causale sull'attenzione per evitare che il modello "veda" le parole future durante l'addestramento).

---

## Fonti
* [[wiki/Fonti/Wikipedia_GPT.md]]
* [[wiki/Concetti/GPT_Models.md]]
