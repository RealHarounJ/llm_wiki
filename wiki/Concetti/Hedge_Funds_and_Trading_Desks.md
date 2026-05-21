---
tags: [finance, hedge-fund, trading-desks, investment-banking, risk-management, regulation]
aliases: [Hedge Funds and Trading Desks, Sell-Side vs Buy-Side, Volcker Rule, Prime Brokerage]
date_created: 2026-05-20
last_modified: 2026-05-20
source_count: 3
---

# Teoria e Struttura Operativa degli Hedge Fund e Trading Desk

Questo modulo esamina l'architettura legale e l'economia di avvio degli Hedge Fund, e analizza in dettaglio i meccanismi interni delle sale operative (trading floor) delle banche d'investimento (Sell-Side) in contrapposizione ai fondi alternativi (Buy-Side).

---

## 1. Architettura Legale e Struttura del Capitale negli Hedge Fund

La costituzione di un fondo d'investimento alternativo richiede una rigorosa strutturazione societaria volta a massimizzare l'efficienza fiscale e limitare la responsabilità dei partecipanti.

### A) Il Modello Standard Statunitense: Delaware LP & LLC GP
La maggior parte dei fondi speculativi basati negli Stati Uniti adotta una struttura a due livelli:
- **Delaware Limited Partnership (LP):** È il veicolo di investimento vero e proprio (il fondo). Gli investitori vi partecipano come **Limited Partners (LPs)**, avendo responsabilità limitata al capitale conferito.
- **Limited Liability Company (LLC) come General Partner (GP):** È la società di gestione che assume la responsabilità operativa illimitata per le decisioni d'investimento (ma protetta dallo scudo della LLC) e risiede nello stato in cui opera il fund manager.
- **Vantaggio Fiscale:** Offre una tassazione trasparente (*pass-through taxation*): le perdite e i profitti fluiscono direttamente nelle dichiarazioni fiscali personali di LPs e GP, evitando la doppia tassazione societaria delle classiche Corporation.

### B) Il Limite dei 15 Investitori (Esenzione Regolamentare)
- **Regola Empirica:** Negli Stati Uniti, la SEC non richiede la registrazione formale come Hedge Fund e Investment Advisor se il numero di investitori totali del veicolo rimane **sotto le 15 persone** (e al di sotto di specifiche soglie di AUM).
- **Flessibilità dei Clienti:** In questa fase pre-registrata ("friends and family shop"), gli investitori non devono necessariamente soddisfare i severi requisiti di **investitore accreditato** (patrimonio > $1M o reddito > $200k), che sono invece obbligatori per tutti i partecipanti di un hedge fund registrato formale.

### C) Strutture di Ingestione a Basso Capitale (AUM < $5M)
Per gestori che partono con piccoli capitali di avvio, i costi operativi di un fondo tradizionale standalone sarebbero insostenibili. Si utilizzano quindi veicoli alternativi:
- **Variable Capital Company (VCC):** Struttura societaria ad ombrello (molto comune a Singapore) che consente di compartimentare sottomoduli di investimento segregando attivi e passivi, dividendo i costi di compliance.
- **Actively Managed Certificate (AMC):** Uno strumento di debito cartolarizzato emesso da una banca o un veicolo speciale (SPV) che replica passivamente le posizioni di un portafoglio gestito dal Portfolio Manager (PM). È l'opzione offshore più economica per testare strategie.
- **Incubator / Approved Funds (BVI):** Struttura leggera offshore (Isole Vergini Britanniche) concepita per manager emergenti con AUM massimo di $100M e limite di 20 investitori, con costi di setup legali inferiori a $10k.

---

## 2. Economia del Lancio e Scalabilità dell'AUM

Il lancio di un fondo speculative è un'impresa ad alto costo fisso, dove le economie di scala giocano un ruolo fondamentale per la sopravvivenza.

