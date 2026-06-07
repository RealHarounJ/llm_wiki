---
tags: [math, foundations, lesson, algebra, equations, logarithms]
aliases: [Lezione 0 Matematica, Basi Algebriche, Prerequisiti Matematica]
date_created: 2026-06-06
last_modified: 2026-06-06
---

# 📐 Lezione 0: Prerequisiti Algebrici e Fondamenta

Benvenuto alla **Lezione 0** di Matematica Generale. Questa lezione è interamente dedicata alla **Fase 0 (Foundations)** del tuo piano di studio. Copre le basi algebriche essenziali necessarie per affrontare l'esame scritto e a crocette senza calcolatrice. Ogni singolo argomento qui trattato è fondamentale per evitare errori banali in compiti d'esame complessi.

---

## 1. Calcolo Letterale e Prodotti Notevoli

Saper semplificare e scomporre rapidamente espressioni algebriche è la chiave per risolvere i limiti e gli integrali.

### Prodotti Notevoli Fondamentali da memorizzare:
1.  **Quadrato di Binomio**:
    $$(a \pm b)^2 = a^2 \pm 2ab + b^2$$
2.  **Differenza di Quadrati (Somma per Differenza)**:
    $$(a + b)(a - b) = a^2 - b^2$$
3.  **Cubo di Binomio**:
    $$(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3$$
4.  **Somma e Differenza di Cubi** (importantissimo per rimuovere le forme indeterminate nei limiti):
    $$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$
    $$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$

---

## 2. Potenze e Radici

All'esame non avrai la calcolatrice, quindi devi saper manipolare le potenze e gli esponenti frazionari.

### Proprietà delle Potenze ($a, b > 0$):
*   $$a^m \cdot a^n = a^{m+n}$$
*   $$\frac{a^m}{a^n} = a^{m-n}$$
*   $$(a^m)^n = a^{m \cdot n}$$
*   $$a^{-n} = \frac{1}{a^n}$$
*   $$a^0 = 1 \quad (\text{per } a \neq 0)$$
*   $$a^{\frac{m}{n}} = \sqrt[n]{a^m}$$

> [!WARNING]
> ⚠️ **Errore comune**: Ricorda che $(a+b)^n \neq a^n + b^n$. Non distribuire mai l'esponente sulla somma!

---

## 3. Equazioni e Disequazioni di 1° e 2° Grado

Le disequazioni sono lo strumento principale per calcolare il **dominio delle funzioni** e studiare il **segno della derivata prima** (monotonia).

### Equazioni e Disequazioni di 2° Grado
Data la forma $ax^2 + bx + c = 0$, calcoliamo il discriminante $\Delta = b^2 - 4ac$:
*   Se $\Delta > 0$: due soluzioni reali distinte $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$.
*   Se $\Delta = 0$: una soluzione reale coincidente $x = -\frac{b}{2a}$.
*   Se $\Delta < 0$: nessuna soluzione reale.

#### Regola del Segno per Disequazioni di 2° Grado ($ax^2 + bx + c > 0$ o $< 0$ con $a > 0$):
Pensa sempre alla **parabola**:
*   Se $\Delta > 0$: 
    *   $ax^2 + bx + c > 0 \Rightarrow$ valori **esterni** ($x < x_1 \cup x > x_2$)
    *   $ax^2 + bx + c < 0 \Rightarrow$ valori **interni** ($x_1 < x < x_2$)
*   Se $\Delta = 0$:
    *   $ax^2 + bx + c > 0 \Rightarrow$ sempre verificata ($\forall x \neq x_1$)
    *   $ax^2 + bx + c < 0 \Rightarrow$ mai verificata.
*   Se $\Delta < 0$:
    *   $ax^2 + bx + c > 0 \Rightarrow$ sempre verificata ($\forall x \in \mathbb{R}$)
    *   $ax^2 + bx + c < 0 \Rightarrow$ mai verificata.

---

## 4. Logaritmi ed Esponenziali

I logaritmi e gli esponenziali compaiono in quasi tutti gli esercizi d'esame. Devi conoscere a memoria il loro andamento grafico e le loro proprietà algebriche.

```
Grafico qualitativo di y = e^x (esponenziale) e y = ln(x) (logaritmo naturale):

      y ^                                     y ^
        |                                       |
    e^x |      *                                |         * * * * ln(x)
        |     *                                 |     *
        |    *                                  |   *
--------|---*--------> x            ------------|--*---------> x
        |  *                                    | * | 1
      1 | *                                     |*  |
```

### Proprietà Fondamentali dei Logaritmi (base $a > 0, a \neq 1$ e argomenti $x, y > 0$):
1.  **Prodotto**:
    $$\log_a(x \cdot y) = \log_a(x) + \log_a(y)$$
2.  **Quoziente**:
    $$\log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)$$
3.  **Potenza**:
    $$\log_a(x^n) = n \cdot \log_a(x)$$
4.  **Base speciale**:
    $$\log_a(a) = 1 \qquad \text{e} \qquad \log_a(1) = 0$$
5.  **Logaritmo Naturale ($\ln(x)$)**: ha base $e \approx 2.718$.
    $$\ln(e^x) = x \qquad \text{e} \qquad e^{\ln(x)} = x$$

> [!IMPORTANT]
> 🚨 **Condizione di Esistenza del Logaritmo**:
> Il logaritmo è definito **solo** per argomenti **strettamente positivi**.
> Per trovare il dominio di $y = \ln(f(x))$, devi sempre imporre:
> $$f(x) > 0$$

---

## 🏋️ Esercizi di Autovalutazione (Fai i calcoli a mano!)

Risolvi i seguenti esercizi per verificare se le tue basi algebriche sono pronte per il programma avanzato.

### Esercizio 1: Calcolo algebrico e frazioni
Semplifica la seguente espressione algebrica razionale:
$$E(x) = \frac{x^2 - 9}{x^2 - 3x} \cdot \frac{x}{x^2 + 6x + 9}$$

### Esercizio 2: Disequazione di secondo grado
Trova l'intervallo di soluzioni reali per la disequazione:
$$2x^2 - 5x + 2 \le 0$$

### Esercizio 3: Calcolo del Dominio (Campo di Esistenza)
Trova il dominio della seguente funzione:
$$f(x) = \ln(x - 3) + \sqrt{10 - x}$$

### Esercizio 4: Equazione esponenziale parametrica (stile test a crocette)
Risolvi la seguente equazione trovando le soluzioni per $x$:
$$e^{2x} - 4e^x + 3 = 0$$
*(Suggerimento: poni $t = e^x$)*

---

## 🔗 Collegamenti Utili
*   Torna alla mappa di studio: [[Percorso_Studio_Matematica]]
*   Dashboard Matematica: [[Math_Home]]
*   Formulario: [[Math_Formulario]]
