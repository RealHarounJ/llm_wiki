---
tags: [ai, llm, fine-tuning, machine-learning, gemma, training]
aliases: [Fine Tuning, Finetuning, Addestramento LLM]
date_created: 2026-06-17
last_modified: 2026-06-17
source_count: 1
---

# 🎯 Fine-Tuning dei Modelli LLM

Il **fine-tuning** è il processo di specializzare un [[Large_Language_Models|modello linguistico pre-addestrato]] su dati specifici per migliorarne le performance in un dominio preciso.

---

## 1. Analogia

> Un **medico generico** (modello base) → fa una specializzazione in cardiologia (fine-tuning) → diventa un **cardiologo** (modello specializzato).

Il modello base già conosce il linguaggio, la grammatica, la logica. Il fine-tuning insegna solo le specificità del dominio.

---

## 2. Come Funziona

```
Modello pre-addestrato (es. Gemma 4, LLaMA 3)
        ↓
  + Dataset specifico (esempi input/output)
        ↓
  Nuovo addestramento (leggero, economico)
        ↓
  Modello specializzato 🎯
```

### Fasi operative
1. **Raccolta dati**: costruisci coppie (prompt, risposta ideale)
2. **Preparazione**: formatta nel template del modello scelto
3. **Training**: esegui l'addestramento su GPU (ore/giorni)
4. **Valutazione**: testa su dati mai visti
5. **Deploy**: metti il modello in produzione

---

## 3. Tecniche Principali

| Tecnica | Descrizione | Costo GPU |
|---|---|---|
| **Full Fine-Tuning** | Aggiorna tutti i pesi del modello | Alto |
| **LoRA** | Low-Rank Adaptation — aggiorna solo matrici ridotte | Basso |
| **QLoRA** | LoRA + quantizzazione 4-bit | Molto basso |
| **RLHF** | Reinforcement Learning from Human Feedback | Alto |
| **Instruction Tuning** | Fine-tuning su coppie istruzione/risposta | Medio |

> 💡 **LoRA/QLoRA** sono le tecniche più usate per chi ha risorse limitate. Permettono di fare fine-tuning di modelli da 7B parametri su una singola GPU consumer.

---

## 4. Esempi Pratici

| Caso d'uso | Dati per il fine-tuning | Risultato |
|---|---|---|
| Chatbot aziendale | FAQ e documenti interni | Risponde solo su dati aziendali |
| Assistente medico | Letteratura scientifica | Risponde a domande cliniche |
| Generatore di codice | Migliaia di snippet | Suggerisce codice domain-specific |
| Traduttore burocratico | Coppie (documento formale, spiegazione semplice) | Traduce ISEE, INPS, ecc. |

---

## 5. Requisiti Hardware per Fine-Tuning

| Dimensione Modello | Tecnica | GPU Minima |
|---|---|---|
| 2B parametri | QLoRA | 6 GB VRAM (RTX 3060) |
| 7B parametri | QLoRA | 8 GB VRAM (RTX 3070) |
| 13B parametri | QLoRA | 12 GB VRAM (RTX 3080) |
| 70B parametri | QLoRA multi-GPU | 2× A100 |

---

## 6. Fine-Tuning vs RAG

| | Fine-Tuning | [[RAG]] |
|---|---|---|
| **Quando usarlo** | Stile, tono, dominio specifico | Aggiornamenti frequenti, documenti larghi |
| **Costo** | Una volta sola (training) | Ongoing (retrieval + inferenza) |
| **Aggiornamento** | Richiede re-training | Aggiorna solo il database vettoriale |
| **Allucinazioni** | Riduce ma non elimina | Riduce molto (cita le fonti) |

> In produzione spesso si **combinano**: fine-tuning per il tono + RAG per i dati aggiornati.

---

## 7. Strumenti

| Tool | Cosa fa |
|---|---|
| **Hugging Face Transformers** | Libreria base per fine-tuning |
| **PEFT** | Libreria per LoRA/QLoRA |
| **Axolotl** | Framework semplificato per fine-tuning |
| **LLaMA Factory** | UI per fine-tuning no-code |
| **Weights & Biases** | Monitoring del training |

---

## Fonti
- [[Sessione_AI_Business_Scalabile_2026]]
- [[Foundation_Models]] — Pre-training e architettura base
- [[GPT_Models]] — Storia e scaling dei modelli
- [[Transformer_Architecture]] — Architettura tecnica sottostante
