---
tags: [valutazione, titoli, bonds, stocks]
aliases: [Valutazione Bond, Valutazione Azioni]
---

# 📊 Valutazione Titoli (Bond e Azioni)

La valutazione si basa sul principio del **Valore Attuale (PV)** dei flussi di cassa futuri attesi.

## 1. Valutazione delle Obbligazioni (Bonds)
Il valore di un bond è il PV delle cedole e del valore nominale di rimborso.
$$P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{FV}{(1+r)^n}$$
- **$C$**: Cedola (Coupon).
- **$FV$**: Valore Nominale (Face Value).
- **$r$**: Tasso di rendimento richiesto (YTM - Yield to Maturity).
- **Relazione Prezzo-Tasso**: Se i tassi di mercato aumentano, il prezzo dei bond diminuisce (e viceversa).

## 2. Valutazione delle Azioni (Stocks)
Il valore teorico di un'azione è il PV di tutti i dividendi futuri attesi all'infinito.
$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}$$

### Modelli di Crescita
- **Zero Growth (Perpetuità)**: $P_0 = D / r$
- **Constant Growth (Gordon Model)**: $P_0 = \frac{D_1}{r - g}$
  - Dove $g$ è il tasso di crescita dei dividendi.
- **Variazione dei prezzi**: 
  - Se aumentano i profitti attesi → Aumentano i dividendi → Aumenta il prezzo.
  - Se aumenta il rischio → Aumenta il tasso di sconto ($r$) → Diminuisce il prezzo.

## 3. Terminal Value (Valore Terminale)
Nel valutare aziende o titoli con orizzonte infinito, si calcola il valore a una data futura ($T$) e lo si attualizza. Oltre un certo orizzonte, il PV del prezzo finale tende a zero, quindi ci si concentra sulla somma dei dividendi attualizzati.

---
**Vedi anche:**
- [[Time_Value_of_Money]]
- [[Valutazione_Aziendale]]
- [[Efficienza_dei_Mercati]]

## Fonti
* [[raw/Note Taking & Research Assistant Powered by AI.md]]
