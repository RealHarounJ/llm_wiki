---
tags: [concept, theory]
aliases: [NoSQL Databases]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---
# 🌐 Database NoSQL & Sistemi Distribuiti di Big Data

I database NoSQL ("Not Only SQL") nascono per superare i limiti di scalabilità verticale dei DBMS relazionali tradizionali (RDBMS), consentendo di gestire le **3 V dei Big Data**: **Volume** (moli enormi di dati), **Velocity** (velocità di scrittura/lettura in tempo reale) e **Variety** (dati non strutturati o semi-strutturati).

---

## 🏛️ 1. Le 4 Famiglie di Database NoSQL

Secondo il manuale *Elmasri & Navathe (Capitolo 24)*, i sistemi NoSQL si dividono in quattro grandi categorie architetturali:

| Modello di Dati | Descrizione Interna | Principali Casi d'Uso | Esempi Reali |
| :--- | :--- | :--- | :--- |
| **Chiave-Valore (Key-Value)** | Una tabella hash distribuita. Associa a una chiave univoca un valore arbitrario (blob di testo, JSON o binario). Estremamente performante. | Sessioni utente, caching ad alta velocità, carrelli della spesa. | **Redis, Amazon DynamoDB, Riak** |
| **Documentale (Document Store)** | Estende il modello chiave-valore. Il valore è un documento strutturato (JSON, BSON o XML). Consente di fare query e indicizzare i campi interni del documento. | Content Management Systems (CMS), cataloghi prodotti e-commerce. | **MongoDB, CouchDB** |
| **A Famiglie di Colonne (Column-Family)** | Memorizza i dati per colonne anziché per righe. Ogni "riga" ha un identificativo e può contenere un numero dinamico di colonne raggruppate in famiglie. | Time-series data, log di sistema, web analytics su larga scala. | **Apache Cassandra, HBase, ScyllaDB** |
| **A Grafi (Graph Databases)** | Basato sulla teoria dei grafi. I dati sono rappresentati da **Nodi** (entità), **Archi** (relazioni dirette) e **Proprietà** (attributi di nodi e archi). | Social network, motori di raccomandazione, sistemi antifrode. | **Neo4j, Amazon Neptune** |

---

## ⚖️ 2. Transazioni e Coerenza: ACID vs. BASE

Mentre i database relazionali tradizionali si fondano sulle rigide proprietà **ACID** per garantire la massima coerenza, i sistemi distribuiti NoSQL adottano il paradigma **BASE**, ottimizzato per la scalabilità e la tolleranza ai guasti:

*   **ACID (RDBMS tradizionali)**:
    *   *Atomicity*: Transazione tutto-o-niente.
    *   *Consistency*: Il database passa da uno stato valido a un altro.
    *   *Isolation*: Transazioni concorrenti isolate.
    *   *Durability*: Effetti persistenti anche dopo un crash.
*   **BASE (NoSQL distribuiti)**:
    *   **B**asically **A**vailable: Il sistema garantisce la disponibilità del servizio. Anche in caso di guasti a singoli nodi, il cluster risponde sempre alle richieste.
    *   **S**oft State: Lo stato dei dati può cambiare nel tempo senza un input esplicito, a causa dei processi di sincronizzazione asincrona tra i nodi.
    *   **E**ventually Consistent: Il database non garantisce la coerenza immediata su tutti i nodi, ma assicura che, se non avvengono nuove scritture, **alla fine** (eventually) tutti i nodi si allineeranno allo stesso valore.

---

## 📐 3. Il Teorema CAP (Teorema di Brewer)

Formulato da Eric Brewer, è il pilastro teorico dei sistemi distribuiti. Afferma che un sistema distribuito non può garantire contemporaneamente tre proprietà fondamentali:

