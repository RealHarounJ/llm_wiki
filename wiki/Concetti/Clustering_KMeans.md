---
tags: [data-mining, clustering, k-means, ml]
date_created: 2026-05-07
source: "wiki/Fonti/‎Google Gemini.md (Capitolo 28.4 Elmasri)"
---

# 🔵 Clustering & K-Means

## 🎯 Cos'è il Clustering?
Il clustering è **apprendimento non supervisionato**: raggruppa i dati senza etichette predefinite. L'obiettivo è trovare gruppi di record simili tra loro e diversi dagli altri.

> Esempio: Raggruppare i clienti di un supermercato per abitudini d'acquisto simili → **segmentazione di mercato**.

## ⚙️ Algoritmo K-Means

```
Input:  Database D, numero desiderato di cluster k
Output: k cluster che minimizzano l'errore quadratico

1. Scegli k record casuali come centroidi iniziali (m₁, ..., mₖ)
2. RIPETI:
   a. Assegna ogni record al cluster il cui centroide è più vicino
      (distanza euclidea minima)
   b. Ricalcola il centroide di ogni cluster come media dei suoi record
3. FINO A: nessun cambiamento negli assegnamenti
```

## 📐 Distanza Euclidea
$$Distance(r_j, r_k) = \sqrt{\sum_{i=1}^{n} (r_{ji} - r_{ki})^2}$$

## 📐 Funzione di Errore (Squared Error)
$$Error = \sum_{i=1}^{k} \sum_{r_j \in C_i} Distance(r_j, m_i)^2$$

L'algoritmo converge verso un **minimo locale** (non necessariamente globale).

## 🔑 Come Scegliere k?
- **Elbow Method:** Plotta l'errore vs k, scegli il "gomito" della curva
- **Silhouette Score:** Misura quanto ogni punto è simile al suo cluster vs gli altri
- Conoscenza del dominio (es. 3 segmenti di mercato)

## ✅ Pro & Contro
| Pro | Contro |
|---|---|
| Semplice e veloce | Bisogna specificare k a priori |
| Scala bene su grandi dataset | Sensibile ai centroidi iniziali |
| Risultati interpretabili | Assume cluster sferici e di dimensione simile |

## 🔗 Collegato a
- [[Classificazione_Decision_Tree]]
- [[Tecniche_di_Data_Mining]]
- [[Fonte_Database_Systems_Elmasri]]

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
