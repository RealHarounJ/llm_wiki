---
tags: [concept, data-mining, algorithms, techniques]
source_count: 2
last_modified: 2026-05-06
---

# 🛠️ Tecniche di Data Mining

Le tecniche di Data Mining mirano a raggiungere quattro obiettivi principali (**PICO**):
- **Prediction**: Determinare il comportamento futuro di alcuni attributi.
- **Identification**: Identificare l'esistenza di un item, evento o attività (es. intrusioni di rete).
- **Classification**: Partizionare i dati in classi o categorie.
- **Optimization**: Ottimizzare l'uso di risorse limitate.

## Tipologie di Analytics
L'analisi si evolve lungo quattro livelli di complessità:
1. **Descriptive**: "Cosa è successo?"
2. **Diagnostic**: "Perché è successo?"
3. **Predictive**: "Cosa succederà?"
4. **Prescriptive**: "Cosa dovrei fare?"

## 1. Classificazione (Classification)
Costruisce modelli per assegnare i dati a categorie predefinite (Apprendimento Supervisionato).

### Concetti Fondamentali
Perché la classificazione funzioni, dobbiamo distinguere tra:
- **Features (Attributi/Variabili Indipendenti)**: Sono le caratteristiche misurabili del dato (es. Età, Reddito, Stato Civile). Sono le "domande" che l'algoritmo pone per decidere.
- **Class (Etichetta/Variabile Dipendente)**: È il risultato o la categoria che vogliamo prevedere (es. "Rischioso" o "Affidabile", "Spam" o "No Spam").
- **Training Set**: Insieme di dati con etichette note usato per "istruire" il modello.
- **Test Set**: Insieme di dati usato per valutare quanto il modello è preciso su dati mai visti prima.
- **Esempio**: Classificare le email come "Spam" o "Legittime".
- **Algoritmi comuni**:
    - **Decision Trees**: Modelli a albero basati sull'**Algoritmo di Hunt**.
        - Si basano sullo split iterativo dei dati.
        - **Scelta dello split**: Si cerca di massimizzare l'**Information Gain** (Guadagno di Informazione).
        - **Entropia (Entropy)**: Misura il disordine dei dati. Formula testuale: `Entropy = - Somma di [ p * log2(p) ]` dove p è la probabilità della classe.
        - **Information Gain**: `Gain = Entropia(Genitore) - Entropia(Figli)`. L'attributo con il Gain più alto viene scelto per lo split.
        - **Metriche Alternative**: **Gini Index**, **Classification Error**.
    - **SVM (Support Vector Machines)**: Ottimi per dati complessi ad alta dimensione.
    - **KNN (K-Nearest Neighbors)**: Classifica in base alla vicinanza con altri dati.
    - **Naive Bayes**: Basato sul teorema di Bayes.

## 2. Clustering
Raggruppa dati simili tra loro senza categorie predefinite (apprendimento non supervisionato).
- **K-Means**: Centroidi basati sulla media. Obiettivo: minimizzare il **SSE** (o **SSW** - Sum of Squares Within).
    - **Relazione Fondamentale**: SST = SSW + SSB. Minimizzando la coesione interna (SSW), si massimizza automaticamente la separazione tra cluster (SSB).
    - **K-Means++**: Algoritmo di inizializzazione avanzato che sceglie centroidi iniziali distanti tra loro per evitare ottimi locali.
    - **Condizioni di Stop**: L'algoritmo si ferma quando i centroidi non cambiano, la SSE migliora meno di una soglia X, o si raggiunge il numero massimo di iterazioni.
    - **Decision Boundaries**: Le linee di separazione tra i cluster si chiamano **Confini di Voronoi**.
    - **Valutazione**:
        - **Elbow Method**: Cerca il "gomito" nel grafico SSE/K.
        - **Silhouette Coefficient**: Varia da -1 a 1. Misura quanto un punto è vicino al proprio cluster rispetto al vicino più prossimo.
        - **Davies-Bouldin Index**: Rapporto tra dispersione interna e distanza inter-cluster. Valori bassi indicano un clustering migliore.
- **K-Medoids**: I centroidi devono essere punti reali del dataset.
- **DBSCAN (Density-Based)**: Raggruppa i punti in base alla densità. Distingue tra **Core points**, **Border points** e **Noise points**.

## 3. Regole di Associazione (Association Rules)
Cerca relazioni tra variabili in un dataset.
- **Esempio**: **Market Basket Analysis** (chi compra pane spesso compra anche burro).

## 4. Regressione (Regression)
Utilizzata per prevedere valori numerici continui.
- **Esempio**: Prevedere il prezzo futuro di un'azione o la temperatura.
- **Tipi**: Lineare, Multipla, Logistica.

## 5. Anomaly Detection (Outlier Detection)
Identificazione di record insoliti che potrebbero indicare errori, frodi bancarie o intrusioni di rete.

## 6. Reti Neurali (Neural Networks - ANN)
Modelli ispirati al cervello umano, eccellenti per pattern complessi ma spesso considerati "Black Box" (difficili da interpretare).

## Preparazione dei Dati (Standardization)
Per algoritmi basati sulla distanza (come K-Means o KNN), è fondamentale la **Standardizzazione**:
- Trasformare i dati per avere **media = 0** e **deviazione standard = 1**.
- Questo evita che variabili con scale diverse (es. stipendio in migliaia vs età in decine) abbiano pesi differenti nel calcolo della distanza euclidea.

---
*Vedi anche: [[Data_Mining]], [[Processo_KDD]], [[Gerarchia_di_Classificazione]]*
*Sources: [[Wikipedia]], [[GeeksforGeeks]]*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
