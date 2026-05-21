---
tags: [concept, database, modeling, hierarchy]
source_count: 1
last_modified: 2026-05-05
---

# 🪜 Gerarchia di Classificazione (Classification Hierarchy)

La gerarchia di classificazione è il metodo strutturale usato nei database per organizzare i dati dal generale allo specifico (o viceversa) e per gestire la navigazione multidimensionale.

## 1. Prospettiva del Design (EER Modeling)
Nel design concettuale, le gerarchie si manifestano attraverso due percorsi mentali:
- **Specializzazione (Top-Down)**: Si parte da un'entità generale (Superclasse) e la si "spacca" in sottogruppi (Sottoclassi) con attributi unici.
    - *Esempio*: Persona → Studente / Professore.
- **Generalizzazione (Bottom-Up)**: Si osservano entità diverse con attributi comuni e si "astrae" una superclasse per evitare ridondanze.
    - *Esempio*: Libro + DVD → Risorsa.

### Vincoli di Gerarchia
- **Disjoint (d)**: Un'entità può appartenere a **una sola** sottoclasse.
- **Overlapping (o)**: Un'entità può appartenere a **più** sottoclassi contemporaneamente.
- **Total (Doppia linea)**: Ogni entità della superclasse **deve** appartenere a una sottoclasse.
- **Partial (Linea singola)**: Un'entità può esistere solo nella superclasse senza appartenere a nessuna sottoclasse.

## 2. Prospettiva Analitica (Data Warehouse & OLAP)
Nelle analisi multidimensionali, la gerarchia permette di navigare i dati (Dimensioni) a diversi livelli di granularità:
- **Roll-up**: Risalire la gerarchia per aggregare i dati (es. da Vendite Giornaliere → Vendite Annuali). Maggiore generalizzazione.
- **Drill-down**: Scendere nella gerarchia per rivelare dettagli (es. da Anno → Mese → Giorno). Maggiore specificità.

## 3. Implementazione Fisica
Le gerarchie vengono mappate in tabelle relazionali usando diverse strategie (Step 8 dell'algoritmo):
- **Multiple Relations**: Tabelle separate per superclasse e sottoclassi (più pulito per Overlapping).
- **Single Relation (Mega-table)**: Una sola tabella con colonne "flag" o un "discriminatore" (più veloce per query semplici, ma molti valori NULL).

---
*Vedi anche: [[Enhanced_ER_Model]], [[Data_Warehouse]], [[OLAP]]*
*Source: [[Database_Systems_Fundamentals]]*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
