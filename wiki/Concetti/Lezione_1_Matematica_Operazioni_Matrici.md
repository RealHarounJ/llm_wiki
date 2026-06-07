---
tags: [math, linear-algebra, lesson, matrices, vectors]
aliases: [Lezione 1 Matematica, Operazioni Matrici]
date_created: 2026-06-06
last_modified: 2026-06-06
---

# 📐 Lezione 1: Vettori, Matrici e Operazioni Fondamentali

Benvenuto nella tua prima lezione di **Matematica Generale (Algebra Lineare)**. 
Questa lezione affronta le basi dello **STAGE 1 - UNIT 1** del tuo percorso. Poiché l'esame si svolge interamente **senza calcolatrice**, ci concentreremo molto sulla precisione del calcolo a mente, sui passaggi logici e sulle definizioni teoriche.

---

## 1. I Vettori in $\mathbb{R}^n$

Un **vettore** $\mathbf{v} \in \mathbb{R}^n$ è una n-upla ordinata di numeri reali, scritta come riga o colonna:
$$\mathbf{v} = (v_1, v_2, \dots, v_n)$$

### Operazioni Fondamentali sui Vettori
Date due vettori $\mathbf{x} = (x_1, x_2, \dots, x_n)$ e $\mathbf{y} = (y_1, y_2, \dots, y_n)$ ed uno scalare $\lambda \in \mathbb{R}$:

1.  **Somma / Sottrazione** (componente per componente):
    $$\mathbf{x} \pm \mathbf{y} = (x_1 \pm y_1, x_2 \pm y_2, \dots, x_n \pm y_n)$$
2.  **Moltiplicazione per uno scalare**:
    $$\lambda\mathbf{x} = (\lambda x_1, \lambda x_2, \dots, \lambda x_n)$$
3.  **Prodotto Scalare** (il risultato è un **numero**, non un vettore!):
    $$\mathbf{x} \cdot \mathbf{y} = x_1 y_1 + x_2 y_2 + \dots + x_n y_n = \sum_{i=1}^n x_i y_i$$
4.  **Norma (o Lunghezza)** del vettore:
    $$\|\mathbf{x}\| = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$$

> [!WARNING]
> ⚠️ **Attenzione all'ortogonalità**: Due vettori si dicono **ortogonali** (perpendicolari) se il loro prodotto scalare è zero ($\mathbf{x} \cdot \mathbf{y} = 0$). 
> Ricorda che il prodotto scalare nullo **non** implica che uno dei due vettori sia nullo! 
> *Esempio:* $\mathbf{x} = (2, -3)$ e $\mathbf{y} = (3, 2)$ sono ortogonali poiché $\mathbf{x} \cdot \mathbf{y} = (2 \cdot 3) + (-3 \cdot 2) = 6 - 6 = 0$.

---

## 2. Le Matrici

Una **matrice** $m \times n$ è una tabella rettangolare ordinata con $m$ righe ed $n$ colonne:
$$A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$
L'elemento genrico si indica con $a_{ij}$, dove $i$ è l'indice di riga e $j$ è l'indice di colonna.

### Tipologie di Matrici da ricordare
*   **Quadrata**: se $m = n$ (stesso numero di righe e colonne).
*   **Trasposta ($A^T$)**: si ottiene scambiando le righe con le colonne ($a^T_{ij} = a_{ji}$).
*   **Diagonale**: una matrice quadrata in cui tutti gli elementi fuori dalla diagonale principale sono zero ($a_{ij} = 0$ per $i \neq j$).
*   **Identità ($I$)**: una matrice diagonale con tutti $1$ sulla diagonale principale.
*   **Simmetrica**: se coincide con la sua trasposta ($A = A^T$).

---

## 3. Operazioni tra Matrici

### Somma e Prodotto per uno Scalare
Come per i vettori, si effettuano **componente per componente**. Entrambe le matrici devono avere le stesse dimensioni $m \times n$.

