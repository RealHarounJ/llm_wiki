---
tags: [concetto, finanza, quantitativa, portfolio-management, bayesian-alpha, black-litterman, qualitative-priors, posteriors]
aliases: [Bayesian_Portfolio_Mojo, Bayesian_Alpha, Modello_Black_Litterman, Analisi_Bayesiana]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 2
---

# 🧠 Bayesian Portfolio Mojo (Bayesian α)

La **Statistica Bayesiana applicata alla gestione quantitativa** (Bayesian Portfolio Mojo) fornisce una metodologia matematica rigorosa per risolvere uno dei problemi più critici del Portfolio Management: l'integrazione di informazioni qualitative non strutturate (come raccomandazioni degli analisti, rating, report di mercato o screening fondamentali) all'interno di modelli econometrici quantitativi basati interamente sui dati storici. 

Attraverso la stima del **Bayesian $\alpha$** e l'utilizzo del celebre **Modello di Black-Litterman**, il gestore quantitativo può evitare correzioni arbitrarie *ad-hoc*, riducendo gli errori di stima e migliorando la stabilità dei pesi ottimali di portafoglio.

---

## 1. Il Teorema di Bayes nel Portfolio Management

La statistica classica (frequentista) assume che i parametri del modello (es. l'Alfa atteso o il rendimento medio storico di un titolo) siano costanti ignote che possono essere stimate unicamente analizzando i dati storici. La statistica bayesiana, invece, tratta questi parametri come variabili casuali dotate di una propria distribuzione di probabilità.

Il **Teorema di Bayes** unisce le opinioni iniziali del gestore (Prior) con le informazioni campionarie derivate dai dati storici (Likelihood) per produrre stime aggiornate e ottimizzate (Posterior):

$$p(\boldsymbol{\theta} | \mathbf{x}) = \frac{p(\mathbf{x} | \boldsymbol{\theta}) p(\boldsymbol{\theta})}{p(\mathbf{x})}$$

Applicato al calcolo dell'Alfa di portafoglio:
- $\boldsymbol{\theta} \rightarrow$ Il vero Alfa atteso dei titoli.
- $p(\boldsymbol{\theta}) \rightarrow$ La distribuzione **Prior** (il grado di fiducia espresso sotto forma di probabilità sul fatto che un titolo sovraperformi, derivato da analisi qualitative, z-score screening, ecc.).
- $p(\mathbf{x} | \boldsymbol{\theta}) \rightarrow$ La **Likelihood** (i dati storici dei rendimenti di mercato catturati da un modello a fattori).
- $p(\boldsymbol{\theta} | \mathbf{x}) \rightarrow$ Il **Posterior** (il **Bayesian $\alpha$** finale che sarà inserito nel solutore di ottimizzazione QP).

---

## 2. Quantificazione dell'Informazione Qualitativa (Prior Chincarini)

Ludwig Chincarini formalizza tre metodi matematici precisi per convertire indicazioni puramente qualitative in parametri quantitativi di una distribuzione normale Prior.

### A. Quantificazione di uno Stock Screen (Liste di Selezione)
Si supponga che un team di analisti crei una lista di titoli consigliati. L'inclusione del titolo $A$ nella lista implica che si prevede che esso sovraperformerà un titolo $B$ non incluso. 
Definiamo $p_A = P(\alpha_A > \alpha_B)$ come la probabilità che il titolo in lista sovraperformi quello non in lista (calcolata basandosi sul consenso degli analisti, es. la frazione di analisti che consiglia il titolo $A$ sul totale).

1. Per il titolo $B$ non in lista, utilizziamo la stima classica del modello a fattori:
   $$\alpha_B \sim N(\hat{\alpha}_B, S(\hat{\alpha}_B)^2)$$
2. Per il titolo $A$ in lista, assumiamo lo stesso livello di incertezza $S(\hat{\alpha}_B)$ ma una media incognita $\mu_A$. Assumendo l'indipendenza delle stime:
   $$\alpha_A - \alpha_B \sim N\left(\mu_A - \hat{\alpha}_B, 2 S(\hat{\alpha}_B)^2\right)$$
3. Esprimiamo la probabilità di sovraperformance tramite la funzione di ripartizione della normale standard $\Phi$:
   $$P(\alpha_A > \alpha_B) = P(\alpha_A - \alpha_B > 0) = \Phi\left(\frac{\mu_A - \hat{\alpha}_B}{\sqrt{2} S(\hat{\alpha}_B)}\right) = p_A$$
4. Risolvendo rispetto alla media Prior incognita del titolo consigliato $\mu_A$:
   
$$\mu_A = \hat{\alpha}_B + \sqrt{2} S(\hat{\alpha}_B) \Phi^{-1}(p_A)$$

> [!NOTE]
> Dove $\Phi^{-1}$ è la funzione inversa della normale standard. Se il consenso degli analisti su $A$ è del $70\%$ ($p_A = 0.70$), la formula alzerà matematicamente la media Prior di $A$ rispetto alla stima del modello storico di un valore proporzionale alla volatilità residua del titolo, in modo rigoroso e privo di arbitrarietà.

### B. Quantificazione di uno Stock Ranking (Classifiche)
Se gli analisti producono classifiche di titoli anziché liste binarie, la probabilità $p_A = P(\alpha_A > \alpha_B)$ viene determinata confrontando le posizioni relative nella classifica consensus. La determinazione del Prior $\mu_A$ segue la stessa identica formulazione matematica, confrontando sistematicamente ciascun titolo con quello posizionato costantemente all'ultimo posto della classifica.

### C. Quantificazione di Raccomandazioni Buy/Sell
Nel caso di raccomandazioni discrete (Strong Buy, Buy, Hold, Sell, Strong Sell), Chincarini propone di definire il **Buy Ratio (BR)** di ciascun titolo come:
$$BR_i = \frac{\text{Numero di raccomandazioni Buy o Strong Buy}}{\text{Totale delle raccomandazioni Buy e Sell}}$$

La probabilità che il titolo $A$ sia superiore a $B$ è calcolata come differenza tra i rispettivi Buy Ratio:
$$P(\alpha_A > \alpha_B) = BR_A - BR_B$$
Questo valore viene inserito nella funzione $\Phi^{-1}$ per determinare la media Prior $\mu_A$.

---

## 3. Il Modello di Black-Litterman: L'Approccio Istituzionale

Il **Modello di Black-Litterman** (sviluppato da Fischer Black e Robert Litterman presso Goldman Sachs nel 1990) rappresenta l'applicazione bayesiana più famosa e utilizzata a livello istituzionale per la costruzione di portafogli efficienti.

### Il Problema Risolto
L'ottimizzazione classica di Markowitz è estremamente sensibile ai rendimenti attesi di input: piccole variazioni nelle stime storiche dei rendimenti producono portafogli estremamente concentrati o pesi non realistici. Black-Litterman risolve questo problema ridefinendo il punto di partenza dell'ottimizzazione.

### Il Processo Black-Litterman
1. **Prior di Equilibrio (Market Implied Returns)**:
   Invece di partire dai rendimenti medi storici, il modello ipotizza che il mercato sia in equilibrio e decodifica i rendimenti attesi impliciti ($\boldsymbol{\Pi}$) partendo dai pesi della capitalizzazione di mercato reale ($\mathbf{w}_{\text{mkt}}$) tramite "ottimizzazione inversa":
   $$\boldsymbol{\Pi} = \lambda \mathbf{\Sigma} \mathbf{w}_{\text{mkt}}$$
2. **Le Opinioni del Gestore (Views)**:
   Il gestore esprime le proprie opinioni soggettive (views) assolute o relative tramite tre matrici:
   - $\mathbf{P} \rightarrow$ Matrice identificativa dei titoli coinvolti nelle views ($K \times N$).
   - $\mathbf{Q} \rightarrow$ Vettore dei rendimenti attesi per ciascuna view ($K \times 1$).
   - $\mathbf{\Omega} \rightarrow$ Matrice diagonale di incertezza delle views ($K \times K$).
3. **Calcolo del Posterior (Rendimenti Attesi di Black-Litterman)**:
   Il modello combina il Prior di equilibrio e le Views del gestore applicando il teorema di Bayes in forma matriciale:

$$E[R] = \left[ (\tau \mathbf{\Sigma})^{-1} + \mathbf{P}^T \mathbf{\Omega}^{-1} \mathbf{P} \right]^{-1} \left[ (\tau \mathbf{\Sigma})^{-1} \boldsymbol{\Pi} + \mathbf{P}^T \mathbf{\Omega}^{-1} \mathbf{Q} \right]$$

Dove $\tau$ è uno scalare di calibrazione che esprime l'incertezza sul Prior di equilibrio (solitamente compreso tra $0.01$ e $0.05$).

```mermaid
graph TD
    A[Market Cap Weights w_mkt] -->|Reverse Optimization| B[Implied Equilibrium Returns Pi]
    C[Manager's Views P, Q, Omega] --> D[Black-Litterman Formula]
    B --> D
    D -->|Posterior Expected Returns E[R]| E[Mean-Variance QP Optimizer]
    E --> F[Stable & Robust Portfolio Weights w*]
```

> [!TIP]
> Se il gestore non ha alcuna opinione su un settore del mercato, la formula BL assegnerà automaticamente a quei titoli i rendimenti attesi di equilibrio ($\boldsymbol{\Pi}$), portando ad un'allocazione pari esattamente ai pesi di capitalizzazione di mercato. Questo garantisce stabilità eccezionale ed evita scommesse speculative non giustificate.

---

## Fonti
* [[wiki/Fonti/Fonte_Chincarini_QEPM.md]] (Chapter 14)
* [[wiki/Fonti/Fonte_Grinold_Kahn_APM.md]] (Chapter 10)
* [[wiki/Concetti/Z_Score_Stock_Screening.md]]
* [[wiki/Concetti/Portfolio_Weights_Optimization.md]]