1.  **Consistency (Consistenza - C)**: Ogni operazione di lettura restituisce la scrittura più recente o un errore. Tutti i nodi vedono gli stessi dati nello stesso istante.
2.  **Availability (Disponibilità - A)**: Ogni richiesta non fallita riceve una risposta (non d'errore), senza la garanzia che contenga i dati più recenti.
3.  **Partition Tolerance (Tolleranza alla Partizione - P)**: Il sistema continua a funzionare anche se la rete si divide, isolando alcuni nodi e impedendo loro di comunicare.

> [!IMPORTANT]
> **Il Trade-off Inevitabile**:
> In un sistema reale distribuito su più macchine fisiche, **le partizioni di rete (P) sono inevitabili**. Pertanto, in caso di partizione, gli architetti di database devono scegliere rigorosamente tra:
> *   **Sistemi CP (Consistency + Partition Tolerance)**: Sacrificano la disponibilità. Se una parte del cluster non è raggiungibile per confermare la scrittura coerente, il sistema rifiuta la richiesta o va in errore per prevenire dati disallineati.
> *   **Sistemi AP (Availability + Partition Tolerance)**: Sacrificano la consistenza immediata. I nodi isolati continuano ad accettare letture e scritture (garantendo l'operatività), accettando il rischio che nodi diversi abbiano versioni diverse dello stesso dato (incoerenza temporanea).

---

## 🕸️ 4. Consistent Hashing & Ring Topology

Nei database distribuiti (come Dynamo o Cassandra), i dati devono essere distribuiti su centinaia di nodi. 

### Il Problema dell'Hashing Tradizionale
Nel caching classico si usa la formula:
$$\text{Nodo} = \text{hash}(\text{key}) \pmod N$$
Dove $N$ è il numero di nodi nel cluster. 
*   **Il disastro**: Se aggiungiamo un nodo ($N \to N+1$) o un nodo fallisce ($N \to N-1$), la stragrande maggioranza delle chiavi calcolerà un modulo completamente diverso. Questo richiede un **ri-hashing quasi totale (circa il 99%) dei dati del database**, bloccando la rete e invalidando le cache.

### La Soluzione: Consistent Hashing
Il **Consistent Hashing** mappa sia i **nodi** che le **chiavi** sullo stesso spazio logico circolare, chiamato **Hash Ring** (anello di hashing), tipicamente rappresentato dall'intervallo $[0, 2^{32} - 1]$.

```text
                     [0 / 2^32 - 1]
                       * * * *
                   *             *
                *                   *
             Node 1 (ID: 100)        *
            *                         *
           *                           *  Key A (Hash: 250)
          *                             *
         *                               *
          Node 3 (ID: 800)              Node 2 (ID: 500)
            *                         *
                *                   *
                   *             *
                       * * * *
```

1.  **Posizionamento dei Nodi**: Si calcola l'hash dell'IP o dell'ID del server (es. $\text{hash}(\text{"Node 1"}) = 100$, $\text{hash}(\text{"Node 2"}) = 500$, ecc.) e lo si posiziona sull'anello.
2.  **Assegnazione delle Chiavi**: Si calcola l'hash della chiave del dato (es. $\text{hash}(\text{"User_42"}) = 250$). 
3.  **Ricerca del Nodo**: Per trovare su quale nodo salvare la chiave, ci si sposta sull'anello **in senso orario** a partire dall'hash della chiave fino a incontrare il primo nodo fisico disponibile.
    *   *Esempio*: La chiave con hash `250` viene salvata su **Node 2** (hash 500), poiché è il primo nodo che si incontra procedendo in senso orario.

### Vantaggi del Consistent Hashing
*   **Join / Leave efficienti**: Se un nodo si scollega o viene aggiunto, **solo una frazione minima delle chiavi ($K/N$) deve essere spostata**.
    *   Se aggiungiamo un nodo tra il Node 1 e il Node 2, solo le chiavi che cadono in quella porzione di anello migreranno sul nuovo nodo. Tutte le altre rimangono intatte sui rispettivi nodi.

### I Nodi Virtuali (Virtual Nodes / Vnodes)
Se abbiamo pochi nodi fisici, la distribuzione sull'anello rischia di non essere uniforme, creando **hotspots** (nodi sovraccarichi di dati mentre altri sono vuoti).
*   **Risoluzione**: Ogni nodo fisico viene mappato su molteplici **nodi virtuali** sparsi casualmente sull'anello (es. `NodeA_1`, `NodeA_2`, `NodeA_3`).
*   **Effetto**: La distribuzione delle chiavi diventa estremamente uniforme ed equilibrata dal punto di vista statistico.

---

## 👥 5. Replicazione & Consistenza a Quorum ($N, R, W$)

Per garantire l'alta affidabilità (Availability), ogni dato viene replicato su più nodi dell'anello. In genere, una chiave viene scritta sul nodo primario identificato dal Consistent Hashing e poi copiata nei successivi **$N-1$ nodi fisici in senso orario** sull'anello.

Il livello di consistenza e la velocità del cluster sono regolati da tre parametri chiave:

*   **$N$ (Replication Factor)**: Il numero totale di nodi su cui il dato deve essere replicato.
*   **$W$ (Write Quorum)**: Il numero di nodi che devono confermare la corretta scrittura su disco affinché l'operazione di scrittura sia considerata conclusa con successo.
*   **$R$ (Read Quorum)**: Il numero di nodi che devono rispondere a una richiesta di lettura affinché il dato sia considerato valido e restituito al client.

### La Formula della Consistenza Forte (Strong Consistency)
Per garantire che una lettura restituisca **sempre** l'ultima scrittura effettuata nel sistema distribuito, deve essere soddisfatta la seguente disequazione di Quorum:

$$R + W > N$$

> [!TIP]
> **Spiegazione Intuitiva (Principio dei Cassetti)**:
> Se la somma dei nodi di lettura e scrittura supera il fattore di replicazione totale, significa che l'insieme dei nodi scritti ($W$) e l'insieme dei nodi letti ($R$) devono necessariamente sovrapporsi in **almeno un nodo**. Quel nodo conterrà la versione più recente del dato, che verrà rilevata e restituita grazie al confronto delle versioni (es. tramite Vector Clocks).

#### Esempio Standard: $N = 3, W = 2, R = 2$
*   $R + W = 4 > 3$ (Consistenza Forte Garantita).
*   Se un nodo fallisce, il sistema continua a scrivere e leggere in modo coerente perché bastano 2 nodi funzionanti su 3.

### Consistenza Debole/Eventuale (Weak / Eventual Consistency)
Se configuriamo il sistema in questo modo:

$$R + W \le N$$

*   *Esempio*: $N = 3, W = 1, R = 1$ (Scrittura rapida su 1 nodo, lettura rapida da 1 solo nodo).
*   Il sistema è estremamente veloce e a bassissima latenza, ma c'è il rischio concreto di effettuare una lettura da un nodo replica che non ha ancora ricevuto l'aggiornamento asincrono (lettura di dati vecchi, detti *stale data*).

---

## 🕰️ 6. Vector Clocks (Orologi Vettoriali)

Nei sistemi distribuiti senza un coordinatore centrale (masterless, come Dynamo), i nodi possono accettare scritture concorrenti sulla stessa chiave. Come facciamo a sapere quale scrittura è avvenuta prima e a risolvere i conflitti se non possiamo fidarci del tempo fisico dei server?

> [!WARNING]
> **Il problema del Clock Drift**:
> Gli orologi fisici dei server (anche sincronizzati via NTP) soffrono di microscopici sfasamenti temporali (clock drift). Utilizzare i semplici timestamp fisici per decidere l'ordine delle transazioni in un DB distribuito causerebbe la perdita involontaria di dati legittimi (*Last-Write-Wins silenzioso*).

### Definizione di Vector Clock (VC)
Un **Vector Clock** è un vettore di contatori logici (interi), in cui ogni elemento è associato a un nodo specifico del sistema distribuito. Ogni dato salvato porta con sé il suo Vector Clock nella forma:

$$VC(D) = [(\text{Nodo}_A, c_A), (\text{Nodo}_B, c_B), \dots]$$

#### Regole di Funzionamento:
1.  Prima di scrivere o modificare un dato localmente, un nodo incrementa il proprio contatore nel Vector Clock del documento.
2.  Quando il client aggiorna un documento, invia la versione precedentemente letta comprensiva del suo Vector Clock. Il nodo che riceve la scrittura confronta il Vector Clock in ingresso con quello presente sul proprio disco.

### Determinazione della Causalità: Chi vince?

Date due versioni dello stesso documento, $D_1$ con orologio $VC_1$ e $D_2$ con orologio $VC_2$:

1.  **Dominanza causale ($D_1$ è antenato di $D_2$, quindi $D_2$ vince)**:
    *   $VC_1 < VC_2$ se e solo se per ogni nodo $i$, $VC_1[i] \le VC_2[i]$ e per almeno un nodo $j$ si ha $VC_1[j] < VC_2[j]$.
    *   *Significato*: $D_2$ ha incorporato tutte le modifiche di $D_1$ ed è andato oltre. La versione $D_1$ può essere sovrascritta in sicurezza.
2.  **Conflitto Concorrente (Scritture concorrenti conflittuali)**:
    *   Nessuno dei due orologi domina l'altro. Esistono nodi per cui $VC_1$ ha contatori maggiori, e nodi per cui $VC_2$ ha contatori maggiori.
    *   *Esempio*: $VC_1 = [A: 2, B: 1]$ e $VC_2 = [A: 1, B: 2]$.
    *   *Significato*: I dati sono stati scritti contemporaneamente e in modo indipendente su due partizioni diverse. Il database **non elimina nessuno dei due**, ma li conserva entrambi (chiamati *siblings*) e demanda la risoluzione del conflitto al client al momento della successiva lettura (es. unendo i carrelli della spesa).

#### Esempio Pratico Passo-Dopo-Passo

```text
1. Il client crea un record sul Nodo A.
   Dato: D1, Vector Clock: [A: 1]

2. Il client legge D1 e decide di modificarlo sul Nodo A.
   Dato: D2, Vector Clock: [A: 2] (A incrementa il suo contatore)

3. A causa di una partizione di rete, due aggiornamenti concorrenti avvengono in parallelo:
   - Client X aggiorna sul Nodo B: 
     Dato: D3, Vector Clock: [A: 2, B: 1]
   - Client Y aggiorna sul Nodo C: 
     Dato: D4, Vector Clock: [A: 2, C: 1]

4. La partizione si risolve. Un client legge la chiave ed entrambi i nodi rispondono.
   Il client riceve sia D3 [A: 2, B: 1] che D4 [A: 2, C: 1].
   Nessuno dei due domina l'altro! C'è un conflitto concorrente.
   Il client fonde i dati e scrive la versione risolta D5 sul Nodo A.
   Dato: D5, Vector Clock: [A: 3, B: 1, C: 1]
```

---

## 🔗 Collegamenti e Riferimenti
*   [[NoSQL_Databases]] (Scheda sintetica in Inglese)
*   [[Mappatura_ER_Relazionale]] (Per confrontare la teoria relazionale a quella NoSQL)
*   **Simulatore Interattivo NoSQL & CAP**: Per sperimentare praticamente questi concetti con partizioni di rete attive, apri il file locale [simulation_nosql/index.html](file:///c:/Users/jaafa/Downloads/llm_wiki-main/simulation_nosql/index.html) nel tuo browser web!

---
*Bibliografia: Elmasri & Navathe, Fundamentals of Database Systems, Capitolo 24.*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
