---
tags: [ai, machine-learning, deep-learning, training, backpropagation, neural-networks]
aliases: [Addestramento AI, Come si Addestra un Modello, Neural Network Training]
date_created: 2026-06-17
last_modified: 2026-06-17
source_count: 1
---

# 🧠 Come si Addestra un Modello AI

Processo con cui un modello di intelligenza artificiale impara dai dati, aggiustando i propri parametri interni per minimizzare l'errore sulle previsioni.

---

## 1. Principio Base — "Impara dagli Errori"

```
Input → [Modello] → Previsione
                         ↓
              Confronto con risposta reale
                         ↓
                    Calcolo errore (Loss)
                         ↓
              Backpropagation (chi ha sbagliato?)
                         ↓
              Optimizer aggiusta i pesi ↺
```

Questo ciclo si ripete **milioni di volte** su tutto il dataset.

---

## 2. I Parametri — Cosa Impara il Modello

Un modello è fatto di **pesi** (weights): numeri che determinano il suo comportamento. Addestrare = trovare i valori ottimali per questi pesi.

| Modello | Parametri |
|---|---|
| GPT-2 | ~1.5 miliardi |
| Gemma 4 (9B) | ~9 miliardi |
| GPT-4 | ~1.8 trilioni (stimati) |
| Llama 3 (70B) | ~70 miliardi |

---

## 3. Pipeline Completa di Training

```
1. 📦 Raccolta dati
        ↓
2. 🧹 Pulizia e preprocessing (tokenizzazione, normalizzazione)
        ↓
3. ⚙️  Scelta architettura (es. Transformer)
        ↓
4. 🔁 Training Loop:
   a) Forward pass  → il modello fa una previsione
   b) Loss function → misura quanto è sbagliata
   c) Backpropagation → calcola i gradienti
   d) Optimizer → aggiusta i pesi
        ↓
5. ✅ Valutazione su validation set
        ↓
6. 🚀 Deploy in produzione
```

---

## 4. Componenti Chiave

### Loss Function
Misura l'errore tra previsione e risposta corretta. Esempi:
- **Cross-entropy loss** → per classificazione e testo
- **MSE (Mean Squared Error)** → per regressione
- **Contrastive loss** → per embedding e similarity

### Backpropagation
Algoritmo che propaga l'errore "all'indietro" nella rete neurale per capire quale peso ha contribuito all'errore e di quanto va corretto.

Matematicamente usa la **regola della catena** (chain rule) del calcolo differenziale:
$$\frac{\partial L}{\partial w_i} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_i}$$

### Optimizer
Algoritmo che aggiusta i pesi in base ai gradienti calcolati dalla backpropagation.

| Optimizer | Caratteristica |
|---|---|
| **SGD** | Stochastic Gradient Descent — semplice ma lento |
| **Adam** | Adaptive — il più usato per LLM |
| **AdamW** | Adam con weight decay — standard per Transformer |
| **Lion** | Più efficiente memoria, usato da Google |

### Learning Rate
Controlla "quanto" aggiustare i pesi ad ogni step.
- Troppo alto → il modello diverge (instabile)
- Troppo basso → convergenza lentissima
- **Learning Rate Scheduler** → riduce il LR nel tempo

### Epoch
Una passata completa su **tutti** i dati di training.
- Troppo poche epoch → underfitting (modello non impara)
- Troppe epoch → overfitting (memorizza, non generalizza)

---

## 5. Come Imparano gli LLM

Il task di pre-training degli LLM è semplicissimo:

> **"Dato questo testo, prevedi il token successivo"**

```
Input:  "Il gatto è sul"
Target: "tappeto"

Input:  "La banca centrale ha alzato i"
Target: "tassi"
```

Ripetuto su **centinaia di miliardi** di token, il modello impara implicitamente: grammatica, fatti, logica, ragionamento, matematica, codice.

---

## 6. Fasi di Addestramento degli LLM Moderni

```
Fase 1: Pre-training
        → Enormi dataset di testo (Common Crawl, Wikipedia, GitHub...)
        → Obiettivo: imparare il linguaggio
        → Costo: milioni di €

Fase 2: Supervised Fine-Tuning (SFT)
        → Dataset di coppie (istruzione, risposta ideale)
        → Obiettivo: seguire le istruzioni

Fase 3: RLHF (Reinforcement Learning from Human Feedback)
        → Feedback umano su quale risposta è migliore
        → Obiettivo: allineare il comportamento ai valori umani
```

---

## 7. Costi di Training

| Tipo | Hardware | Durata | Costo Stimato |
|---|---|---|---|
| Fine-tuning piccolo (LoRA) | 1 GPU consumer | Ore | Quasi gratis |
| Fine-tuning dataset medio | 1 A100 | Giorni | €100-1.000 |
| Training da zero (7B) | 8× A100 | Settimane | €10.000-50.000 |
| Training da zero (GPT-4 scale) | Migliaia di GPU | Mesi | **€50-100 milioni** |

---

## 8. Concetti Correlati

- [[Fine_Tuning_LLM]] — Specializzare un modello già addestrato
- [[Transformer_Architecture]] — L'architettura neurale dominante per gli LLM
- [[Foundation_Models]] — Modelli base pre-addestrati su larga scala
- [[RAG]] — Alternativa al fine-tuning per aggiungere conoscenza

---

## Fonti
- [[Sessione_AI_Business_Scalabile_2026]]
- [[Foundation_Models]]
- [[GPT_Models]]
- [[Transformer_Architecture]]
