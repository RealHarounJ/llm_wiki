---
tags: [data-mining, clustering, k-means, python, ml]
date_created: 2026-05-07
source: "raw/7 Most Asked Questions on K-Means Clustering.md (Towards Data Science - Aaron Zhu)"
---

# 🔵 K-Means Clustering — Guida Completa

## 🎯 Obiettivo
Raggruppare punti dati con caratteristiche simili nello stesso cluster (**internal cohesion**) e separare punti con caratteristiche diverse (**external separation**).

## 📐 Metriche di Qualità

### SSW — Sum of Squares Within (intra-cluster variance)
Misura la coesione interna: somma delle distanze quadratiche tra ogni punto e il centroide del suo cluster.
$$SSW = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - m_i\|^2$$
*Più piccolo = cluster più compatti = migliore*

### SSB — Sum of Squares Between (inter-cluster variance)
Misura la separazione esterna: distanza tra il centroide globale e i centroidi dei cluster.
*Più grande = cluster più separati = migliore*

> **Regola chiave:** $SST = SSW + SSB$ — minimizzare SSW massimizza automaticamente SSB.

## ⚙️ Algoritmo K-Means (step by step)

```
1. Inizializza: scegli k punti casuali come centroidi iniziali
2. Assegna: ogni punto → cluster con centroide più vicino (distanza euclidea)
3. Aggiorna: ricalcola centroidi come media dei punti del cluster
4. Ripeti 2-3 fino a:
   - Centroidi invariati (convergenza)
   - SSE migliorato < x%
   - Raggiunto numero massimo iterazioni
```

## 🔑 Come Scegliere il Valore di k

### Elbow Method
Plotta SSE vs k — scegli il "gomito" dove SSE inizia ad appiattirsi.

### Silhouette Analysis
$$S(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
- $a(i)$: distanza media dal punto ai suoi vicini nello stesso cluster
- $b(i)$: distanza media dal punto ai vicini nel cluster più prossimo
- $S(i) = 1$ → punto ben classificato
- $S(i) = 0$ → punto al confine
- $S(i) = -1$ → punto nel cluster sbagliato

### Davies-Bouldin Index
Rapporto tra dispersione intra-cluster e separazione inter-cluster. *Più basso = meglio.*

## 🚀 K-Means++ (inizializzazione migliorata)
Problema dell'algoritmo base: può bloccarsi in un **minimo locale**.

K-Means++ sceglie centroidi iniziali **lontani tra loro**:
```
1. Scegli il primo centroide casualmente
2. Per ogni punto rimanente: P(punto selezionato) ∝ distanza² dal centroide più vicino
3. Il punto più lontano dai centroidi scelti ha più probabilità di essere il prossimo
4. Ripeti fino a k centroidi
```

## 💻 Implementazione Python (sklearn)

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# IMPORTANTE: standardizzare sempre prima (unità diverse → scala diversa!)
X_scaled = StandardScaler().fit_transform(X)

# K-Means++ con 3 cluster
kmeans = KMeans(
    n_clusters=3,
    max_iter=1000,
    n_init=10,          # esegui 10 volte con starting points diversi
    init='k-means++',   # inizializzazione intelligente
    random_state=123    # riproducibilità
).fit(X_scaled)

labels = kmeans.labels_
sse = kmeans.inertia_  # SSW
```

## ✅ Vantaggi vs ⚠️ Limiti

| Vantaggi | Limiti |
|---|---|
| Semplice e veloce | Richiede k specificato a priori |
| Un solo iperparametro (k) | Sensibile agli outlier |
| Scalabile su grandi dataset | Assume cluster sferici e di dimensione simile |
| Risultati interpretabili | Converge a minimi locali (non globali) |
| | Non funziona con cluster non convessi (es. cerchi concentrici) |

## 🔗 Collegato a
- [[Clustering_KMeans]] — versione base dell'algoritmo
- [[Classificazione_Decision_Tree]] — algoritmo supervisionato comparabile
- [[Regole_di_Associazione]]
- [[Data_Mining_Hub]]