### A) Costi di Avvio (First-Year Burn Rate)
I costi iniziali variano a seconda della complessità computazionale e di asset class della strategia:
- **Standard Equity Fund:** Circa **$1.000.000** nel primo anno.
- **Credit / Systematic Funds (Algoritmici):** Circa **$2.000.000** nel primo anno per via delle licenze tecnologiche e dei feed dati a bassa latenza.
- **Chief Operating Officer (COO):** Assunzione strategica primaria per supervisionare la compliance regolamentare, le relazioni con i broker e la rendicontazione amministrativa. Stipendio medio stimato tra **$130.000 e $190.000**.

### B) I Livelli dell'AUM e Due Diligence Istituzionale
L'attrazione di capitali esterni segue una scala gerarchica basata sulle masse in gestione (**AUM**):

```
┌────────────────────────┐
│   AUM > $100 Milioni   │ ───► Attrattiva per Investitori Istituzionali (Fondi Pensione, Fondazioni)
└───────────┬────────────┘
            │
┌───────────▼────────────┐
│    AUM ~ $20 Milioni   │ ───► Visibilità per investitori qualificati esterni (Family Offices)
└───────────┬────────────┘
            │
┌───────────▼────────────┐
│   AUM Minimo: $5M      │ ───► Soglia di sopravvivenza per coprire i costi fissi operativi
└────────────────────────┘
```

- **Seed Investment Agreements:** Trattative in cui il manager concede sconti sulle commissioni storiche (es. ridurre il classico schema *2 e 20* — 2% management fee, 20% performance fee) o cede equity della LLC di gestione a un grosso investitore iniziale (*anchor investor*) in cambio di impegni di capitale a lungo termine (*lock-up periods*).

---

## 3. L'Ecosistema dei Trading Desk: Sell-Side vs. Buy-Side

La professione del "trader" ha significati diametralmente opposti a seconda che si operi per una banca d'investimento o per un hedge fund.

### A) Differenze Strutturali

