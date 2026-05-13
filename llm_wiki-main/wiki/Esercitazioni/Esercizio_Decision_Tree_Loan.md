# 📝 Esercizio: Costruzione Albero di Decisione (Loanworthy)

Applichiamo l'algoritmo di costruzione di un albero di decisione utilizzando i dati tratti dalla sessione di studio.

## 1. Il Dataset (Training Data)
Vogliamo prevedere se un cliente è "Loanworthy" (Sì/No) basandoci su 4 attributi.

| RID | Married | Salary | Acct_balance | Age | Loanworthy (Class) |
|-----|---------|--------|--------------|-----|--------------------|
| 1   | No      | >= 50K | < 5K         | >= 25 | **Yes**              |
| 2   | Yes     | >= 50K | >= 5K        | >= 25 | **Yes**              |
| 3   | Yes     | 20-50K | < 5K         | < 25  | **No**               |
| 4   | No      | < 20K  | >= 5K        | < 25  | **No**               |
| 5   | No      | < 20K  | < 5K         | >= 25 | **No**               |
| 6   | Yes     | 20-50K | >= 5K        | >= 25 | **Yes**              |

## 2. Calcolo dell'Entropia Iniziale
Abbiamo 3 "Yes" e 3 "No" su 6 campioni totali.
- Probabilità Yes (p1) = 3/6 = 0.5
- Probabilità No (p2) = 3/6 = 0.5
- **Entropia(Dataset) = 1** (Massimo disordine).

## 3. Scelta dello Split (Information Gain)
Calcolando l'Information Gain per ogni attributo:
- **Gain(Married)** = 0.08
- **Gain(Salary)** = **0.67** (Vincitore!)
- **Gain(Acct_balance)** = 0.08
- **Gain(Age)** = 0.46

**Decisione:** Il primo bivio (Nodo Radice) dell'albero sarà il **Salary**.

## 4. Risultato dell'Albero
1. Se **Salary < 20K** -> La classe è sempre **No** (Foglia).
2. Se **Salary >= 50K** -> La classe è sempre **Yes** (Foglia).
3. Se **Salary 20K-50K** -> Bisogna guardare l'**Age**:
    - Se Age < 25 -> **No**.
    - Se Age >= 25 -> **Yes**.

---
*Vedi anche: [[Tecniche_di_Data_Mining]], [[Google_Gemini_Session]]*
