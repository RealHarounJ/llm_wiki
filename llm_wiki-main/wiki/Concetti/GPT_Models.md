---
tags: [ai, llm, gpt, transformer, storia]
aliases: [GPT Models, ChatGPT, Foundation Models]
date_created: 2026-05-07
source: "raw/Generative pre-trained transformer.md (Wikipedia)"
---

# 🤖 GPT — Generative Pre-Trained Transformer

## 🎯 Cos'è un GPT?
Un GPT è un tipo di **Large Language Model (LLM)** basato sull'architettura **Transformer**. È pre-addestrato su grandi dataset di testo non etichettato e capace di generare contenuto nuovo.

> **Paper fondativo:** *"Attention Is All You Need"* (Google, 2017) — ha introdotto l'architettura Transformer che è alla base di tutti i GPT.

## 📅 Timeline Storica

| Anno | Modello | Parametri | Novità |
|---|---|---|---|
| 2018 | **GPT-1** | 117M | Primo modello pre-addestrato + fine-tuning |
| 2019 | **GPT-2** | 1.5B | Generazione di testo coerente, rilascio graduale per rischi |
| 2020 | **GPT-3** | 175B | Few-shot learning, zero-shot capabilities |
| 2022 | **InstructGPT** | — | RLHF: allineamento con preferenze umane |
| 2022 | **ChatGPT** | — | Chatbot basato su GPT-3.5, lancio 30 nov 2022 |
| 2023 | **GPT-4** | — | Multimodale (testo + immagini), human-level benchmarks |
| 2024 | **GPT-4o** | — | Testo + immagini + audio nativamente |
| 2025 | **GPT-5** | — | Router automatico: modello veloce vs reasoning |

## 🏗️ Come Funziona (architettura base)
1. **Pre-training:** Il modello viene addestrato su enormi quantità di testo web non etichettato per imparare a predire la prossima parola.
2. **Fine-tuning:** Il modello viene specializzato su task specifici con dati etichettati.
3. **RLHF** (Reinforcement Learning from Human Feedback): Human raters valutano le risposte → il modello impara a generare output allineati alle preferenze umane.

## 📐 Concetti Chiave

### Foundation Model
Un modello addestrato su dati ampi che può essere adattato a molti task downstream diversi. GPT, PaLM, LLaMA, Gemini sono tutti Foundation Models.

### Scaling Laws
La performance dei LLM segue leggi empiriche (power-law): più parametri, più dati, più compute → migliore performance. *Non scala linearmente, ma segue una curva.*

### Emergent Abilities
Capacità che emergono *solo* oltre una certa soglia di scala e **non sono presenti nei modelli più piccoli**:
- Reasoning multi-step
- In-context learning (task da esempi nel prompt)
- Chain-of-Thought reasoning

### Chain-of-Thought (CoT)
Tecnica di prompting in cui il modello genera **passi intermedi di ragionamento** prima della risposta finale. Migliora drasticamente le performance su problemi matematici e logici.

## 🌍 Modelli Concorrenti
| Azienda | Modello |
|---|---|
| Google | Gemini, PaLM |
| Meta | LLaMA |
| Anthropic | Claude |
| Mistral AI | Mistral, Mixtral |
| DeepSeek | DeepSeek R1 |

## ⚠️ Rischi e Considerazioni Etiche
- **Bias:** I modelli amplificano i bias presenti nei dati di training
- **Allucinazioni:** Generano testo fluente ma factualmente scorretto
- **Impatto ambientale:** Training enormemente energivoro
- **Trademark:** OpenAI tenta di registrare "GPT" come marchio (controverso)

## 🔗 Collegato a
- [[LLM_Hub]]
- [[Transformer_Architecture]]
- [[RAG]]
- [[LLM_Changing_Search]]