### Prodotto tra due Matrici (Riga per Colonna)
Il prodotto $C = AB$ è definito **solo se** il numero di colonne della prima matrice $A$ è **uguale** al numero di righe della seconda matrice $B$.
*   Se $A$ è di dimensione $m \times p$ e $B$ è di dimensione $p \times n$, allora il prodotto $C = AB$ avrà dimensione $m \times n$.
*   L'elemento genrico $c_{ij}$ si calcola facendo il prodotto scalare tra la riga $i$ di $A$ e la colonna $j$ di $B$:
    $$c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{ip}b_{pj}$$

> [!IMPORTANT]
> ⚠️ **Proprietà Non Commutativa**: In generale, il prodotto tra matrici **non è commutativo**:
> $$AB \neq BA$$
> Spesso, anche se $AB$ è definito, $BA$ potrebbe non esserlo affatto a causa delle dimensioni.

---

### ✍️ Esempio Guidato di Prodotto Riga per Colonna

Siano:
$$A = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 3 & 1 \end{pmatrix} \quad (2 \times 3) \qquad \text{e} \qquad B = \begin{pmatrix} 2 & 1 \\ -1 & 0 \\ 3 & 4 \end{pmatrix} \quad (3 \times 2)$$

Le dimensioni sono compatibili ($3 = 3$). Il risultato $C = AB$ sarà una matrice $2 \times 2$.

Calcoliamo ogni elemento:
*   $c_{11}$ (Riga 1 di $A$ $\cdot$ Colonna 1 di $B$):
    $$c_{11} = (1 \cdot 2) + (-1 \cdot -1) + (2 \cdot 3) = 2 + 1 + 6 = 9$$
*   $c_{12}$ (Riga 1 di $A$ $\cdot$ Colonna 2 di $B$):
    $$c_{12} = (1 \cdot 1) + (-1 \cdot 0) + (2 \cdot 4) = 1 + 0 + 8 = 9$$
*   $c_{21}$ (Riga 2 di $A$ $\cdot$ Colonna 1 di $B$):
    $$c_{21} = (0 \cdot 2) + (3 \cdot -1) + (1 \cdot 3) = 0 - 3 + 3 = 0$$
*   $c_{22}$ (Riga 2 di $A$ $\cdot$ Colonna 2 di $B$):
    $$c_{22} = (0 \cdot 1) + (3 \cdot 0) + (1 \cdot 4) = 0 + 0 + 4 = 4$$

Quindi il prodotto finale è:
$$C = AB = \begin{pmatrix} 9 & 9 \\ 0 & 4 \end{pmatrix}$$

---

## 🏋️ Esercizi di Autovalutazione (Risolvi senza calcolatrice!)

Prendi carta e penna e risolvi i seguenti esercizi per verificare la comprensione e allenare il calcolo mentale veloce.

### Esercizio 1: Operazioni con i vettori
Dati i vettori in $\mathbb{R}^3$:
$$\mathbf{u} = (2, -1, 3) \qquad \text{e} \qquad \mathbf{v} = (1, 4, -2)$$
1.  Calcola $3\mathbf{u} - 2\mathbf{v}$.
2.  Calcola il prodotto scalare $\mathbf{u} \cdot \mathbf{v}$.
3.  Determina se i due vettori sono ortogonali.
4.  Calcola la norma $\|\mathbf{u}\|$.

### Esercizio 2: Prodotto tra matrici
Siano:
$$A = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} \qquad \text{e} \qquad B = \begin{pmatrix} 0 & 4 \\ 1 & -2 \end{pmatrix}$$
1.  Calcola il prodotto $AB$.
2.  Calcola il prodotto $BA$.
3.  Verifica che $AB \neq BA$.

### Esercizio 3: Trasposizione e Simmetria
Data la matrice:
$$M = \begin{pmatrix} 1 & -2 & 3 \\ -2 & 5 & 0 \\ 3 & 0 & 9 \end{pmatrix}$$
1.  Scrivi la matrice trasposta $M^T$.
2.  La matrice $M$ è simmetrica? Spiega perché.

---

## 🔗 Risorse di Riferimento
*   Torna alla mappa di studio: [[Percorso_Studio_Matematica]]
*   Consulta la teoria completa: [[Math_Algebra_Lineare]]
*   Formulario: [[Math_Formulario]]