| Caratteristica | Sell-Side (Banca d'Investimento) | Buy-Side (Hedge Fund) |
| :--- | :--- | :--- |
| **Ruolo del Trader** | Gestisce il bilancio della banca, fornisce liquidità, esegue coperture ed estrae spread. | Il **Portfolio Manager (PM)** decide l'asset allocation. Il trader fa solo **esecuzione** operativa al miglior prezzo. |
| **Edge Operativo** | Asimmetria informativa, infrastrutture proprietarie interne, prestiti titoli integrati. | Ricerca quantitativa, modelli statistici, velocità di reazione. |
| **Rischio di Licenziamento** | Medio. Si viene tagliati in caso di cattiva condotta politica o perdite gravi ripetute. | Elevatissimo. Mancati rendimenti portano al licenziamento immediato o alla chiusura del fondo. |
| **Remunerazione Base** | Salario fisso + bonus direttamente proporzionale al volume transato/PnL desk (~$300k in Asia). | Stipendio fisso + bonus derivato dal taglio concesso dal PM (~$50k-$100k). |

### B) Prime Services & Balance Sheet Renting
Le banche d'investimento ottengono profitti a basso rischio prestando il proprio stato patrimoniale (*balance sheet*) agli hedge fund:
1. Un hedge fund vuole posizionarsi long su un titolo a leva tramite **CFD** o **Equity Swap**.
2. La banca d'investimento acquista fisicamente il titolo a mercato per coprire il delta del derivato.
3. **Ottimizzazione del collaterale:** La banca detiene fisicamente le azioni a bilancio e le riutilizza per prestarle ad altri operatori corti (*short sellers*), intascando tassi di prestito (*stock lend fee*), utilizzandole come collaterale in contratti pronti contro termine (Repo), o facendo arbitraggi su tassi di cambio e depository receipt.
4. Pur producendo solo 25-100 bps di spread, su notionali miliardari la banca estrae enormi profitti privi di rischio di mercato diretto.

### C) Elusione del Divieto di Prop Trading (Volcker Rule)
- Il **Volcker Rule** (Dodd-Frank Act) vieta alle banche commerciali statunitensi di fare investimenti speculativi con capitali propri (*proprietary trading*).
- **Scappatoie Operative:** I trader bancari camuffano la speculazione tramite:
  - **Client Facilitation (Principal Trading):** Acquistare blocchi di azioni anticipando ordini massicci dei clienti a fine giornata, lucrando sul differenziale di prezzo.
  - **Esposizione di Tasso Complessa (Curve Betting):** Assumere posizioni su scadenze diverse per scommettere sulla pendenza della curva dei rendimenti (es. swap a 3 anni con clienti coperti con rolling a 3 mesi, bettando sul tasso di funding e sul roll-risk legati al tasso Rho).

---

## 4. Gestione del Rischio e Coperture Operative

Nelle sale operative istituzionali, il rischio non viene analizzato solo sul movimento direzionale del prezzo, ma su molteplici dimensioni matematiche.

### A) Le Greche e Limiti di Portafoglio
- **Delta ($\Delta$):** Esposizione direzionale pura al prezzo del sottostante. Scommesse naked delta sono vietate o strettamente limitate.
- **Rho ($\rho$):** Sensibilità del portafoglio alle variazioni dei tassi di interesse. È cruciale per i desk di derivati a lungo termine e per la gestione dei costi di finanziamento (*funding fees*).
- **DV01 (Dollar Value of a Basis Point):** Misura la variazione del prezzo di un titolo obbligazionario a fronte di una variazione dell'1% (o 1 bps) del rendimento.

### B) Strategie di Arbitraggio Comune
- **Index Arbitrage:** Sfrutta le temporanee discrepanze di prezzo tra i contratti future su indici e il paniere di azioni fisiche sottostanti che compongono l'indice stesso.
- **Statistical Arbitrage (Stat Arb):** Modello quantitativo che individua deviazioni statistiche nel prezzo di coppie di titoli storicamente correlati (Long/Short), confidando nella convergenza media (*mean reversion*).

### C) Limiti dell'Hedging & Black Swan
- **Costo del Rischio:** Coprire ogni singola greca e rischio di coda azzera i margini di profitto del desk (il costo dei derivati di copertura supera il profitto dello spread). 
- I desk operano quindi assumendo un livello calcolato di rischio residuo. Eventi estremi e imprevedibili (*Black Swan*) come insolvenze improvvise dei broker o default sovrani non sono modellabili e portano a perdite sistemiche strutturali.

---

## 5. Asimmetria Informativa e Dinamiche di Mercato

Il vantaggio competitivo istituzionale risiede principalmente nell'accesso asimmetrico alle informazioni e nei canali di esecuzione privilegiati.

### A) Il Vantaggio Temporale dei Flussi Informativi
- I trader istituzionali su terminali specializzati (es. Bloomberg, Reuters) e attraverso reti di contatti diretti sul mercato ricevono le breaking news societarie e i rumors caldi con un anticipo stimato fino a **15 minuti** rispetto alla pubblicazione sui media tradizionali o sulle applicazioni retail.
- Questo lasso temporale consente di riposizionare i portafogli ed eseguire gli ordini prima del movimento massiccio dei volumi.

### B) Analisi Tecnica (TA) vs. Fondamentale (FA)
- **Teoria dell'Efficienza dei Mercati (EMH):** Sostiene che i prezzi riflettano già tutte le informazioni disponibili.
- **Realtà Operativa:** I trader considerano l'efficienza una variabile psicologica e geopolitica (es. mercati ad alta trasparenza e liquidità come il Giappone sono molto efficienti; mercati a bassa trasparenza come la Cina sono fortemente inefficienti).
- **TA vs FA:** Nelle trading room, l'Analisi Fondamentale (FA) è considerata inefficace per il trading a breve termine poiché i dati reali sono costantemente monopolizzati dagli insider. L'**Analisi Tecnica (TA)** viene preferita per rilevare barriere psicologiche aggregate (supporti, resistenze, gap di liquidità) e trend di momentum, in particolare su asset volatili come le criptovalute.

---

## Fonti
- [[Fonte_Reddit_Hedge_Fund_Start]]
- [[Fonte_Investopedia_Hedge_Fund_Guide]]
- [[Fonte_Reddit_Trading_Floor_AMA]]
