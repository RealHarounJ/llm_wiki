---
tags: [esercitazione, corporate-finance, study-guide, exam-prep, soluzioni]
aliases: [Soluzioni Domande Corporate Finance, Risposte Esercitazione]
date_created: 2026-05-22
last_modified: 2026-05-22
---

# 📚 Soluzioni Complete — Domande di Corporate Finance

Questo documento raccoglie le risposte formali, rigorose e accademiche alle domande teoriche e al caso pratico contenuti nel file grezzo `questions corporate finance.md`. Ogni risposta è strutturata per riflettere lo standard richiesto all'esame, con formule finanziarie scritte in LaTeX e collegamenti attivi al Second Brain.

---

## 🏛️ Blocco 1 — Valore Temporale del Denaro e Criteri Base di Capital Budgeting

### Q1. Come calcolare il valore futuro di una somma $S$ investita oggi per i primi 5 anni? Mostra la formula in capitalizzazione composta.

Per calcolare il valore futuro ($FV$, *Future Value*) di una somma iniziale $S$ (valore attuale o $PV$, *Present Value*) investita per un orizzonte temporale di $t = 5$ anni ad un tasso di interesse annuo costante $r$ in regime di **capitalizzazione composta**, si applica la seguente formula fondamentale del [[Time_Value_of_Money]]:

$$FV_5 = S \cdot (1 + r)^5$$

#### Spiegazione Finanziaria:
* Il termine $(1 + r)^5$ rappresenta il **fattore di capitalizzazione composta** (*compounding factor*) a 5 anni.
* A differenza della capitalizzazione semplice, la capitalizzazione composta ipotizza che gli interessi maturati alla fine di ogni anno vengano **reinvestiti** immediatamente per generare ulteriori interessi nei periodi successivi (*interest on interest*).
* Il tasso $r$ deve essere espresso in forma decimale (es. se il tasso è del $5\%$, si utilizza $r = 0.05$).

---

### Q2. Spiega la differenza tra costo opportunità del capitale e rendimento atteso di un investimento.

Sebbene entrambi i termini rappresentino tassi di rendimento, essi hanno significati logici e decisionali completamente opposti nella finanza aziendale:

1. **Costo Opportunità del Capitale ($r$):**
   * **Definizione:** È il tasso di rendimento atteso offerto da attività finanziarie alternative disponibili sul mercato dei capitali che presentano lo **stesso livello di rischio** del progetto di investimento in esame.
   * **Ruolo decisionale:** Rappresenta la *soglia minima di rendimento* (*hurdle rate*) richiesta dagli investitori (azionisti e creditori) per rinunciare ad impieghi alternativi della liquidità. È una variabile **esogena**, determinata esclusivamente dalle condizioni del mercato finanziario.
   * Per approfondimenti sulla sua stima tramite il modello CAPM, vedi [[Topic_7_8_CAPM_Cost_of_Capital]].

2. **Rendimento Atteso dell'Investimento ($E[R]$ o $IRR$):**
   * **Definizione:** È il rendimento specifico che si stima che il progetto di investimento generi in base ai suoi flussi di cassa operativi prospettici e all'esborso iniziale.
   * **Ruolo decisionale:** È una variabile **endogena**, calcolata a partire dalle caratteristiche operative ed economiche interne del progetto stesso (ad esempio, è il tasso che azzera il valore attuale netto, ovvero l'[[Topic_5_NPV_Investment_Criteria#Internal Rate of Return (IRR)]]).

#### Regola di Decisione Finanziaria:
* Si crea valore economico se e solo se il rendimento stimato del progetto supera il costo opportunità del capitale:
  $$E[R] > r$$

---

### Q3. Il valore attuale netto (NPV) di un investimento è positivo: cosa si conclude? Cosa significa in termini di ricchezza finanziaria e tasso di rendimento?

La constatazione che un progetto presenti un $NPV > 0$ (Valore Attuale Netto positivo) porta a conclusioni economiche e decisionali estremamente precise:

1. **Conclusione Decisionale:**
   * Il progetto di investimento è **economicamente conveniente** e deve essere accettato (regola aurea dell'NPV).

2. **Implicazioni in termini di Ricchezza Finanziaria:**
   * Un $NPV > 0$ misura l'**incremento immediato e assoluto della ricchezza netta degli azionisti** dell'impresa, espresso in valore monetario attuale (a t=0).
   * All'approvazione del progetto, il valore di mercato complessivo dell'impresa ($V$) aumenta teoricamente di un ammontare esattamente pari all'NPV stesso:
     $$\Delta V = NPV$$
   * Rappresenta la creazione di valore puro dopo aver coperto tutti i costi del progetto, incluso il costo del capitale per finanziare l'esborso iniziale.

3. **Implicazioni in termini di Tasso di Rendimento:**
   * Significa che il tasso di rendimento interno ($IRR$) del progetto è **strettamente superiore** al costo opportunità del capitale ($r$):
     $$IRR > r$$
   * L'investimento rende ad un tasso superiore rispetto a quanto gli investitori avrebbero potuto ottenere sul mercato finanziario acquistando attività a parità di rischio.

Per approfondimenti, consultare la nota [[Topic_5_NPV_Investment_Criteria]].

---

### Q4. Il valore attuale netto (NPV) di un investimento è pari a zero. Dovresti investire o no?

Se $NPV = 0$, dal punto di vista prettamente teorico-matematico l'impresa si trova in una posizione di **perfetta indifferenza**. Tuttavia, l'analisi finanziaria avanzata suggerisce alcune considerazioni cruciali:

#### Significato Economico di $NPV = 0$:
* Un $NPV = 0$ non significa che il progetto non generi profitti o flussi di cassa. Significa che il progetto genera flussi di cassa il cui valore attuale è **esattamente pari** all'investimento iniziale.
* In questo scenario, il tasso di rendimento del progetto coincide perfettamente con il costo opportunità del capitale:
  $$IRR = r$$
* Gli investitori riceveranno esattamente il rendimento minimo richiesto per compensare il rischio assunto. La ricchezza netta degli azionisti non viene né incrementata né distrutta ($\Delta V = 0$).

#### Criteri Decisionali Pratici:
Nella realtà aziendale, di fronte a un $NPV = 0$, la decisione di intraprendere comunque l'investimento si basa su fattori strategici esterni:

* **SÌ, si investe se:**
  1. Il progetto possiede **Opzioni Reali** incorporate di natura strategica (es. l'opportunità di espandersi in un nuovo mercato o acquisire brevetti che apriranno la strada a futuri progetti ad NPV positivo, vedi [[Opzioni_Reali]]).
  2. Ha benefici intangibili essenziali (es. mantiene il posizionamento strategico sul mercato impedendo alla concorrenza di occupare una nicchia vuota, o migliora la reputazione del brand / ESG).
  3. Serve ad addestrare o riallocare risorse umane strategiche che altrimenti rimarrebbero inattive (costo opportunità del lavoro).

* **NO, non si investe se:**
  1. Vi è **razionamento del capitale** (capitale limitato) e la cassa deve essere preservata per progetti alternativi a NPV strettamente positivo ($NPV > 0$).
  2. Il progetto presenta rischi operativi occulti o asimmetrie informative non pienamente catturate nelle stime dei flussi di cassa.
  3. In assenza di sinergie strategiche o opzioni reali, è preferibile non assumersi rischi operativi inutili e restituire la cassa in eccesso agli azionisti.

---

### Q5. Preferisci ottenere un rendimento di € 100 dopo un anno su un investimento di € 1.000 o € 200 dopo un anno su un investimento di € 2.000?

#### 1. Calcolo del Rendimento Percentuale ($R$)
Entrambi i progetti di investimento offrono lo stesso tasso di rendimento annuo nominale del $10\%$:
* **Progetto A:** $R_A = \frac{100}{1000} = 10\%$
* **Progetto B:** $R_B = \frac{200}{2000} = 10\%$

#### 2. Criterio Decisionale basato sul Valore Attuale Netto (NPV)
Ipotizzando che $100€$ e $200€$ rappresentino il rendimento netto reale (quindi i flussi di cassa netti a $t=1$ sono rispettivamente $1100€$ e $2200€$), calcoliamo i rispettivi NPV in base al costo opportunità del capitale $r$:

$$NPV_A = -1000 + \frac{1100}{1+r}$$
$$NPV_B = -2000 + \frac{2200}{1+r}$$

Esaminiamo i diversi contesti finanziari:

##### Scenario 1: Assenza di Razionamento del Capitale ($r < 10\%$)
Se il costo opportunità del capitale è inferiore al rendimento del progetto (es. $r = 5\%$), entrambi i progetti sono convenienti ($NPV > 0$).
* $NPV_A = -1000 + \frac{1100}{1.05} \approx 47.62€$
* $NPV_B = -2000 + \frac{2200}{1.05} \approx 95.24€$

* **Se i progetti sono mutuamente esclusivi:** Si preferisce nettamente il **Progetto B**, in quanto genera il doppio dell'incremento di ricchezza assoluta per gli azionisti ($95.24€ > 47.62€$). La finanza aziendale insegna a massimizzare l'NPV assoluto, non il tasso percentuale o l'efficienza relativa.
* **Se i progetti non sono mutuamente esclusivi:** L'impresa dovrebbe intraprendere **entrambi** i progetti, poiché entrambi creano valore positivo.

##### Scenario 2: Presenza di Razionamento del Capitale Rigido (Budget massimo = € 1.000)
Se l'impresa ha un vincolo invalicabile di capitale pari a $1000€$, il Progetto B non è fisicamente realizzabile per mancanza di fondi. L'unica opzione fattibile è intraprendere il **Progetto A**.

##### Scenario 3: Tasso di mercato superiore ($r > 10\%$)
Se $r = 12\%$, entrambi i progetti presentano un NPV negativo e distruggerebbero ricchezza. In questo caso la scelta corretta è **rifiutare entrambi**.

---

### Q6. Puoi investire € 1.000 e ottenere un NPV di 200 oppure investire € 3.000 e ottenere un NPV di 250. Assenza di razionamento del capitale (No capital rationing). Quale sceglieresti e perché?

#### Scelta Ottimale:
In assenza di razionamento del capitale, si deve scegliere l'investimento da **€ 3.000 con un NPV di 250**.

#### Razionale Finanziario Accademico ("Stile Domenichelli"):
1. **Massimizzazione della Ricchezza Assoluta:**
   L'obiettivo cardine della Corporate Finance è la massimizzazione del valore dell'impresa e, di conseguenza, della ricchezza finanziaria netta degli azionisti in termini assoluti. 
   * Il Progetto da € 3.000 incrementa la ricchezza degli azionisti di **250€**.
   * Il Progetto da € 1.000 incrementa la ricchezza degli azionisti di **200€**.
   * Scegliendo il secondo progetto, gli azionisti saranno più ricchi di $50€$ ($250 - 200$) rispetto alla scelta del primo progetto.

2. **Perché il Profitability Index (PI) non è rilevante qui?**
   * Si calcolassimo il Profitability Index (definito come $PI = \frac{NPV}{\text{Investimento Iniziale}}$):
     * $PI_{\text{1000}} = \frac{200}{1000} = 0.20$ (20% di efficienza del capitale)
     * $PI_{\text{3000}} = \frac{250}{3000} \approx 0.083$ (8.3% di efficienza del capitale)
   * Il Progetto da € 1.000 è molto più "efficiente" nell'uso del capitale. Tuttavia, la regola del PI è utile **esclusivamente in presenza di razionamento del capitale** (quando il budget è limitato e dobbiamo selezionare la combinazione ottimale di progetti ad alta efficienza).
   * Poiché l'enunciato specifica chiaramente **"No capital rationing"**, l'impresa ha accesso illimitato ai mercati dei capitali al tasso $r$ e può finanziare qualunque progetto conveniente. Pertanto, l'efficienza relativa del capitale perde significato decisionale e l'unico criterio corretto rimane il valore attuale netto assoluto ($NPV$).

---

### Q7. Supponi di essere il financial manager di una società. Non hai future opportunità di investimento di valore. Spiega cosa significa tecnicamente "valuable opportunities of investment" e cosa dovresti fare con la cassa extra a disposizione.

#### 1. Significato Tecnico di "Valuable Opportunities of Investment":
Nella finanza aziendale quantitativa, le "opportunità di investimento di valore" si riferiscono a progetti reali (es. espansione industriale, R&D, acquisizioni strategiche) che presentano un **Valore Attuale Netto strettamente positivo**:

$$NPV = -I_0 + \sum_{t=1}^{T} \frac{CF_t}{(1+r)^t} > 0$$

Ciò significa che il tasso di rendimento atteso dei progetti interni all'impresa ($IRR$) è superiore al costo opportunità del capitale ($r$) richiesto dal mercato per investimenti con lo stesso profilo di rischio ($IRR > r$). Solo questi progetti generano valore netto per gli azionisti.

#### 2. Cosa fare con la cassa extra a disposizione?
Se l'impresa ha esaurito tutti i progetti a NPV positivo, qualsiasi cassa residua in eccesso viene definita tecnicamente **Free Cash Flow (FCF)** (Flusso di Cassa Libero). 

Trattenere questa cassa all'interno dell'impresa per investirla in progetti a NPV negativo ($NPV < 0$) o lasciarla accumulare in attività finanziarie liquide a bassissimo rendimento (es. conti di deposito che rendono meno del costo del capitale dell'impresa) **distrugge valore** ed esaspera i [[Governance_e_Problemi_di_Agenzia]] (i manager potrebbero essere tentati di utilizzare la cassa per investimenti di "trinceramento" o di puro status, vedi *Empire Building*).

La condotta finanziaria ottimale ed efficiente impone di **restituire integralmente la cassa extra in eccesso agli azionisti**.

#### Strumenti di Restituzione del Capitale:
Il Financial Manager può attuare questa restituzione attraverso due modalità principali:

1. **Distribuzione di Dividendi (Dividends):**
   * Pagamento diretto di cedole monetarie agli azionisti (ordinari o straordinari). Gli azionisti riceveranno contante che potranno liberamente reinvestire sul mercato dei capitali al proprio costo opportunità ($r$).

2. **Riacquisto di Azioni Proprie (Share Repurchases / Buybacks):**
   * L'azienda acquista le proprie azioni sul mercato aperto, riducendo il numero di azioni in circolazione. Questo aumenta la quota di possesso (e l'utile per azione futuro) degli azionisti rimanenti ed è spesso preferito per ragioni di efficienza fiscale.

In questo modo il capitale fluisce nuovamente verso l'economia reale e i mercati finanziari, dove può essere allocato in modo efficiente in altre imprese che hanno invece progetti di investimento a NPV positivo.

---

## 🏗️ Blocco 2 — Flussi di Cassa, Criteri di Valutazione e Decisioni di Investimento

### Q1. Per valutare se vale la pena intraprendere un progetto di investimento, puoi considerare i profitti o i flussi di cassa. Sei d'accordo o meno? Spiega.

**No, non sono d'accordo.** La valutazione di un investimento deve basarsi **esclusivamente sui flussi di cassa (cash flows)** e mai sui profitti contabili (utile netto).

#### Perché i profitti contabili ingannano?
1. **Principio di Competenza vs. Cassa:**
   I profitti contabili sono calcolati secondo il *principio di competenza* (*accounting accrual method*). Questo metodo include voci non monetarie, come gli ammortamenti (*depreciation*) e gli accantonamenti, che riducono i profitti teorici ma non comportano alcuna uscita di liquidità fisica. Al contrario, le vendite a credito aumentano i profitti ma non portano contante in cassa fino all'incasso reale.
   
2. **"Profit is an opinion, cash is a fact":**
   I profitti possono essere ampiamente manipolati tramite scelte contabili (scelta del metodo di ammortamento, valutazione delle rimanenze LIFO/FIFO, capitalizzazione dei costi). I flussi di cassa misurano la liquidità effettiva entrata o uscita dal conto corrente aziendale, che non è soggetta ad arbitrio contabile.

3. **Il Valore Temporale del Denaro:**
   L'attualizzazione (NPV) richiede scadenze temporali precise per ogni movimento di liquidità. Solo la cassa reale può essere prelevata, distribuita agli azionisti o reinvestita immediatamente sul mercato al costo opportunità del capitale $r$. Non è possibile "reinvestire" un profitto contabile cartaceo se la cassa non è ancora stata incassata.

Vedi anche [[Topic_3_Statement_of_Cash_Flows]] e [[Free_Cash_Flow]].

---

### Q2. Quando calcoli il flusso di cassa netto di un progetto di investimento, devi prevedere i suoi flussi di cassa su base incrementale: perché?

La stima dei flussi di cassa su **base incrementale** è un pilastro fondamentale della finanza aziendale perché risponde alla domanda cardine: *"Qual è la variazione netta della ricchezza aziendale se decidiamo di accettare questo specifico progetto?"*

#### Definizione di Flusso Incrementale:
I flussi di cassa incrementali sono calcolati come la differenza tra i flussi di cassa complessivi dell'impresa *in presenza* del progetto ($CF_{\text{With}}$) e quelli dell'impresa *in assenza* del progetto ($CF_{\text{Without}}$):

$$\Delta CF_t = CF_{\text{With}, t} - CF_{\text{Without}, t}$$

#### Perché è necessario?
* **Esclusione di flussi inevitabili:** Se un'uscita di cassa si verificherebbe in ogni caso (indipendentemente dall'accettazione del progetto), non è incrementale e non deve influenzare la decisione (es. costi generali comuni già contrattualizzati).
* **Cattura degli effetti collaterali:** Consente di includere sia i costi o benefici indiretti indotti dal progetto sulle altre linee di business (es. cannibalizzazione o sinergie), sia i costi opportunità delle risorse proprietarie già impiegate.

---

### Q3. Cosa intendiamo con l'affermazione “separare le decisioni di investimento da quelle di finanziamento”?

Il **Principio di Separazione** stabilisce che la convenienza economica di un progetto di investimento deve essere valutata **indipendentemente** dal mix di fonti finanziarie (debito vs equity) utilizzato per raccogliere i fondi necessari a coprirlo.

#### Come si applica operativamente?
1. **Flussi di Cassa Unlevered:**
   Nel calcolo dei flussi di cassa incrementali del progetto, si assume che l'impresa sia interamente finanziata tramite Equity (*all-equity firm*). Di conseguenza, **non si sottraggono mai gli oneri finanziari (interessi passivi)** o i rimborsi di quota capitale del debito dai flussi di cassa operativi del progetto.
   
2. **Il Tasso di Sconto cattura il Finanziamento:**
   Il costo e la struttura del finanziamento (compreso lo scudo fiscale sul debito) vengono incorporati interamente nel **tasso di sconto**, tipicamente rappresentato dal WACC al netto delle imposte (vedi [[Topic_7_8_CAPM_Cost_of_Capital]] e [[Struttura_del_Capitale]]).

#### Perché si fa?
Se sottraessimo gli interessi passivi dai flussi di cassa operativi e poi attualizzassimo questi flussi al WACC (che include già il costo del debito), commetteremmo un grave errore di **doppio conteggio** (*double counting*), sottovalutando pesantemente l'NPV del progetto.

---

### Q4. Chiarisci la differenza tra flusso di cassa operativo (OCF) e flusso di cassa netto (NCF) di un progetto di investimento.

Sebbene correlati, l'OCF misura la redditività monetaria della gestione operativa corrente del progetto, mentre l'NCF (o Free Cash Flow del progetto) rappresenta la liquidità effettiva totale rilasciata dal progetto agli investitori.

#### 1. Operating Cash Flow (OCF):
È la liquidità generata esclusivamente dalle vendite e dai costi operativi giornalieri legati al progetto, al netto delle imposte sul reddito operativo.
* **Formula standard (Unlevered):**
  $$OCF = (Revenues - Expenses - Depreciation) \cdot (1 - \tau_c) + Depreciation$$
  $$OCF = EBIT \cdot (1 - \tau_c) + Depreciation$$
  *dove $\tau_c$ è l'aliquota d'imposta societaria.*
* Si somma nuovamente l'ammortamento (*Depreciation*) perché è un costo contabile non monetario che ha ridotto l'utile pretasse ma non ha generato un'uscita di cassa.

#### 2. Net Cash Flow (NCF):
È il flusso di cassa finale di progetto a disposizione dei finanziatori (azionisti e creditori). Si ottiene deducendo dall'OCF gli investimenti in capitale fisso ($CapEx$) e le variazioni netta del capitale circolante ($NWC$):
* **Formula:**
  $$NCF = OCF - CapEx - \Delta NWC$$
  *   $CapEx$ (*Capital Expenditures*): Uscite di cassa per l'acquisto di asset fissi (es. attrezzature a t=0) e entrate per vendite di asset a fine vita (al netto delle tasse sulle plusvalenze).
  *   $\Delta NWC$ (*Net Working Capital Change*): Risorse monetarie temporaneamente bloccate nel ciclo commerciale (magazzino, crediti commerciali netti dei debiti commerciali, vedi [[Gestione_del_Capitale_Circolante]]).

---

### Q5. Spiega l'impatto degli effetti incidentali (incidental effects) sul flusso di cassa di un progetto di investimento.

Gli **effetti incidentali** (noti anche come *esternalità* o *effetti collaterali*) rappresentano l'impatto economico (positivo o negativo) che il nuovo progetto produce sulle attività preesistenti dell'impresa. 

Poiché la valutazione si basa sulla base incrementale (Q2), l'impatto di questi effetti deve essere rigorosamente stimato e incluso nel calcolo dell'NPV del progetto:

1. **Effetti Incidentali Negativi (Cannibalizzazione):**
   * Si verifica quando il lancio di un nuovo prodotto riduce le vendite e i relativi flussi di cassa di prodotti già venduti dall'impresa (es. Apple lancia l'iPad che cannibalizza in parte le vendite dei MacBook di fascia bassa).
   * **Impatto:** La perdita di margine di contribuzione sui vecchi prodotti è a tutti gli effetti un **costo incrementale** del nuovo progetto e va sottratta dai flussi di cassa di quest'ultimo.

2. **Effetti Incidentali Positivi (Sinergie o Complementarità):**
   * Si verifica quando il nuovo progetto incrementa le vendite o riduce i costi di altre divisioni aziendali esistenti (es. l'apertura di un nuovo parco a tema Disney aumenta le vendite di merchandising e le prenotazioni negli hotel Disney limitrofi).
   * **Impatto:** I flussi di cassa addizionali generati sulle attività esistenti sono a tutti gli effetti **benefici incrementali** e vanno sommati ai flussi di cassa del nuovo progetto.

---

### Q6. Chiarisci il concetto di costo opportunità per un progetto di investimento.

Il **costo opportunità** rappresenta il valore economico della risorsa di cui l'impresa dispone già (es. un terreno, un capannone industriale, o una licenza software) e che viene destinata all'uso esclusivo del nuovo progetto, rinunciando alla sua valorizzazione alternativa.

* **Regola Finanziaria:** Le risorse preesistenti impiegate nel progetto **non sono gratuite** solo perché l'impresa non deve sborsare liquidità oggi per acquistarle.
* **Calcolo:** Il costo opportunità è pari al **flusso di cassa netto (al netto delle imposte) generabile dal miglior impiego alternativo** della risorsa (ad esempio, il prezzo di vendita di mercato del terreno oggi o i canoni di affitto che si potrebbero riscuotere da terzi).
* **Impatto:** Questo importo deve essere inserito come un **flusso di cassa in uscita (costo) a t=0** nella scheda del progetto.

---

### Q7. Cos'è un costo affondato (sunk cost)?

Un **costo affondato** (*sunk cost*) è una spesa già sostenuta nel passato (o che l'impresa è comunque legalmente obbligata a sostenere in futuro), che **non può essere in alcun modo recuperata**, indipendentemente dalla decisione finale di accettare o rifiutare il progetto di investimento.

* **Esempi tipici:** Spese sostenute per ricerche di mercato preliminari, studi di fattibilità ingegneristica, o consulenze legali svolte prima della votazione sul progetto.
* **Regola di Trattamento:** I sunk cost **non sono incrementali** (non variano se decidiamo di avviare o meno il progetto). Pertanto, devono essere **rigorosamente esclusi** dal calcolo dei flussi di cassa e dell'NPV.
* **Bias Psicologico:** I manager spesso cadono nella *fallacia dei costi affondati*, approvando progetti fallimentari nel tentativo di "giustificare" spese passate ormai irrecuperabili. La finanza aziendale si focalizza esclusivamente sui flussi di cassa *futuri incrementali*.

---

### Q8. "L'IRR è buono quanto l'NPV come metodo per scegliere nuovi progetti di investimento." Sei d'accordo e perché?

**No, sono fortemente contrario.** Sebbene l'IRR sia ampiamente utilizzato nella prassi aziendale per la sua immediatezza espressiva (un rendimento in percentuale), esso presenta gravissimi difetti teorici e pratici che rendono l'**NPV intrinsecamente superiore**.

#### I 3 Limiti Critici dell'IRR rispetto all'NPV:

1. **Problema della Scala dei Progetti (Mutuamente Esclusivi):**
   L'IRR misura l'efficienza percentuale del capitale ma ignora la scala assoluta dell'investimento.
   * *Progetto A:* Investo 10€, ottengo un IRR del $100\%$ ($NPV \approx 10€$).
   * *Progetto B:* Investo 1.000.000€, ottengo un IRR del $20\%$ ($NPV \approx 200.000€$).
   * In assenza di razionamento, il Progetto B crea immensamente più valore rispetto ad A, ma l'IRR sceglierebbe erroneamente A.

2. **Problema degli IRR Multipli o Inesistenti:**
   Se i flussi di cassa di un progetto sono *non convenzionali* (ossia cambiano segno più di una volta nel corso del tempo, es. uscite a t=0, entrate negli anni 1-3, e grandi uscite di bonifica/smantellamento a t=4), l'equazione polinomiale dell'IRR può avere **molteplici soluzioni reali** (es. sia il 10% che il 45% azzerano l'NPV) o nessuna soluzione reale. L'NPV ha sempre una soluzione univoca e chiara per ogni tasso di sconto.

3. **Ipotesi Irrealistica sul Tasso di Reinvestimento dei Flussi Intermedi:**
   * L'IRR assume implicitamente che tutti i flussi di cassa intermedi generati dal progetto vengano reinvestiti all'interno dell'impresa allo **stesso tasso IRR** fino alla fine del progetto (ipotesi irrealistica se l'IRR è eccezionalmente alto, es. 80%).
   * L'NPV assume, molto più realisticamente, che i flussi intermedi vengano reinvestiti al **costo opportunità del capitale ($r$)**, che è il tasso di rendimento standard di mercato a parità di rischio.

Consultare [[Topic_5_NPV_Investment_Criteria#NPV vs IRR]] per la trattazione analitica.

---

### Q9. Definisci l'indice di redditività (profitability index) e spiega il contesto in cui è utile.

Il **Profitability Index (PI)** (o Indice di Redditività) misura la convenienza economica di un progetto espressa come valore creato per singola unità di capitale investito.

#### Formule:
Esistono due formulazioni equivalenti utilizzate in dottrina:
1. **PI Netto (Net Profitability Index):**
   $$PI_{\text{Netto}} = \frac{NPV}{I_0}$$
2. **PI Lordo (Gross Profitability Index):**
   $$PI_{\text{Lordo}} = \frac{\text{Valore Attuale dei Flussi di Cassa Futuri}}{I_0} = 1 + \frac{NPV}{I_0}$$
*dove $I_0$ è l'investimento iniziale netto a t=0.*

#### Regola di Accettazione Standard:
* Si accetta il progetto se $PI_{\text{Netto}} > 0$ (o $PI_{\text{Lordo}} > 1$).

#### Contesto di Utilità — Il Razionamento del Capitale:
Il PI è un criterio decisionale inutile in condizioni standard (dove l'NPV assoluto è sovrano), ma diventa **lo strumento fondamentale in presenza di Razionamento del Capitale a Breve Termine** (*capital rationing*).
* Quando un'impresa ha a disposizione un budget massimo rigido a t=0 e una moltitudine di progetti ad NPV positivo che superano tale budget complessivo, la massimizzazione del valore si ottiene selezionando il portafoglio di progetti a **maggiore efficienza allocativa**.
* **Procedura:** Si classificano tutti i progetti in ordine decrescente di Profitability Index e si approvano a cascata partendo dal PI più alto fino all'esaurimento completo del budget disponibile.

---

### Q10. Disegna e chiarisci le nozioni di NPV e IRR di un progetto di investimento.

Il legame analitico e geometrico tra NPV e IRR è rappresentato graficamente dal **Profilo dell'NPV** (*NPV Profile* o *NPV Curve*).

#### Rappresentazione Concettuale e Grafica:
La curva dell'NPV mostra l'andamento del Valore Attuale Netto (asse delle ordinate Y) al variare del tasso di sconto $r$ (asse delle ascisse X):

```text
 NPV (€)
   ▲
   │  * (NPV a tasso r = 0% = somma algebrica semplice dei CF)
   │   *
   │     *
   │       *
   │         * 
   │           *
   └─────────────*─────────────► Tasso di Sconto r (%)
   │              \
   │               * IRR (Punto di intersezione con l'asse X: NPV = 0)
   ▼                *
```

#### Elementi Chiave del Profilo:
1. **Intercetta sull'Asse Y ($r = 0$):**
   Quando il tasso di sconto è pari a zero, l'NPV is semplicemente la **somma algebrica non attualizzata** di tutti i flussi di cassa del progetto:
   $$NPV_{(r=0)} = -I_0 + \sum_{t=1}^{T} CF_t$$

2. **Pendenza della Curva:**
   Per un progetto di investimento convenzionale (uscite a t=0, entrate successive), la curva è **decrescente e convessa**. All'aumentare del tasso di sconto $r$, il valore attuale dei flussi in entrata futuri si contrae esponenzialmente, riducendo l'NPV.

3. **Intercetta sull'Asse X (Definizione di IRR):**
   Il punto esatto in cui la curva attraversa l'asse delle ascisse ($NPV = 0$) definisce il **Tasso di Rendimento Interno (IRR)**. Matematicamente, l'IRR è l'incognita che soddisfa l'equazione:
   $$NPV = -I_0 + \sum_{t=1}^{T} \frac{CF_t}{(1+IRR)^t} = 0$$

4. **Regola di Decisione Comparativa:**
   * Se il costo opportunità del capitale $r$ è posizionato a **sinistra** dell'IRR ($r < IRR$), l'NPV è positivo ($NPV > 0$) $\rightarrow$ **Si investe**.
   * Se $r$ è posizionato a **destra** dell'IRR ($r > IRR$), l'NPV è negativo ($NPV < 0$) $\rightarrow$ **Si rifiuta**.

---

### Q11. Descrivi i principali limites del payback period (periodo di recupero).

Il **Payback Period** misura il numero di anni necessari affinché i flussi di cassa operativi cumulati generati dal progetto vadano a pareggiare interamente l'esborso iniziale $I_0$. Nonostante la sua popolarità dovuta a semplicità di calcolo e immediatezza per la valutazione del rischio di liquidità, presenta 3 limiti gravissimi:

1. **Ignora il Valore Temporale del Denaro (nella versione classica):**
   Somma flussi di cassa registrati in anni diversi come se avessero lo stesso potere d'acquisto oggi. Un euro ricevuto al decimo anno ha lo stesso peso di un euro ricevuto al primo anno. 
   *(Nota: Il "Discounted Payback Period" corregge questo limite attualizzando i flussi, ma non risolve i due limiti successivi).*

2. **Ignora completamente tutti i Flussi di Cassa successivi al Cut-off:**
   Si focalizza esclusivamente sul tempo necessario per recuperare il capitale iniziale. Se il cut-off prefissato dall'azienda è 3 anni:
   * *Progetto A:* Costa 1000€, genera 500€/anno per 2 anni e poi **0€** per sempre. Viene accettato (Payback = 2 anni).
   * *Progetto B:* Costa 1000€, genera 300€/anno per 3 anni e poi **1.000.000€/anno** dal quarto anno. Viene rifiutato (Payback = 3.3 anni).
   Questo induce a scelte gravemente inefficaci, distruggendo valore a lungo termine.

3. **Soglia di Accettazione Arbitraria:**
   Il termine massimo di accettazione (es. 2 o 3 anni) viene stabilito dal management in modo del tutto discrezionale, senza alcuna relazione con il costo opportunità del capitale o con criteri di massimizzazione del valore di mercato.

Vedi [[Topic_5_NPV_Investment_Criteria#Payback Period]].

---

### Q12. Sei un manager finanziario e hai a disposizione un certo numero di possibili investimenti di valore (progetti a NPV positivo). Prima di intraprenderli, cos'altro devi decidere?

Trovare progetti a $NPV > 0$ è solo il primo passo. Un Financial Manager strategico deve affrontare altre 4 decisioni fondamentali prima dell'approvazione finale:

1. **La Decisione di Timing dell'Investimento (Investment Timing Option):**
   * Avere un NPV positivo oggi non implica che sia ottimale investire immediatamente. Potrebbe essere preferibile attendere un anno per raccogliere maggiori informazioni di mercato (riducendo l'incertezza su prezzi e costi). 
   * La decisione finale deve confrontare l'NPV dell'investimento immediato con il valore dell'**Opzione di Differimento** (vedi [[Opzioni_Reali]]).

2. **La Scala e la Flessibilità del Progetto:**
   * Bisogna valutare se il progetto può essere implementato in fasi successive (*staged investment*) per limitare il rischio finanziario iniziale, e se sono presenti **Opzioni di Abbandono** (*abandonment options*) in caso di andamento negativo del mercato, o **Opzioni di Espansione**.

3. **La Struttura Finanziaria Ottimale (Capital Structure):**
   * Occorre decidere come raccogliere la cassa necessaria ($I_0$): emettere nuovo debito (sfruttando lo scudo fiscale, vedi [[Teorema_Modigliani_Miller]]), emettere azioni o attingere interamente agli utili trattenuti. Questa scelta impatterà sul WACC complessivo e sui covenants dei creditori (vedi [[Debt_Financing_Overview]]).

4. **Il Cash Management e il Cash Budgeting a breve termine:**
   * L'avvio di molteplici progetti contemporaneamente richiede un massiccio sforzo di liquidità. Il manager deve redigere un **Cash Budget** dettagliato (vedi [[Topic_3d_Cash_Budgeting]]) per garantire che l'impresa abbia sempre linee di credito e riserve liquide disponibili a coprire non solo il CapEx, ma anche i massicci incrementi stagionali di NWC, evitando crisi di insolvenza tecnica.

---

### Q13. Commenta questa affermazione di un manager finanziario: “Tra le nostre attività, abbiamo il prodotto New Experience che ha generato flussi di cassa molto elevati, quindi l'anno prossimo investiremo in un nuovo stabilimento in Canada per incrementare quella produzione”.

Questa affermazione è finanziariamente **fallace** ed evidenzia gravi errori metodologici e comportamentali tipici di manager non allineati alla massimizzazione del valore:

#### Le 4 Criticità Finanziarie dell'Affermazione:

1. **La Fallacia della Fonte di Finanziamento:**
   Il manager decide di effettuare l'investimento semplicemente perché l'azienda ha accumulato molta cassa prodotta internamente da un altro prodotto ("New Experience"). Questo viola il principio di separazione (Q3). La disponibilità di cassa interna non rende un nuovo investimento intrinsecamente buono.
   
2. **Assenza di Valutazione Autonoma (NPV del Nuovo Progetto):**
   La costruzione di un nuovo impianto in Canada è un progetto a sé stante che deve essere valutato esclusivamente in base ai suoi **futuri flussi di cassa incrementali attesi** e al proprio costo del capitale. Il Canada presenta rischi geografici, di cambio e di mercato differenti. Se il nuovo impianto ha un $NPV < 0$, realizzarlo distruggerà ricchezza, indipendentemente da quanto sia stato profittevole "New Experience".

3. **La Trappola del Ciclo di Vita del Prodotto:**
   Il fatto che "New Experience" abbia generato molta cassa in passato indica probabilmente che si trova nella fase di maturità del suo ciclo di vita (una *Cash Cow* nel modello BCG). Reinvestire massicciamente in nuova capacità produttiva potrebbe essere un grave errore se la domanda sta per contrarsi o se il mercato è ormai saturo.

4. **Bias di Agenzia ("Empire Building"):**
   I manager tendono a non voler restituire la cassa in eccesso agli azionisti per aumentare le dimensioni dell'impresa sotto il proprio controllo (*Empire Building*), giustificando l'espansione con progetti non redditizi (a NPV negativo) pur di non ridurre il proprio status. La cassa generata da "New Experience" andrebbe restituita agli azionisti tramite dividendi o buybacks se non vi sono progetti alternativi reali con $NPV > 0$ (vedi [[Governance_e_Problemi_di_Agenzia]] e [[Topic_5_NPV_Investment_Criteria]]).

---

## 📈 Blocco 3 — Stima dei Rendimenti, Costruzione di Portafoglio e Rischio

### Q1. Come si stimano i rendimenti di un titolo azionario (stock return)?

Il rendimento di un titolo azionario può essere misurato ed analizzato sotto due profili temporali:

#### 1. Rendimento Storico (Ex-Post):
Misura il rendimento effettivo generato dal titolo in un periodo passato (es. un anno o un mese), composto da due componenti: il guadagno in conto capitale (*Capital Gain*) e i dividendi distribuiti (*Dividend Yield*):

$$R_t = \frac{P_t - P_{t-1} + D_t}{P_{t-1}}$$
*dove $P_t$ è il prezzo finale, $P_{t-1}$ è il prezzo iniziale e $D_t$ è il dividendo distribuito.*

#### 2. Rendimento Atteso (Ex-Ante):
Rappresenta il rendimento stimato che il titolo dovrebbe generare in futuro. Viene determinato principalmente tramite tre approcci metodologici:

##### A. Approccio Probabilistico (Analisi di Scenario):
Si stimano i rendimenti attesi del titolo in $M$ diversi scenari economici futuri (es. recessione, stabilità, boom), pesati per la probabilità $p_j$ di accadimento dello scenario:
$$E[R_i] = \sum_{j=1}^{M} p_j \cdot R_{i, j} \quad \text{con} \quad \sum_{j=1}^{M} p_j = 1$$

##### B. Approccio Storico (Media dei Rendimenti):
Si ipotizza che il passato sia un buon predittore del futuro. Si calcola la media aritmetica semplice dei rendimenti storici realizzati su un orizzonte di $N$ periodi:
$$E[R_i] = \frac{1}{N} \sum_{t=1}^{N} R_{i, t}$$

##### C. Approccio di Equilibrio (CAPM):
Si stima il rendimento atteso in funzione del rischio sistematico ($\beta$) del titolo stesso (vedi [[Topic_7_8_CAPM_Cost_of_Capital]]):
$$E[R_i] = R_f + \beta_i \cdot (E[R_m] - R_f)$$
*dove $R_f$ è il tasso risk-free e $(E[R_m] - R_f)$ è il premio al rischio del mercato.*

---

### Q2. Come si stima il rendimento di un portafoglio di titoli (portfolio return)?

A differenza del rischio, il rendimento atteso di un portafoglio è una grandezza lineare estremamente semplice da calcolare. È pari alla **media ponderata** dei rendimenti attesi dei singoli titoli che lo compongono, dove i pesi corrispondono alla frazione di capitale investita in ciascun titolo.

#### Formula:
Dato un portafoglio composto da $n$ titoli, il rendimento atteso $E[R_p]$ è:

$$E[R_p] = \sum_{i=1}^{n} w_i \cdot E[R_i] = w_1 E[R_1] + w_2 E[R_2] + \dots + w_n E[R_n]$$

#### Vincolo dei Pesi:
La somma dei pesi di portafoglio deve essere tassativamente pari a $1$ (ovvero al $100\%$ del capitale investito):
$$\sum_{i=1}^{n} w_i = 1$$
*(Nota: Un peso $w_i > 0$ indica una posizione d'acquisto "Long", mentre un peso $w_i < 0$ indica una vendita allo scoperto o "Short").*

---

### Q3. Spiega la nozione di rischio di un titolo e come può essere misurata.

Nella moderna teoria di portafoglio, la nozione di **rischio** rappresenta l'incertezza o la variabilità dei rendimenti effettivi di un'attività finanziaria rispetto al suo valore atteso (rendimento medio). Maggiore è la dispersione dei rendimenti storici o futuri attorno alla media, maggiore è il rischio associato al titolo.

#### Misurazione del Rischio Totale:
Il rischio totale di un singolo titolo viene quantificato tramite indicatori statistici di dispersione: la **Varianza ($\sigma^2$)** e la **Deviazione Standard ($\sigma$)** (nota anche come *volatilità*).

1. **Varianza Storica ($\sigma^2$):**
   Misura la media dei quadrati degli scostamenti dei singoli rendimenti rispetto alla media:
   $$\sigma^2 = \frac{1}{N-1} \sum_{t=1}^{N} (R_t - E[R])^2$$

2. **Deviazione Standard Storica ($\sigma$):**
   È la radice quadrata della varianza. Viene preferita nella pratica perché è espressa nella stessa unità di misura dei rendimenti (in percentuale):
   $$\sigma = \sqrt{\frac{1}{N-1} \sum_{t=1}^{N} (R_t - E[R])^2$$

Un titolo con $\sigma = 25\%$ è statisticamente molto più rischioso di un titolo con $\sigma = 8\%$, poiché presenta una probabilità molto più elevata di registrare pesanti scostamenti negativi (o positivi) rispetto alle attese.

Vedi [[Topic_6_Risk_and_Return]].

---

### Q4. Chiarisci il concetto di covarianza.

La **covarianza** ($\sigma_{ij}$ o $Cov(R_i, R_j)$) è una misura statistica che indica la direzione e l'intensità della relazione lineare tra i rendimenti di due diverse attività finanziarie nel tempo. Risponde alla domanda: *"I due titoli tendono a muoversi in sintonia o in direzioni opposte?"*

#### Formula (Probabilistica):
$$Cov(R_i, R_j) = E\Big[\big(R_i - E[R_i]\big)\big(R_j - E[R_j]\big)\Big] = \sum_{k=1}^{M} p_k \cdot (R_{i, k} - E[R_i])(R_{j, k} - E[R_j])$$

#### Interpretazione del Segno della Covarianza:
1. **Covarianza Positiva ($Cov(R_i, R_j) > 0$):**
   I rendimenti dei due titoli tendono a muoversi nella **stessa direzione**. Quando il titolo $A$ registra performance superiori alla sua media, anche il titolo $B$ tende ad essere sopra la media.
   
2. **Covarianza Negativa ($Cov(R_i, R_j) < 0$):**
   I rendimenti si muovono in **direzioni opposte**. Quando il titolo $A$ sale, il titolo $B$ tende a scendere. Questa è la condizione ideale per ridurre il rischio complessivo di un portafoglio (diversificazione).
   
3. **Covarianza Nulla ($Cov(R_i, R_j) = 0$):**
   Non vi è alcuna relazione lineare tra i rendimenti dei due titoli. I loro movimenti sono linearmente indipendenti.

---

### Q5. Descrivi il concetto di correlazione (coefficiente di correlazione).

Il **coefficiente di correlazione lineare di Pearson ($\rho_{ij}$ o $Corr(R_i, R_j)$)** è la versione **standardizzata** della covarianza. 

Poiché la covarianza risente delle unità di misura dei rendimenti, essa può assumere valori illimitati (es. $+0.0045$), rendendo difficile valutarne la reale intensità. Standardizzando la covarianza tramite il prodotto delle deviazioni standard dei due titoli, si ottiene un coefficiente puro, facilmente interpretabile.

#### Formula:
$$\rho_{ij} = \frac{Cov(R_i, R_j)}{\sigma_i \cdot \sigma_j}$$

#### Proprietà e Campo di Esistenza:
Il valore di $\rho_{ij}$ è tassativamente compreso nell'intervallo:
$$-1 \le \rho_{ij} \le +1$$

#### Interpretazione dei Valori Limite:
* **$\rho_{ij} = +1$ (Correlazione Positiva Perfetta):**
  I due titoli si muovono in modo perfettamente identico e proporzionale. Non si ottiene alcun beneficio di riduzione del rischio tramite la diversificazione (la deviazione standard del portafoglio sarà la semplice media ponderata delle deviazioni standard).
  
* **$\rho_{ij} = -1$ (Correlazione Negativa Perfetta):**
  I due titoli si muovono in modo perfettamente opposto. È teoricamente possibile azzerare completamente la volatilità del portafoglio ($\sigma_p = 0$) selezionando opportunamente i pesi (vedi Q10).
  
* **$\rho_{ij} = 0$ (Assenza di Correlazione):**
  I movimenti sono indipendenti. Si ottengono ottimi benefici di diversificazione per abbattere la volatilità di portafoglio.

---

### Q6. Crea una matrice per calcolare la varianza di un portafoglio a 3 titoli (3-stock portfolio).

Per calcolare la varianza di un portafoglio composto da 3 titoli ($A, B, C$) con rispettivi pesi $w_A, w_B, w_C$ e deviazioni standard $\sigma_A, \sigma_B, \sigma_C$, si utilizza la **matrice di covarianza** pesata.

La varianza del portafoglio ($\sigma_p^2$) è pari alla somma di tutti gli elementi all'interno della seguente matrice $3 \times 3$:

$$\begin{array}{c|ccc}
& \mathbf{w_A} & \mathbf{w_B} & \mathbf{w_C} \\
\hline
\mathbf{w_A} & w_A^2 \sigma_A^2 & w_A w_B \sigma_{AB} & w_A w_C \sigma_{AC} \\
\mathbf{w_B} & w_B w_A \sigma_{BA} & w_B^2 \sigma_B^2 & w_B w_C \sigma_{BC} \\
\mathbf{w_C} & w_C w_A \sigma_{CA} & w_C w_B \sigma_{CB} & w_C^2 \sigma_C^2 \\
\end{array}$$

#### Scomposizione della Matrice:
* **Elementi Diagonali (Varianze dei singoli titoli):**
  Rappresentano il contributo al rischio dato dalla volatilità individuale di ciascun asset:
  $$w_A^2 \sigma_A^2, \quad w_B^2 \sigma_B^2, \quad w_C^2 \sigma_C^2$$
* **Elementi Fuori Diagonale (Covarianze bilaterali):**
  Rappresentano l'interazione tra le coppie di titoli. Poiché la matrice è simmetrica ($Cov(R_i, R_j) = Cov(R_j, R_i)$ ovvero $\sigma_{ij} = \sigma_{ji}$), questi termini si sommano a due a due.

#### Formula Estesa Risolutiva:
$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + w_C^2 \sigma_C^2 + 2 w_A w_B \sigma_{AB} + 2 w_A w_C \sigma_{AC} + 2 w_B w_C \sigma_{BC}$$

*(Nota: Sostituendo la relazione $\sigma_{ij} = \rho_{ij} \sigma_i \sigma_j$, la formula può essere scritta anche in funzione dei coefficienti di correlazione $\rho$).*

---

### Q7. Spiega e dai esempi di rischio specifico (specific/idiosyncratic risk) e rischio sistematico (systematic/market risk). Sono entrambi diversificabili?

Il rischio totale di un'attività finanziaria ($\sigma$) può essere scomposto in due componenti distinte:

#### 1. Rischio Specifico (noto anche come *Idiosincratico*, *Unsystematic* o *Diversificabile*):
* **Definizione:** È la quota di rischio legata a fattori microeconomici ed eventi straordinari che colpiscono **esclusivamente la singola impresa emittente** o, al massimo, la sua stretta nicchia industriale.
* **Esempi:**
  * Un incendio doloso che distrugge il magazzino centrale dell'impresa.
  * Le dimissioni improvvise e inaspettate del CEO o del team di sviluppo chiave.
  * Il fallimento dei test clinici di un farmaco rivoluzionario per un'azienda Biotech.
  * Una causa legale per violazione di brevetto intentata contro la società.
* **Diversificabilità: SÌ.** Questo rischio può essere **completamente eliminato** inserendo un numero sufficiente di titoli (in media 20-30) all'interno del portafoglio. Gli eventi negativi specifici di un'azienda saranno statisticamente compensati da eventi positivi specifici di un'altra.

#### 2. Rischio Sistematico (noto anche come *Rischio di Mercato* o *Non Diversificabile*):
* **Definizione:** È la quota di rischio legata a macro-variabili economiche e geopolitiche che influenzano contemporaneamente **tutti i titoli scambiati sul mercato**, sebbene con intensità diverse.
* **Esempi:**
  * Un innalzamento dei tassi di interesse di riferimento da parte della Federal Reserve / BCE.
  * Uno shock petrolifero o energetico globale che impenna i costi di produzione di tutte le industrie.
  * Una recessione macroeconomica globale o una pandemia.
  * Lo scoppio di un conflitto bellico internazionale.
* **Diversificabilità: NO.** Questo rischio **non può essere eliminato** in alcun modo per portafogli composti da sole attività risidiose, poiché tutte le imprese registrano performance negative di fronte a shock sistemici del mercato. L'unica difesa è la copertura con derivati o la riduzione dell'esposizione azionaria a favore del risk-free rate.

---

### Q8. Disegna la relazione tra la deviazione standard del portafoglio e il numero di titoli.

La riduzione del rischio di portafoglio all'aumentare della diversificazione è illustrata dal classico grafico della **diversificazione di portafoglio**:

#### Rappresentazione Grafica:
```text
Deviazione Standard
del Portafoglio σ_p (%)
   ▲
   │* 
   │  *   ◄─── Rischio Totale del singolo titolo a N=1
   │    *
   │      * 
   │        *  ◄─── Area del RISCHIO SPECIFICO (idiosincratico)
   │          *    (completamente azzerato dalla diversificazione)
   │            *
   │──────────────*──────────────────*────────────────────► Limite Asintotico
   │               *                 * 
   │                 * * * * * * * * *  ◄─── RISCHIO SISTEMATICO
   │                                         (Non diversificabile)
   └──────────────────────────────────────────────────────► Numero di Titoli N
   0              10                20                    30
```

#### Spiegazione Finanziaria:
1. **Andamento decrescente:**
   Aggiungendo titoli non perfettamente correlati, la volatilità complessiva del portafoglio $\sigma_p$ si riduce drasticamente all'inizio (il beneficio marginale della diversificazione è massimo tra $N = 1$ e $N = 15$).
   
2. **Eliminazione del Rischio Specifico:**
   All'aumentare di $N$ verso l'infinito ($N \rightarrow \infty$), la componente di rischio specifico (idiosincratico) si contrae fino ad **azzerarsi del tutto**.
   
3. **Il Pavimento del Rischio Sistematico:**
   La curva non raggiunge mai lo zero. Essa tende asintoticamente ad un limite inferiore positivo che rappresenta il **Rischio Sistematico del Mercato**. Questo "pavimento" corrisponde alla covarianza media tra tutti i titoli inclusi nel mercato finanziario.

---

### Q9. Cosa misura il Beta? Come si determina?

Il **Beta ($\beta$)** è l'indicatore fondamentale del rischio sistematico di un'attività finanziaria.

#### 1. Cosa misura?
* Misura la **sensibilità** del rendimento atteso di un singolo titolo rispetto alle oscillazioni del mercato finanziario nel suo complesso (rappresentato dal portafoglio di mercato).
* Indica quanto il titolo sia "reattivo" o rischioso rispetto alla media del mercato (che ha per definizione $\beta_m = 1$):
  * **$\beta_i = 1$ (Titolo Neutrale):** Il titolo oscilla in media esattamente in sintonia con il mercato.
  * **$\beta_i > 1$ (Titolo Aggressivo):** Il titolo amplifica i movimenti del mercato (es. se $\beta = 1.5$, e il mercato sale del $10\%$, il titolo sale in media del $15\%$; se il mercato crolla del $10\%$, il titolo crolla del $15\%$). Tipico dei settori tecnologici, finanziari o ciclici.
  * **$\beta_i < 1$ (Titolo Difensivo):** Il titolo attenua i movimenti del mercato (es. se $\beta = 0.6$, e il mercato crolla del $10\%$, il titolo scende in media del $6\%$). Tipico dei settori di pubblica utilità (*utilities*), alimentari o farmaceutici.

#### 2. Come si determina?
Matematicamente, il Beta del titolo $i$ si calcola come il rapporto tra la covarianza tra il rendimento del titolo ($R_i$) e il rendimento del portafoglio di mercato ($R_m$), e la varianza del mercato stesso ($\sigma_m^2$):

$$\beta_i = \frac{Cov(R_i, R_m)}{\sigma_m^2} = \rho_{i, m} \cdot \frac{\sigma_i}{\sigma_m}$$

*   **Pendenza della Retta:** Geometricamente, il $\beta$ rappresenta il coefficiente angolare della regressione lineare dei rendimenti del titolo sul rendimento del mercato (nota come *Characteristic Line* o retta del *Market Model*).

---

### Q10. Spiega questa affermazione: teoricamente il rischio di un portafoglio di titoli rischiosi potrebbe essere pari a zero.

Questa affermazione è **teoricamente corretta**, ma si basa su una condizione puramente accademica e quasi impossibile da riscontrare nella realtà empirica: che i titoli in portafoglio siano caratterizzati da una **correlazione negativa perfetta ($\rho = -1$)**.

#### Dimostrazione Matematica (Caso a 2 Titoli):
Consideriamo due titoli rischiosi $A$ e $B$ con pesi $w_A$ e $w_B = 1 - w_A$, e volatilità $\sigma_A$ e $\sigma_B$.
Se la correlazione $\rho_{AB} = -1$, la formula della varianza di portafoglio diventa un quadrato perfetto:

$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{AB} \sigma_A \sigma_B$$
$$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 - 2 w_A w_B \sigma_A \sigma_B = (w_A \sigma_A - w_B \sigma_B)^2$$

Estraendo la radice quadrata, la deviazione standard del portafoglio è:
$$\sigma_p = |w_A \sigma_A - w_B \sigma_B|$$

#### Calcolo dei pesi per azzerare il rischio ($\sigma_p = 0$):
Impostando la volatilità di portafoglio pari a zero, risolviamo per il peso $w_A$:
$$w_A \sigma_A - (1 - w_A) \sigma_B = 0 \implies w_A (\sigma_A + \sigma_B) = \sigma_B$$

$$w_A^* = \frac{\sigma_B}{\sigma_A + \sigma_B} \quad \text{e} \quad w_B^* = \frac{\sigma_A}{\sigma_A + \sigma_B}$$

Utilizzando queste precise proporzioni di investimento, le fluttuazioni opposte dei due titoli si **neutralizzano perfettamente ed istantaneamente** in ogni scenario di mercato, garantendo un rendimento certo e privo di qualsiasi volatilità ($\sigma_p = 0$).

#### Limite Empirico:
Nel mondo reale è impossibile trovare azioni con $\rho = -1$. Tutte le imprese operano nello stesso sistema economico globale e sono soggette a fattori di rischio sistematico comuni, che impediscono al coefficiente di correlazione di raggiungere stabilmente il valore limite di $-1$.

---

### Q11. "Il rischio di un portafoglio ben diversificato dipende solo dai beta dei titoli inclusi in esso". Vero o falso? Perché?

L'affermazione è **VERA**.

#### Spiegazione Teorica:
In un portafoglio ampiamente e correttamente diversificato (quando il numero di titoli $N$ tende all'infinito), il rischio specifico (idiosincratico) di ciascuna azione viene interamente ridotto a zero grazie alla compensazione reciproca (diversificazione).

Di conseguenza, il rischio totale residuo del portafoglio coincide unicamente con il **rischio sistematico (di mercato)** aggregato.

Poiché il rischio sistematico di ciascuna singola azione inclusa nel portafoglio è misurato esclusivamente dal suo coefficiente **Beta ($\beta_i$)**, la rischiosità complessiva del portafoglio diversificato sarà funzione lineare dei singoli beta.

#### Relazione Matematica:
* Il Beta del portafoglio sarà la media ponderata dei singoli beta:
  $$\beta_p = \sum_{i=1}^{n} w_i \cdot \beta_i$$
* La volatilità (deviazione standard) del portafoglio ben diversificato sarà pari al beta del portafoglio moltiplicato per la volatilità del mercato:
  $$\sigma_p \approx \beta_p \cdot \sigma_m$$

Pertanto, la deviazione standard del portafoglio dipende unicamente dai pesi e dai Beta dei titoli in esso inclusi.

---

### Q12. "Se possiedo un singolo titolo, allora il suo rischio è rappresentato dal suo beta". Vero o falso? Perché?

L'affermazione è **FALSISSIMA**.

#### Spiegazione Finanziaria:
* Il **Beta ($\beta$)** misura unicamente il **rischio sistematico (non diversificabile)** di un titolo, ovvero la sua sensibilità ai movimenti del mercato. Il beta assume che l'investitore sia già perfettamente diversificato (e che quindi non subisca alcun rischio specifico).
* Se un investitore commette l'errore di possedere un **singolo titolo** (assenza totale di diversificazione), egli è esposto al **rischio totale** dell'impresa, il quale comprende sia il rischio sistematico (macroeconomico) sia il rischio specifico (es. fallimento aziendale, incendi, scandali).
* La misura corretta e reale del rischio per un investitore non diversificato che detiene un unico titolo è la **deviazione standard ($\sigma$)** del rendimento del titolo, che cattura la volatilità globale dell'asset.

#### Esempio Numerico:
Un'azienda Biotech ad altissimo rischio specifico (es. start-up che sperimenta un singolo farmaco) potrebbe avere un $\beta = 0.8$ (sensibilità di mercato inferiore alla media) ma una deviazione standard del $\sigma = 75\%$ (rischio totale enorme dovuto alla probabilità del 90% di fallire i test). Detenendo solo questo titolo, l'investitore subisce un rischio del 75%, non dello 0.8.

---

## 📊 Blocco 4 — Modello CAPM, Frontiera Efficiente e Costo del Capitale

### Q1. Disegna e descrivi la frontiera efficiente di Markowitz.

La **Frontiera Efficiente di Markowitz** rappresenta le combinazioni ottimali di attività finanziarie rischiose che offrono il massimo rendimento atteso possibile per ogni livello di rischio (misurato dalla deviazione standard) o, equivalentemente, il minimo livello di rischio possibile per ogni livello di rendimento atteso.

#### Descrizione e Rappresentazione Grafica:
Se tracciamo tutti i portafogli rischiosi possibili composti dagli asset presenti sul mercato (es. combinando centinaia di azioni), essi giacciono all'interno di un'area geometrica chiamata **"Proiettile di Markowitz"** (*Markowitz Bullet*).

```text
 Rendimento Atteso
 E[R_p] (%)
   ▲
   │              * * * * * (Frontiera Efficiente: porzione superiore)
   │            *
   │          * 
   │        *  ◄─── Portafoglio a Varianza Minima Globale (MVP)
   │        *
   │          *
   │            *
   │              * * * * * (Porzione inefficiente: porzione inferiore)
   └───────────────────────────────────► Rischio / Volatilità σ_p (%)
   0
```

#### Elementi Chiave del Modello:
1. **Minimum Variance Portfolio (MVP):**
   Il punto più a sinistra della parabola rappresenta il portafoglio a **varianza minima assoluta**. Nessuna combinazione di titoli rischiosi può avere un rischio inferiore a quello dell'MVP.
   
2. **La Frontiera Efficiente:**
   È unicamente la **porzione superiore del bordo della parabola** (partendo dall'MVP verso l'alto). I portafogli situati in questa sezione sono dominanti rispetto a quelli della porzione inferiore (a parità di rischio, offrono un rendimento superiore).
   
3. **Razionalità dell'Investitore:**
   Nessun investitore razionale acquisterà portafogli situati all'interno della parabola o sulla metà inferiore (porzione inefficiente), poiché a parità di rischio è possibile salire verticalmente per ottenere un rendimento superiore sulla Frontiera Efficiente.

---

### Q2. Portafogli efficienti e possibilità di prestare e prendere in prestito al tasso risk-free (lending/borrowing): mostra e spiega le scelte fattibili di un investitore.

L'introduzione di un'**attività priva di rischio** ($R_f$) che offre un rendimento certo e ha volatilità pari a zero ($\sigma_f = 0$) modifica radicalmente la frontiera efficiente classica. Gli investitori possono ora combinare l'attività priva di rischio con portafogli di attività rischiose.

#### Geometria della Scelta — La retta CML (Capital Market Line):
Geometricamente, le possibili combinazioni tra il tasso risk-free e un portafoglio rischioso tracciano delle rette che partono da $R_f$ sull'asse delle ordinate. 
La retta ottimale in assoluto è la **Capital Market Line (CML)**, ovvero la linea che parte da $R_f$ ed è **tangente** alla frontiera efficiente dei soli titoli rischiosi nel punto **M** (il Portafoglio di Mercato).

```text
 Rendimento
 E[R_p] (%)
   ▲            / (CML)
   │           /     * * * (Frontiera di Markowitz)
   │          /     *
   │         /     *
   │        / ◄── Tangenza nel Portafoglio di Mercato (M)
   │       /   *
   │      /   *
   │    R_f
   └─────┴─────────────────────────────► Volatilità σ_p (%)
   0
```

#### Le 4 Scelte Fattibili dell'Investitore sulla CML:
L'investitore razionale sceglierà esclusivamente un punto situato lungo la retta CML, allocando il proprio capitale tra il titolo privo di rischio ($R_f$) e il portafoglio rischioso ottimale ($M$):

1. **Punto su $R_f$ (Investimento al 100% nel risk-free):**
   L'investitore destina l'intero capitale al titolo privo di rischio (es. titoli di Stato a breve termine). Volatilità zero, rendimento pari a $R_f$.
   
2. **Punti tra $R_f$ e $M$ (Risk-Free Lending / Prestito):**
   L'investitore è moderatamente conservatore. Investe una frazione $w$ in $R_f$ e $(1-w)$ in $M$. Prestare denaro significa acquistare titoli di Stato a basso rendimento per mitigare il rischio totale del portafoglio, posizionandosi sulla CML a sinistra di $M$.
   
3. **Punto su $M$ (Portafoglio di Mercato al 100%):**
   L'investitore alloca l'intero capitale nel paniere rischioso diversificato $M$. Il rischio è pari a $\sigma_m$ e il rendimento atteso è $E[R_m]$.
   
4. **Punti a destra di $M$ (Risk-Free Borrowing / Indebitamento con Leva):**
   L'investitore è aggressivo. Prende a prestito capitale aggiuntivo al tasso privo di rischio $R_f$ (indebitamento a leva) e lo investe interamente in $M$, acquistando una quota del portafoglio di mercato superiore al $100\%$ del proprio capitale proprio. Questo posiziona l'investitore sulla CML a destra di $M$, amplificando linearmente sia il rendimento atteso sia la volatilità del portafoglio.

---

### Q3. Descrivi le assunzioni del CAPM (Capital Asset Pricing Model) e scrivi la relativa formula.

Il CAPM è un modello di equilibrio generale dei prezzi delle attività finanziarie sviluppato da William Sharpe, John Lintner e Jan Mossin. Per isolare il legame puro tra rischio e rendimento, si basa su 6 assunzioni semplificatrici estremamente rigorose:

#### Le 6 Assunzioni del CAPM:
1. **Investitori Razionali ed Avversi al Rischio:**
   Tutti gli investitori ottimizzano i propri portafogli secondo la teoria di Markowitz (massimizzano il rendimento atteso per un dato livello di varianza).
   
2. **Orizzonte Temporale Singolo Periodo:**
   Tutti gli investitori pianificano i propri investimenti per il medesimo orizzonte temporale futuro (es. 1 anno), dopodiché liquidano le posizioni.
   
3. **Mercati dei Capitali Perfetti ed Efficienti:**
   Non esistono costi di transazione, non vi sono imposte (tasse sui capital gain o dividendi), e tutte le attività finanziarie sono infinitamente divisibili (è possibile acquistare anche frazioni di un'azione).
   
4. **Accesso Illimitato al Risk-Free Rate:**
   Tutti gli investitori possono prestare o prendere a prestito qualsiasi ammontare di capitale al medesimo tasso privo di rischio $R_f  senza vincoli o differenziali di tasso.
   
5. **Aspettative Omogenee:**
   Tutti gli investitori hanno accesso alle stesse informazioni contemporaneamente e concordano perfettamente sulle stime dei rendimenti attesi, delle varianze e delle covarianze di tutte le attività finanziarie.
   
6. **Investitori Price-Taker (Assenza di Potere di Mercato):**
   Nessun singolo investitore o istituzione è abbastanza grande da influenzare, con i propri ordini di acquisto o vendita, il prezzo di mercato dei titoli.

#### La Formula del CAPM:
Sotto queste assunzioni, in equilibrio, il rendimento atteso (e richiesto) di un qualsiasi titolo rischioso $i$ è funzione lineare unicamente del suo rischio sistematico ($\beta_i$):

$$E[R_i] = R_f + \beta_i \cdot \big(E[R_m] - R_f\big)$$

*   $R_f$: Rendimento del titolo privo di rischio.
*   $\beta_i$: Coefficiente Beta del titolo (misura il rischio sistematico).
*   $E[R_m]$: Rendimento atteso del portafoglio di mercato.
*   $(E[R_m] - R_f)$: Premio al rischio di mercato (*Equity Risk Premium*).

---

### Q4. Scrivi e spiega la Security Market Line (SML).

La **Security Market Line (SML)** è la rappresentazione grafica del modello CAPM (Q3). Essa esprime visivamente la relazione di equilibrio tra il rendimento atteso di un'attività finanziaria e il suo rischio sistematico ($\beta$).

#### Rappresentazione Grafica:
```text
 Rendimento Atteso
 E[R_i] (%)
   ▲                   / (SML)
   │                  /   
   │                 / * Punto del Portafoglio di Mercato (Beta = 1, E[R_m])
   │                / 
   │               /   
   │              /   
   │            R_f (Intercetta sull'asse Y: Beta = 0)
   └────────────┴──────► Rischio Sistematico (Beta β)
   0            1.0
```

#### Elementi Chiave della SML:
1. **Intercetta sull'Asse Y ($Beta = 0$):**
   Un'attività con rischio sistematico pari a zero ha un rendimento richiesto pari al tasso privo di rischio $R_f$.
   
2. **Pendenza della Retta:**
   La pendenza della SML è esattamente pari al **premio per il rischio di mercato** $(E[R_m] - R_f)$. All'aumentare di ogni unità di beta, il mercato richiede un incremento di rendimento pari all'Equity Risk Premium.
   
3. **Criterio di Valutazione dei Titoli (Sottovalutazione vs Sopravvalutazione):**
   La SML funge da benchmark di equilibrio. Se un titolo viene scambiato sul mercato a prezzi che non riflettono l'equilibrio:
   * **Titolo al di sopra della SML ($\alpha_i > 0$):**
     Il titolo offre un rendimento atteso superiore a quello richiesto per il suo livello di rischio. Il titolo è **sottovalutato** (*underpriced*). È una grande opportunità di acquisto.
   * **Titolo al di sotto della SML ($\alpha_i < 0$):**
     Il titolo offre un rendimento insufficiente rispetto al rischio sistematico assunto. Il titolo è **sopravvalutato** (*overpriced*). Deve essere venduto.

---

### Q5. Commenta vantaggi e svantaggi del CAPM.

Il CAPM è il pilastro centrale della finanza aziendale moderna, ma è anche oggetto di intense discussioni accademiche.

#### I Vantaggi del CAPM:
1. **Semplicità ed Intuizione Pratica:**
   Collega il rendimento richiesto (costo dell'equity) ad un'unica variabile chiave facilmente calcolabile: il coefficiente Beta.
   
2. **Focalizzazione sul Rischio Sistematico:**
   È l'unico modello che formalizza il principio secondo cui il mercato remunera unicamente il rischio che non può essere eliminato tramite la diversificazione (rischio sistematico). Il rischio specifico non viene pagato perché l'investitore può azzerarlo a costo zero diversificando.
   
3. **Standard Industriale:**
   È universalmente accettato come il metodo di riferimento per stimare il costo del capitale netto ($r_e$) nel calcolo del WACC per la valutazione dei progetti e delle imprese.

#### Gli Svantaggi e Limiti del CAPM:
1. **Assunzioni Fortemente Irrealistiche:**
   Ipotizza mercati senza tasse, senza costi di transazione, e la possibilità di indebitarsi allo stesso tasso risk-free delle banche centrali, condizioni palesemente violate nel mondo reale.
   
2. **La Non-Osservabilità del Portafoglio di Mercato (Critica di Roll):**
   Il CAPM richiede l'uso del "Portafoglio di Mercato" ($M$) globale, il quale dovrebbe includere *tutte* le attività rischiose mondiali (non solo azioni quotate, ma anche immobili, oro, capitale umano, arte). Poiché questo portafoglio è impossibile da osservare, si usano indici di borsa (es. S&P 500) che sono proxy imperfette. Roll ha dimostrato che se la proxy usata non è perfettamente efficiente in termini di media-varianza, i risultati del CAPM perdono validità matematica.
   
3. **Instabilità del Beta:**
   Il coefficiente Beta viene stimato su dati storici ed è altamente instabile, variando in base all'orizzonte temporale scelto (es. 2 anni vs 5 anni) e alla frequenza dei dati (giornalieri vs mensili).
   
4. **Modello a Singolo Fattore Superato:**
   Ricerche empiriche (es. Fama e French) hanno dimostrato che il solo Beta non spiega pienamente le differenze di rendimento tra i titoli. Altri fattori sistematici, come la dimensione aziendale (*Size*), il rapporto book-to-market (*Value*) e il trend recente dei prezzi (*Momentum*), catturano anomalie che il CAPM ignora.

---

### Q6. Mostra alcuni metodi alternativi per calcolare il tasso di rendimento atteso di un titolo azionario.

Oltre al modello CAPM, la teoria finanziaria offre validi metodi alternativi per stimare il rendimento richiesto o atteso di un'azione:

#### 1. Dividend Discount Model (DDM) o Modello di Gordon (Costo dell'Equity Implicito):
Deriva direttamente dal modello di valutazione dei flussi di cassa scontati applicato ai dividendi stabili, ipotizzando una crescita costante ad un tasso $g$:

$$E[R_i] = \frac{D_1}{P_0} + g$$

*   $D_1$: Dividendo atteso per il prossimo anno.
*   $P_0$: Prezzo corrente dell'azione sul mercato.
*   $g$: Tasso di crescita annuo perpetuo dei dividendi.
* *Vantaggio:* Si basa su dati fondamentali dell'impresa (dividendi e tasso di crescita degli utili), molto utile per utility e aziende stabili.

#### 2. Arbitrage Pricing Theory (APT) e Modelli Multifattoriali (Fama-French):
Superano il limite del CAPM a singolo fattore ipotizzando che il rendimento risponda a molteplici fattori di rischio macroeconomico o fondamentale.
* **Modello a 3 Fattori di Fama-French:**
  $$E[R_i] = R_f + \beta_{i, m} \cdot (E[R_m] - R_f) + \beta_{i, \text{SMB}} \cdot \text{SMB} + \beta_{i, \text{HML}} \cdot \text{HML}$$
  *   $\text{SMB}$ (*Small Minus Big*): Premio al rischio legato alla dimensione aziendale (le piccole imprese tendono a sovraperformare le grandi).
  *   $\text{HML}$ (*High Minus Low*): Premio al rischio legato al valore contabile/valore di mercato (le imprese "value" con alto book-to-market sovraperformano le imprese "growth").

#### 3. Metodo dell'Inverso del Price-to-Earnings (Earnings Yield):
Utilizzato nella pratica da molti analisti fondamentali per stime rapide di lungo termine per aziende stabili con bassi tassi di crescita:

$$E[R_i] \approx \frac{E_1}{P_0} = \frac{1}{P/E}$$

---

### Q7. Commenta questa affermazione: "Tutti i titoli negoziati in un mercato finanziario sono influenzati dal rischio sistematico nello stesso modo".

L'affermazione è **completamente FALSA**.

#### Spiegazione Finanziaria:
Sebbene il rischio sistematico (macroeconomico) colpisca contemporaneamente e inevitabilmente **tutti** i titoli scambiati sul mercato (nessun titolo rischioso può esserne del tutto immune), la misura e l'intensità con cui ciascun titolo risponde a questi shock è **profondamente diversa**.

L'intensità della reazione di un singolo titolo rispetto alle oscillazioni del mercato è catturata e misurata specificamente dal suo coefficiente **Beta ($\beta$)** (vedi Blocco 3, Q9).

* **Titoli fortemente influenzati ($\beta > 1.5$):** Titoli ciclici e ad alta tecnologia (es. Nvidia, Tesla). Se le condizioni economiche generali peggiorano o i tassi salgono, subiscono contrazioni drammatiche del prezzo.
* **Titoli debolmente influenzati ($\beta < 0.6$):** Titoli difensivi di prima necessità o utilities (es. Nestlé, Enel). Pur subendo lo shock di mercato, la loro domanda commerciale rimane stabile, limitando la fluttuazione del prezzo delle azioni.

Dire che risentono del rischio sistematico "nello stesso modo" equivarrebbe a dire che tutte le azioni hanno $\beta = 1$, il che è smentito da qualsiasi evidenza empirica.

---

### Q8. Come puoi stimare empiricamente il beta di un'azione?

La stima empirica del Beta si effettua applicando l'analisi di regressione lineare sui dati storici dei rendimenti.

#### Procedura Operativa in 4 Fasi:

1. **Raccolta Dati:**
   Si estraggono le serie storiche dei prezzi del titolo ($P_{i, t}$), di un indice di mercato rappresentativo ($P_{m, t}$, es. S&P 500 o FTSE MIB) e del tasso risk-free ($R_{f, t}$) per un determinato periodo (lo standard accademico è **5 anni con dati a frequenza mensile**, o **2 anni con dati a frequenza settimanale**).

2. **Calcolo dei Rendimenti Periodici:**
   Si convertono i prezzi in rendimenti percentuali periodici sia per il titolo ($R_{i, t}$) sia per il mercato ($R_{m, t}$).

3. **Regressione Lineare OLS (Market Model):**
   Si effettua una regressione lineare dei rendimenti in eccesso del titolo sui rendimenti in eccesso del mercato:
   $$\big(R_{i, t} - R_{f, t}\big) = \alpha_i + \beta_i \cdot \big(R_{m, t} - R_{f, t}\big) + \epsilon_{i, t}$$
   *   $\beta_i$ (Coefficiente angolare): È il beta storico stimato.
   *   $\alpha_i$ (Intercetta): Misura la performance anomala del titolo rispetto all'equilibrio (Alpha di Jensen).
   *   $\epsilon_{i, t}$: Errore residuo che cattura il rischio specifico.

4. **Formula Statistica Risolutiva:**
   $$\beta_i = \frac{Cov(R_i, R_m)}{\sigma_m^2}$$

---

### Q9. Perché dobbiamo usare il WACC al netto delle imposte (after-tax WACC) nel contesto del capital budgeting?

Nel capital budgeting, l'attualizzazione dei progetti deve essere effettuata utilizzando il **Weighted Average Cost of Capital (WACC) al netto delle imposte**. Questo è imposto da un principio fondamentale di coerenza finanziaria:

#### 1. Coerenza con i Flussi di Cassa Operativi:
I flussi di cassa incrementali del progetto (OCF e Free Cash Flow) vengono calcolati **al netto delle imposte sul reddito societario ($\tau_c$)**. Poiché i flussi che andiamo ad attualizzare sono grandezze post-tasse, anche il tasso di sconto utilizzato per attualizzarli deve essere espresso su base **post-tasse**.

#### 2. Deducibilità Fiscale del Debito (Scudo Fiscale):
La legislazione fiscale della maggior parte dei paesi consente alle imprese di dedurre gli interessi passivi sul debito dal reddito imponibile. Di conseguenza, il costo effettivo del debito sostenuto dall'azienda ($r_d$) si riduce grazie allo scudo fiscale societario:
$$\text{Costo del Debito Post-Tasse} = r_d \cdot (1 - \tau_c)$$
*Es: Se un'impresa paga un interesse nominale del 7% ($r_d = 0.07$) e l'aliquota fiscale $\tau_c$ è del 40%, lo Stato copre indirettamente il 40% del costo degli interessi. Il costo reale del debito per l'impresa è solo il 4.2% ($0.07 \cdot (1 - 0.40) = 0.042$).*

#### Formula del WACC After-Tax:
$$WACC = r_e \cdot \frac{E}{V} + r_d \cdot (1 - \tau_c) \cdot \frac{D}{V}$$
*dove $E/V$ e $D/V$ sono le quote di Equity e Debito rispetto al valore totale dell'impresa $V$.*

---

### Q10. Commenta questa affermazione: "Il costo del capitale di una società (WACC) è il costo del capitale da utilizzare per qualsiasi tipo di futuro investimento a lungo termine di quella società".

Questa affermazione è **gravemente errata e finanziariamente pericolosa** per la sopravvivenza stessa dell'impresa.

#### Il Rischio di Usare un Unico WACC Aziendale:
Il WACC storico di un'impresa riflette unicamente il **rischio medio delle attività operative correnti** dell'impresa e la sua attuale struttura finanziaria.

Utilizzare indistintamente il WACC medio aziendale per valutare *qualsiasi* investimento futuro è corretto **soltanto se** sono verificate contemporaneamente due condizioni estremamente restrittive:
1. **Omogeneità del Rischio Operativo:** Il nuovo progetto presenta lo stesso identico profilo di rischio sistematico delle attività medie correnti dell'impresa ($\beta_{\text{Project}} = \beta_{\text{Firm}}$).
2. **Invarianza della Struttura Finanziaria:** Il nuovo progetto sarà finanziato mantenendo inalterato il rapporto di leva finanziaria (D/E) aziendale.

#### Cosa succede se il nuovo progetto ha un rischio diverso?
Se l'impresa investe in un progetto con un profilo di rischio significativamente diverso, deve stimare un **costo del capitale specifico del progetto (project-specific cost of capital)**.

```text
Rendimento
Atteso (%)
   ▲
   │                       / Progetti ad Alto Rischio Accettati Erroneamente
   │                      /  (Rendimento atteso < Rendimento minimo richiesto reale)
   │                     /   * (Nuovo Progetto Rischioso)
   │                    /
   ├───────────────────/─── WACC Aziendale Storico Medio
   │                  /
   │                 / * (Nuovo Progetto Conservativo)
   │                /  Progetti Conservativi Rifiutati Erroneamente
   │               /   (Rendimento atteso > Rendimento minimo richiesto reale)
   └──────────────┴────────────────────────► Rischio (Beta β)
```

* **Errore su Progetti ad Alto Rischio (es. start-up interne):**
  Se l'impresa valuta un progetto molto rischioso usando il WACC aziendale medio (che è basso), applicherà un tasso di sconto troppo basso. Questo **sovrastimerà artificialmente l'NPV** del progetto, spingendo l'impresa ad accettare investimenti ad alto rischio che in realtà distruggono valore.
* **Errore su Progetti Conservativi (es. investimenti di pura efficienza):**
  Se l'impresa valuta un progetto a bassissimo rischio usando il WACC aziendale medio (alto), applicherà un tasso di sconto eccessivo. Questo **sottostimerà l'NPV**, portando al rifiuto di progetti sicuri e profittevoli.

---

### Q11. Quali dei seguenti costi sono costi affondati (sunk costs) per uno specifico progetto di investimento: ricerca di mercato (market research), costo del lavoro (labor cost), acquisto di materie prime (purchase of raw materials)?

1. **Ricerca di Mercato (Market Research):**
   * **È un COSTO AFFONDATO.** La ricerca di mercato viene commissionata, svolta e pagata *prima* che il management si riunisca per decidere se approvare o meno l'avvio del progetto. Indipendentemente dalla scelta finale, quei soldi sono persi e non possono essere recuperati. Deve essere esclusa dalla valutazione dell'NPV.

2. **Costo del Lavoro (Labor Cost):**
   * **NON È UN COSTO AFFONDATO.** È un costo operativo futuro ed incrementale. Se il progetto viene rifiutato, l'impresa non assumerà quei lavoratori (o li impiegherà in altre divisioni), azzerando la spesa. Va incluso nei flussi incrementali del progetto.

3. **Acquisto di Materie Prime (Purchase of Raw Materials):**
   * **NON È UN COSTO AFFONDATO.** È una spesa futura incrementale legata strettamente all'avvio produttivo del macchinario. Se il progetto viene bocciato, la materia prima non verrà ordinata, azzerando il costo. Va incluso nei flussi incrementali del progetto.

---

## 🏢 Blocco 5 — Analisi di Sensibilità, Efficienza dei Mercati, Governance e Strumenti di Finanziamento

### Q1. Nel contesto dell'analisi di progetto, sottolinea le differenze tra analisi di sensibilità (sensitivity analysis) e analisi di scenario (scenario analysis).

Entrambi sono strumenti indispensabili nel capital budgeting per valutare il rischio operativo di un progetto prima della sua approvazione, ma differiscono per metodologia e variabili analizzate:

1. **Analisi di Sensibilità (Sensitivity Analysis):**
   * **Metodologia:** Modifica **una sola variabile critica alla volta** (es. solo le Revenues, o solo i costi variabili, o solo il tasso di sconto $r$), mantenendo tutte le altre variabili perfettamente costanti al loro valore del "caso base" (*ceteris paribus*).
   * **Obiettivo:** Identificare quale singola variabile operativa o finanziaria ha l'impatto più devastante o benefico sul Net Present Value (NPV). Aiuta a capire dove focalizzare il monitoring manageriale.
   * Vedi [[Analisi_di_Sensibilita_e_Scenari]].

2. **Analisi di Scenario (Scenario Analysis):**
   * **Metodologia:** Modifica **simultaneamente e coerentemente un gruppo di variabili correlate**, legandole ad una specifica narrativa o evento economico futuro (es. lo scenario "Recessione", "Boom Economico", o "Ingresso di un concorrente aggressivo").
   * **Obiettivo:** Valutare la variabilità dell'NPV in contesti multidimensionali realistici. In una recessione reale, infatti, non variano le vendite isolatamente, ma le vendite scendono, i prezzi dei fattori possono variare ed il tasso di inflazione cambia congiuntamente.

---

### Q2. Definisci il concetto di efficienza del mercato (market efficiency) e le sue tre forme.

L'**Ipotesi di Efficienza del Mercato (EMH — Efficient Market Hypothesis)**, formulata dal Premio Nobel Eugene Fama, stabilisce che in un mercato finanziario i prezzi delle attività negoziate riflettono pienamente, istantaneamente e correttamente tutte le informazioni disponibili. Di conseguenza, nessun investitore può battere costantemente il mercato per generare extra-rendimenti anomali su base rettificata per il rischio.

#### Le Tre Forme di Efficienza (Fama):

1. **Efficienza in Forma Debole (Weak Form Efficiency):**
   * **Informazione:** I prezzi correnti incorporano interamente tutte le informazioni contenute nelle serie storiche dei prezzi, dei volumi di scambio e dei trend passati.
   * **Implicazione:** L'**Analisi Tecnica** (grafici dei prezzi) è del tutto inutile per generare profitti sistematici. I prezzi futuri seguono un *random walk* (cammino casuale).

2. **Efficienza in Forma Semi-Forte (Semi-Strong Form Efficiency):**
   * **Informazione:** I prezzi correnti incorporano sia l'informazione storica sia **tutte le informazioni pubbliche disponibili** sul mercato (bilanci aziendali, annunci di utili, notizie macroeconomiche, decisioni dei regolatori).
   * **Implicazione:** Sia l'analisi tecnica che l'**Analisi Fondamentale** (studio dei bilanci) sono del tutto inutili per sovraperformare il mercato. I prezzi si adeguano istantaneamente non appena le informazioni diventano pubbliche.

3. **Efficienza in Forma Forte (Strong Form Efficiency):**
   * **Informazione:** I prezzi incorporano **tutta l'informazione esistente, sia essa pubblica che privata/riservata** (informazioni insider degli amministratori o scoperte scientifiche segrete).
   * **Implicazione:** Nessuno, nemmeno chi possiede informazioni privilegiate di prima mano, può generare extra-rendimenti anomali. Le informazioni trapelano e si riflettono nei prezzi all'istante.

Per approfondimenti teorici ed approcci alternativi (Behavioral Finance, Grossman-Stiglitz), consultare [[Efficienza_dei_Mercati]].

---

### Q3. Spiega le nozioni di mercati finanziari e intermediari finanziari.

I mercati e gli intermediari sono i due canali principali attraverso cui il sistema economico alloca la liquidità dai risparmiatori alle imprese.

1. **Mercati Finanziari (Financial Markets):**
   * **Definizione:** Sono luoghi ideali o infrastrutture telematiche regolamentate in cui gli agenti economici scambiano direttamente attività finanziarie (azioni, obbligazioni, valute, derivati). Rappresentano il **canale di finanziamento diretto** (es. Borsa Valori, mercati obbligazionari).
   * **Funzione principale:** Favorire la liquidità dei titoli e la trasparenza dei prezzi tramite il libero incontro di domanda e offerta.

2. **Intermediari Finanziari (Financial Intermediaries):**
   * **Definizione:** Istituzioni ed enti specializzati (banche commerciali, fondi comuni di investimento, fondi pensione, compagnie di assicurazione) che si pongono fisicamente tra i datori di fondi (soggetti in surplus, es. famiglie risparmiatrici) e i prenditori di fondi (soggetti in deficit, es. imprese o governi). Rappresentano il **canale di finanziamento indiretto**.
   * **Perché esistono?** Riducono drasticamente le frizioni del mercato reale:
     *   *Riduzione dei Costi di Transazione:* Raccolgono piccoli capitali per sfruttare economie di scala.
     *   *Trasformazione delle Scadenze:* Raccolgono a breve termine (es. depositi di conto corrente) e prestano a lungo termine (es. mutui immobiliari alle imprese).
     *   *Mitigazione del Rischio (Diversificazione):* Consentono ai piccoli risparmiatori di investire in panieri diversificati.
     *   *Risoluzione delle Asimmetrie Informative:* Effettuano lo screening preliminare del merito creditizio (*adverse selection*) e il monitoraggio costante sul comportamento dei debitori (*moral hazard*).

Vedi [[Market_Efficiency_and_Financial_Intermediaries]] e [[Mercati_Finanziari]].

---

### Q4. Cos'è un'IPO (Initial Public Offering)?

Un'**IPO (Offerta Pubblica Iniziale)** è il processo finanziario e legale attraverso il quale una società per azioni privata quota i propri titoli per la prima volta su un mercato azionario regolamentato (es. NYSE, Nasdaq, Borsa Italiana), offrendo le proprie azioni al pubblico indistinto (investitori retail ed istituzionali).

#### Caratteristiche Fondamentali:
* **Transizione Societaria:** L'impresa cessa di essere "privata" (proprietà ristretta nelle mani dei fondatori o di Venture Capital) e diventa una **public company** (società quotata a proprietà diffusa).
* **Raccolta di Capitale (Primary Offering):** Consente all'impresa di raccogliere ingenti capitali di rischio freschi emettendo nuove azioni per finanziare la crescita futura.
* **Exit degli Investitori Esistenti (Secondary Offering):** Consente ai soci storici (es. fondatori o fondi di Private Equity) di smobilizzare il proprio capitale vendendo le proprie azioni storiche sul mercato (*liquidity event*).
* **Il Ruolo degli Underwriters:** Il processo è gestito da un pool di banche d'investimento (*investment banks*) che curano la due diligence legale, la redazione del prospetto informativo per la SEC/Consob, la promozione (*roadshow*), il raccordo degli ordini (*bookbuilding*) e la determinazione del prezzo finale di offerta.

Vedi [[Ciclo_di_Vita_e_Finanziamento]].

---

### Q5. Spiega le principali forme di conflitti di agenzia tra azionisti (shareholders) e manager.

I **Conflitti di Agenzia** nascono dalla separazione tra la proprietà dell'impresa (gli azionisti o *Principal*) e il controllo operativo della stessa (i manager o *Agent*) nelle grandi public companies. I manager, agendo come agenti degli azionisti, potrebbero perseguire obiettivi di massimizzazione del proprio benessere personale anziché la massimizzazione del valore delle azioni per gli azionisti.

#### Le 5 Forme Principali di Opportunismo Manageriale:

1. **Empire Building (Espansione Inefficiente):**
   I manager prediligono le grandi dimensioni aziendali perché lo status sociale, il potere politico e il proprio livello retributivo sono fortemente correlati alle dimensioni dell'impresa controllata. Possono approvare fusioni e acquisizioni non redditizie (a NPV negativo) o investire massicciamente per la pura crescita dimensionale a scapito del valore azionario.
   
2. **Sforzo Insufficiente (Shirking):**
   I manager potrebbero non dedicare il massimo impegno professionale alle attività operative o evitare decisioni strategiche complesse e dolorose (es. ristrutturazioni del personale, tagli di rami inefficienti) per mantenere una "vita tranquilla".
   
3. **Consumo di Benefici Privati (Perquisites / Perks):**
   Utilizzo di risorse liquide dell'impresa per finanziare privilegi di lusso personali giustificati come costi aziendali (es. jet privati aziendali per viaggi personali, uffici sontuosi, cene di gala).
   
4. **Investimenti di Trinceramento (Entrenching Investments):**
   Scelta deliberata del manager di effettuare investimenti specifici in progetti ad alta complessità che solo lui o il suo team ristretto sanno gestire. Questo rende il manager letteralmente indispensabile per l'azienda, aumentando il suo potere contrattuale e rendendo il suo licenziamento estremamente costoso per gli azionisti, anche a fronte di scarse performance.
   
5. **Avversione al Rischio Asimmetrica:**
   Gli azionisti possiedono portafogli diversificati e sono neutrali al rischio specifico dell'impresa. Al contrario, il manager ha la sua ricchezza totale e il suo capitale umano interamente concentrati nell'impresa. Per paura del fallimento (che comporterebbe la perdita del lavoro e del prestigio), il manager potrebbe rifiutare progetti rischiosi ma ad NPV fortemente positivo.

Vedi [[Governance_e_Problemi_di_Agenzia]] e [[Corporate_Governance_and_Lifecycle]].

---

### Q6. Descrivi le principali forme di approccio alla creazione del valore: shareholder capitalism, stakeholder capitalism e socially responsible business.

La dottrina economica e manageriale offre tre visioni alternative sul fine ultimo dell'impresa nella società:

#### 1. Shareholder Capitalism (Capitalismo degli Azionisti):
* **Dottrina:** Teorizzata da Milton Friedman, sostiene che l'unico scopo legittimo dell'impresa è la **massimizzazione della ricchezza degli azionisti** a lungo termine, nel rispetto delle leggi e delle regole base del mercato.
* **Razionale:** Gli azionisti sono i *residual claimants* (sopportano il rischio maggiore e ricevono solo ciò che resta dopo aver pagato dipendenti, fornitori e creditori). Massimizzando il valore azionario, si stimola l'efficienza allocativa di tutta l'impresa, beneficiando indirettamente la società.

#### 2. Stakeholder Capitalism (Capitalismo dei Portatori d'Interesse):
* **Dottrina:** L'impresa deve essere gestita per **creare valore bilanciato per tutti i suoi stakeholder**: azionisti, ma anche dipendenti, clienti, fornitori, comunità locali in cui opera ed ambiente.
* **Razionale:** L'impresa è considerata un'istituzione sociale complessa. Gli interessi dell'azionista non hanno alcuna priorità morale o economica intrinseca rispetto a quelli degli altri portatori d'interesse. Il valore azionario è una conseguenza e non il fine unico.

#### 3. Socially Responsible Business (Impresa Socialmente Responsabile):
* **Dottrina:** Evoluzione operativa dello stakeholder capitalism, formalizzata nei criteri **ESG (Environmental, Social, Governance)**. L'impresa genera profitto esclusivamente operando in modo etico, preservando attivamente l'ambiente, garantendo i diritti dei lavoratori e applicando una governance societaria trasparente e priva di corruzione.
* **Razionale:** Mira alla creazione di **valore condiviso a lungo termine** (*Shared Value*), ritenendo che l'irresponsabilità sociale o ambientale esponga l'impresa a gravissimi rischi reputazionali e legali che distruggerebbero anche il valore finanziario.

---

### Q7. Discuti la differenza tra cash flow rights (diritti sui flussi di cassa) e control rights (diritti di controllo). Chi possiede questi diritti?

1. **Cash Flow Rights (Diritti Economici):**
   * **Cosa sono:** Rappresentano il diritto economico proporzionale di ricevere i flussi di cassa residui generati dall'attività dell'impresa sotto forma di dividendi o, in caso di scioglimento, la quota del patrimonio netto liquidato.
   * **Chi li possiede:** Tutti gli **azionisti** dell'impresa, in proporzione diretta al numero di azioni possedute sul capitale totale.

2. **Control Rights (Diritti di Voto/Controllo):**
   * **Cosa sono:** Rappresentano il diritto amministrativo di votare nelle assemblee dei soci per eleggere i membri del Consiglio di Amministrazione (CdA), nominare i sindaci e approvare le delibere straordinarie (es. fusioni, aumenti di capitale).
   * **Chi li possiede:** Gli **azionisti detentori di azioni con diritto di voto** (es. azioni ordinarie). Sono esclusi i possessori di azioni speciali prive di voto (es. azioni di risparmio).

#### La Separazione dei Diritti (Deviazioni dal principio "One Share, One Vote"):
In condizioni di equilibrio teorico, vige il principio *One Share, One Vote* (se possiedo il 10% delle azioni, ho il 10% dei dividendi e il 10% dei voti). Tuttavia, i soci di controllo possono separare questi diritti per controllare l'impresa pur apportando pochissimo capitale, esponendo gli azionisti di minoranza a forti abusi:

* **Dual-Class Shares (Azioni a Doppia Classe):**
  L'emissione di azioni di Classe A (destinate al pubblico, con 1 voto o zero voti) e azioni di Classe B (trattenute dai fondatori, con 10 o 20 voti per azione). I fondatori mantengono il 70% dei diritti di controllo pur possedendo solo il 10% dei cash flow rights (e quindi del capitale proprio reale).
* **Strutture Piramidali (Pyramidal Structures):**
  Catene di controllo in cui una holding A controlla la holding B, che controlla la società operativa C. Il socio di controllo al vertice può dominare la società operativa C pur possedendo una frazione infinitesima di cash flow rights reali di C.

---

### Q8. Obbligazioni (Bonds): illustra il concetto di seniority, security e call provisions.

Questi tre elementi contrattuali definiscono il profilo di rischio e rendimento di un titolo obbligazionario societario:

1. **Seniority (Grado di Subordinazione):**
   * Indica l'ordine di priorità di rimborso dei creditori in caso di fallimento o liquidazione forzata dell'impresa. 
   * Il debito *Senior* ha la precedenza assoluta e viene pagato per primo con le risorse recuperate. Il debito *Junior* o *Subordinated* (subordinato) viene rimborsato solo dopo che il debito senior è stato integralmente soddisfatto. Poiché rischiano di più, le obbligazioni subordinate offrono cedole più elevate.

2. **Security (Presenza di Garanzie Reali):**
   * Si riferisce alla presenza di asset specifici dell'impresa posti a garanzia del rimborso del debito.
   * I **Secured Bonds** (es. *Mortgage Bonds*) sono garantiti da beni fisici (es. immobili o impianti). In caso di default, i creditori garantiti si rifanno direttamente su tali beni.
   * Gli **Unsecured Bonds** (chiamati *Debentures*) non hanno garanzie su asset specifici, ma sono protetti solo dalla generica capacità dell'impresa di produrre cassa.

3. **Call Provisions (Clausole di Rimborso Anticipato):**
   * Clausola contrattuale che concede alla società emittente il diritto (opzione call) di rimborsare interamente il bond prima della scadenza naturale ad un prezzo prestabilito (*Call Price*).
   * Viene esercitata se i tassi d'interesse di mercato scendono significativamente. L'azienda rimborsa il vecchio debito costoso per emetterne di nuovo a tassi inferiori. Poiché questa clausola danneggia l'investitore (che subisce il rischio di reinvestire a tassi bassi), i *Callable Bonds* devono offrire cedole più elevate rispetto a bond equivalenti non callable.

Vedi [[Strumenti_di_Debito_Avanzati]] e [[Debt_Financing_Overview]].

---

### Q9. Descrivi le principali forme di obbligazioni insolite o esotiche (unusual bonds).

La finanza strutturata ha sviluppato strumenti di debito esotici per rispondere a specifiche esigenze di copertura dei rischi o di ottimizzazione fiscale:

1. **Catastrophe Bonds (Cat Bonds):**
   * Obbligazioni emesse da compagnie assicurative o riassicurative il cui rimborso è legato al non-accadimento di una specifica catastrofe naturale (es. un terremoto in California o un uragano in Florida). Se la catastrofe si verifica entro la scadenza, l'emittente è legalmente esentato dal rimborso del capitale, incamerandolo per liquidare le polizze assicurative dei danneggiati.

2. **Mortality Bonds:**
   * Strumenti di debito legati a indici demografici. Se il tasso di mortalità in una data regione geografica supera una determinata soglia (es. a causa di una pandemia globale), l'emittente sospende il pagamento degli interessi o del capitale.

3. **Asset-Backed Securities (ABS):**
   * Obbligazioni i cui flussi di cassa (cedole e capitale) non sono garantiti dal bilancio dell'impresa emittente, ma da un portafoglio segretato di piccoli asset finanziari illiquidi cartolarizzati (es. contratti di leasing auto, debiti su carte di credito, o mutui subprime).

4. **Zero-Coupon Bonds (Obbligazioni senza Cedola):**
   * Non pagano cedole periodiche. Vengono emessi a forte sconto rispetto al valore nominale (es. prezzo di emissione 70, valore nominale di rimborso 100). Il rendimento dell'investitore è dato interamente dalla differenza di prezzo. Sono privi di rischio di reinvestimento delle cedole.

---

### Q10. Cos'è un prestito bancario (bank loan)?

Un **prestito bancario** è un accordo di finanziamento bilaterale a debito concesso direttamente da un istituto di credito (banca) ad un'impresa. A differenza delle obbligazioni (che sono titoli negoziabili sul mercato dei capitali), il prestito bancario è un contratto privato, non quotato e non trasferibile se non tramite accordi di cessione del credito.

#### Le Principali Tipologie di Prestito Bancario per le Imprese:

1. **Linea di Credito Revolving (Revolving Line of Credit):**
   * Un accordo flessibile a breve-medio termine in cui la banca mette a disposizione dell'impresa un tetto massimo di liquidità. L'impresa può prelevare cassa in base al fabbisogno giornaliero, rimborsarla non appena incassa dai clienti e ri-prelevarla successivamente. Gli interessi si pagano solo sulla quota di capitale effettivamente prelevata.

2. **Prestito Sindacato (Syndicated Loan):**
   * Un finanziamento di dimensioni mastodontiche (spesso centinaia di milioni o miliardi di euro) erogato non da una singola banca, ma da un **sindacato (consorzio) di banche**.
   * Una banca capofila (*Lead Arranger*) struttura l'operazione e organizza il pool di banche, ciascuna delle quali sottoscrive una quota del prestito. Questa struttura consente di ripartire il rischio di insolvenza su grandi progetti industriali ed infrastrutturali.

Vedi [[Debt_Financing]].

---

### Q11. Cos'è un leasing (lease)? Descrivi i suoi principali vantaggi per le imprese.

Il **leasing** è un accordo contrattuale in cui il proprietario di un bene tangibile (il *locatore* o società di leasing) concede ad un'altra parte (il *locatario* o impresa utilizzatrice) il diritto esclusivo di utilizzare quel bene (es. macchinari industriali, flotte aziendali, immobili commerciali) per un periodo di tempo determinato, in cambio di canoni periodici di locazione.

#### I 4 Principali Vantaggi del Leasing:

1. **Finanziamento al 100% e Conservazione della Cassa:**
   Consente all'impresa di acquisire l'utilizzo di beni capitali costosi senza dover sborsare ingenti capitali iniziali ($CapEx$) a t=0. Non richiede acconti massicci, preservando la liquidità dell'impresa per il capitale circolante operativo.
   
2. **Protezione dall'Obsolescenza Tecnologica:**
   Al termine del contratto di leasing operativo, l'impresa ha la facoltà di restituire il macchinario alla società di leasing ed attivare un nuovo contratto per un bene tecnologicamente aggiornato, eliminando il rischio di rimanere proprietari di un bene obsoleto ed invendibile.
   
3. **Vantaggi Fiscali e deducibilità accelerata:**
   In molte normative fiscali, i canoni periodici di leasing sono interamente deducibili dal reddito imponibile in un arco temporale significativamente più breve rispetto al piano di ammortamento ministeriale previsto in caso di acquisto diretto del bene.
   
4. **Flessibilità contrattuale:**
   I contratti possono prevedere opzioni di riscatto finale ad un prezzo prefissato basso, opzioni di rinnovo o opzioni di manutenzione ordinaria inclusa a carico del locatore (*leasing operativo*).

Vedi [[Debt_Financing_Overview]].


---

## 📊 Blocco 6 — Caso Pratico (Vega Corporation)

### Caso Pratico: Valutazione d'Investimento e Struttura Finanziaria per Vega Corporation

Questo blocco propone la risoluzione analitica e accademica del caso pratico legato a **Vega Corporation**, un'impresa petrolifera internazionale che deve valutare l'acquisto di un'attrezzatura per l'estrazione di greggio nel Mare del Nord.

---

### 1. Inquadramento del Problema e Analisi dei Dati

Prima di procedere con i calcoli quantitativi, è fondamentale applicare una regola aurea di capital budgeting trattata nel **Blocco 2, Q7 (Sunk Costs)**:
* Il testo menziona che un investimento precedente di **€ 1.900** ha permesso di identificare i giacimenti di petrolio. 
* Questa spesa rappresenta a tutti gli effetti un **Costo Affondato (Sunk Cost)**. È stata sostenuta nel passato, non è recuperabile in caso di rinuncia e non varia su base incrementale. Pertanto, deve essere **rigorosamente esclusa** dalla valutazione economica corrente.

#### Dati Operativi e Fiscali del Progetto:
* **Costo dell'attrezzatura ($CapEx_0$):** $€ 2.500$ (investito a $t=0$).
* **Vita del progetto ($T$):** $5$ anni.
* **Metodo di ammortamento:** Quote costanti (*straight-line depreciation*), senza valore residuo finale ($Salvage\ Value = 0$).
  $$\text{Ammortamento Annuo (Depreciation)} = \frac{CapEx_0}{T} = \frac{2.500}{5} = 500\text{ €/anno}$$
* **Ricavi annui aggiuntivi:** $€ 1.000$ (anni da 1 a 5).
* **Costi operativi annui aggiuntivi (escluso ammortamento):** $€ 450$ (anni da 1 a 5).
* **Aliquota fiscale societaria ($\tau_c$):** $40\%$ ($0,40$).
* **Capitale Circolante Netto ($NWC$) di fine anno:**
  * Anno 1: $€ 250$
  * Anno 2: $€ 550$
  * Anno 3: $€ 750$
  * Anno 4: $€ 600$
  * Anno 5: $€ 0$ (alla chiusura del progetto, il capitale circolante viene interamente liquidato e recuperato).

#### Dati Finanziari di Mercato e della Società:
* **Tasso privo di rischio ($R_f$):** $3\%$ ($0,03$).
* **Beta azionario dell'impresa ($\beta_e$):** $2$.
* **Rendimento atteso del mercato ($E[R_m]$):** $8\%$ ($0,08$).
* **Costo nominale del debito ($r_d$):** $7\%$ ($0,07$).
* **Leva Finanziaria (Asset-to-Equity Ratio):** $\frac{Asset}{Equity} = 2$.
  * Poiché il valore totale degli asset ($A$) corrisponde al valore totale dell'impresa ($V = D + E$), abbiamo:
    $$\frac{V}{E} = 2 \implies \frac{E}{V} = 0,5 \quad (50\%\ \text{Equity})$$
  * Di conseguenza, la quota di debito sul valore totale è:
    $$\frac{D}{V} = 1 - \frac{E}{V} = 0,5 \quad (50\%\ \text{Debito})$$
  * Il rapporto Debito/Equity di equilibrio è pari a $D/E = 1$.
* **Assunzione di Rischio:** Il rischio operativo del progetto e la sua leva finanziaria sono equiparabili a quelli medi dell'intera impresa.

---

### 2. Calcolo del Costo dell'Equity ($r_e$) e del WACC After-Tax

Poiché il rischio del progetto rispecchia quello aziendale, possiamo utilizzare il tasso di rendimento richiesto medio come tasso di sconto.

#### A. Calcolo del Costo del Capitale Proprio ($r_e$) via CAPM:
Applichiamo la formula della [[Topic_7_8_CAPM_Cost_of_Capital#Security Market Line (SML)]]:
$$r_e = R_f + \beta_e \cdot \big(E[R_m] - R_f\big)$$
$$r_e = 3\% + 2 \cdot (8\% - 3\%) = 3\% + 2 \cdot 5\% = 13\% \quad (0,13)$$

#### B. Calcolo del Costo Medio Ponderato del Capitale al netto delle imposte (After-Tax WACC):
Il debito gode della deducibilità fiscale degli interessi (scudo fiscale). La formula del [[Topic_7_8_CAPM_Cost_of_Capital#Weighted Average Cost of Capital (WACC)]] è:
$$WACC = r_e \cdot \frac{E}{V} + r_d \cdot (1 - \tau_c) \cdot \frac{D}{V}$$
$$WACC = 13\% \cdot 0,5 + 7\% \cdot (1 - 0,40) \cdot 0,5$$
$$WACC = 6,5\% + 7\% \cdot 0,6 \cdot 0,5 = 6,5\% + 2,1\% = 8,6\% \quad (0,086)$$

---

### 3. Calcolo del Operating Cash Flow (OCF) del Progetto

Applichiamo il principio di separazione (Blocco 2, Q3) determinando il flusso operativo unlevered (senza sottrarre gli oneri finanziari):
$$OCF = (Revenues - Expenses - Depreciation) \cdot (1 - \tau_c) + Depreciation$$
$$OCF = (1.000 - 450 - 500) \cdot (1 - 0,40) + 500$$
$$OCF = 50 \cdot 0,60 + 500 = 30 + 500 = 530\text{ €/anno (costante per gli anni 1-5)}$$

---

### 4. Gestione del Capitale Circolante Netto (NWC)

Il Capitale Circolante Netto blocca liquidità quando aumenta ($\Delta NWC > 0$, che rappresenta un deflusso di cassa: $-\Delta NWC$) e rilascia liquidità quando si riduce o si azzera alla fine del ciclo vitale del progetto ($\Delta NWC < 0$).

La variazione incrementale del circolante ($\Delta NWC_t = NWC_t - NWC_{t-1}$) e i relativi flussi di cassa operativi legati al [[Gestione_del_Capitale_Circolante]] sono riassunti nella seguente tabella:

| Voce | Anno 0 | Anno 1 | Anno 2 | Anno 3 | Anno 4 | Anno 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Capitale Circolante ($NWC_t$)** | 0,00 | 250,00 | 550,00 | 750,00 | 600,00 | 0,00 |
| **Variazione ($\Delta NWC_t$)** | 0,00 | 250,00 | 300,00 | 200,00 | -150,00 | -600,00 |
| **Flusso di Cassa ($-\Delta NWC_t$)** | **0,00** | **-250,00** | **-300,00** | **-200,00** | **150,00** | **600,00** |

---

### 5. Ricostruzione dei Flussi di Cassa Netti di Progetto ($NCF_t$)

Il flusso di cassa totale di progetto ($NCF_t$), noto anche come *Free Cash Flow to Firm (FCFF) del progetto*, si ottiene sommando i flussi di investimento e i flussi operativi:
$$NCF_t = CF(\text{Capital Investment})_t + OCF_t - \Delta NWC_t$$

| Voce | Anno 0 | Anno 1 | Anno 2 | Anno 3 | Anno 4 | Anno 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Spese in Asset Fissi (CapEx)** | -2.500,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **Operating Cash Flow (OCF)** | 0,00 | 530,00 | 530,00 | 530,00 | 530,00 | 530,00 |
| **Variazione Circolante ($-\Delta NWC$)** | 0,00 | -250,00 | -300,00 | -200,00 | 150,00 | 600,00 |
| **Flusso Netto di Progetto ($NCF_t$)** | **-2.500,00** | **280,00** | **230,00** | **330,00** | **680,00** | **1.130,00** |

---

### 6. Caso 1: Valutazione con Struttura Finanziaria Target ($WACC = 8,6\%$)

Attualizziamo i flussi di cassa netti di progetto al costo medio ponderato del capitale della società ($WACC = 8,6\%$):

$$NPV = -2.500 + \sum_{t=1}^{5} \frac{NCF_t}{(1 + WACC)^t}$$

#### Tabella di Attualizzazione dei Flussi:

| Periodo ($t$) | Flusso di Cassa ($NCF_t$) | Formula di Attualizzazione | Fattore Sconto ($1,086^{-t}$) | Flusso Attualizzato ($PV_t$) |
| :---: | :---: | :---: | :---: | :---: |
| **0** | -2.500,00 | $$-2.500,00 / (1 + 0,086)^0$$ | 1,0000 | -2.500,00 € |
| **1** | 280,00 | $$280,00 / (1 + 0,086)^1$$ | 0,9208 | 257,83 € |
| **2** | 230,00 | $$230,00 / (1 + 0,086)^2$$ | 0,8479 | 195,02 € |
| **3** | 330,00 | $$330,00 / (1 + 0,086)^3$$ | 0,7807 | 257,65 € |
| **4** | 680,00 | $$680,00 / (1 + 0,086)^4$$ | 0,7189 | 488,87 € |
| **5** | 1.130,00 | $$1.130,00 / (1 + 0,086)^5$$ | 0,6620 | 748,05 € |
| **NPV** | | **Somma dei Flussi Attualizzati** | | **-552,60 €** |

#### Conclusione Decisionale (NPV Rule):
Poiché il Valore Attuale Netto è strettamente negativo ($NPV = -552,60\text{ €} < 0$), **il progetto distrugge valore economico** per un ammontare pari a $€ 552,60$ a favore degli azionisti. Pertanto, la proposta di investimento **deve essere rifiutata**.

---

### Calcolo e Verifica del Tasso di Rendimento Interno (IRR)

Il Tasso di Rendimento Interno ($IRR$) del progetto è pari al **$1,5463\%$** ($0,015463$). 

#### Verifica dell'IRR (NPV = 0):
Per dimostrare la correttezza dell'IRR calcolato, attualizziamo i medesimi flussi di cassa al tasso del $1,5463\%$ per verificare l'azzeramento dell'NPV:

* Anno 0: $-2.500,00\text{ €}$
* Anno 1: $$\frac{280,00}{(1 + 0,015463)^1} \approx 275,74\text{ €}$$
* Anno 2: $$\frac{230,00}{(1 + 0,015463)^2} \approx 223,05\text{ €}$$
* Anno 3: $$\frac{330,00}{(1 + 0,015463)^3} \approx 315,15\text{ €}$$
* Anno 4: $$\frac{680,00}{(1 + 0,015463)^4} \approx 639,52\text{ €}$$
* Anno 5: $$\frac{1.130,00}{(1 + 0,015463)^5} \approx 1.046,55\text{ €}$$

#### Somma dei Valori Attuali (PV) dei Flussi Futuri:
$$PV_{\text{Attivi}} = 275,74 + 223,05 + 315,15 + 639,52 + 1.046,55 = 2.500,01\text{ €}$$
$$NPV = -2.500,00 + 2.500,01 \approx 0,00\text{ €}$$

La verifica conferma l'esattezza matematica dell'IRR.

#### Conclusione Decisionale (IRR Rule):
Poiché il tasso di rendimento interno del progetto è nettamente inferiore al costo opportunità del capitale (rappresentato dal WACC dell'8,6%):
$$IRR = 1,5463\% < WACC = 8,6\%$$
Anche la regola dell'IRR impone di **rifiutare il progetto**.

---

### 7. Caso 2: Valutazione con Finanziamento tramite Solo Equity ($r_e = 13\%$)

Ipotizziamo ora che il progetto venga finanziato **interamente dagli azionisti** (*all-equity financing*), senza ricorrere ad alcun indebitamento finanziario. 
In questo scenario, l'impresa perde lo scudo fiscale sul debito, ed il costo opportunità del capitale per scontare i flussi coincide interamente con il costo dell'equity non-levered ($r_e = 13\%$).

Attualizziamo i flussi di cassa di progetto al tasso del $13\%$:

$$NPV = -2.500 + \sum_{t=1}^{5} \frac{NCF_t}{(1 + 0,13)^t}$$

#### Tabella di Sconto al 13%:

| Periodo ($t$) | Flusso di Cassa ($NCF_t$) | Formula di Attualizzazione | Fattore Sconto ($1,13^{-t}$) | Flusso Attualizzato ($PV_t$) |
| :---: | :---: | :---: | :---: | :---: |
| **0** | -2.500,00 | $$-2.500,00 / (1 + 0,13)^0$$ | 1,0000 | -2.500,00 € |
| **1** | 280,00 | $$280,00 / (1 + 0,13)^1$$ | 0,8850 | 247,79 € |
| **2** | 230,00 | $$230,00 / (1 + 0,13)^2$$ | 0,7831 | 180,12 € |
| **3** | 330,00 | $$330,00 / (1 + 0,13)^3$$ | 0,6931 | 228,71 € |
| **4** | 680,00 | $$680,00 / (1 + 0,13)^4$$ | 0,6133 | 417,06 € |
| **5** | 1.130,00 | $$1.130,00 / (1 + 0,13)^5$$ | 0,5428 | 613,32 € |
| **NPV** | | **Somma dei Flussi Attualizzati** | | **-813,01 €** |

#### Conclusione Decisionale:
L'NPV scende a **$-813,01\text{ €}$**, distruggendo ancora più valore. Questo decremento è perfettamente coerente con la teoria finanziaria: l'assenza di debito rimuove i benefici dello scudo fiscale societario ($\tau_c \cdot r_d \cdot D$), innalzando il costo opportunità del capitale dal $8,6\%$ al $13\%$. Scontando flussi di cassa identici a un tasso superiore, l'NPV si contrae pesantemente. Il progetto **deve essere rifiutato**.

#### Determinazione dell'IRR del Progetto senza Leva:
L'IRR del progetto in assenza di debito rimane **rigorosamente invariato a $1,5463\%$**.

#### Spiegazione Finanziaria ed Accademica:
Il Tasso di Rendimento Interno ($IRR$) è un indicatore di rendimento di tipo **endogeno** e **intrinseco** al progetto. Esso si calcola risolvendo un'equazione polinomiale che dipende esclusivamente dall'entità, dal segno e dalla sequenza temporale dei flussi di cassa netti di progetto ($NCF_t$). 

In base al **Principio di Separazione** (trattato nel Blocco 2, Q3), la convenienza dei flussi di cassa operativi e di investimento di progetto viene valutata su base *unlevered* (prescindendo da come questi flussi vengano divisi tra debitori ed azionisti). Poiché la variazione della struttura finanziaria altera il tasso di sconto (il WACC o $r_e$) ma **non modifica minimamente i flussi fisici di cassa operativi e di investimento generati dal progetto** ($NCF_t$), l'equazione che determina l'IRR non cambia. Di conseguenza, il tasso che azzera l'NPV rimane identico a $1,5463\%$.

---

## Fonti
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
* [[wiki/Concetti/Topic_5_NPV_Investment_Criteria.md]]
* [[wiki/Concetti/Topic_7_8_CAPM_Cost_of_Capital.md]]
* [[wiki/Concetti/Struttura_del_Capitale.md]]
* [[wiki/Concetti/Gestione_del_Capitale_Circolante.md]]
* [[wiki/Concetti/Teorema_Modigliani_Miller.md]]
* [[wiki/Concetti/Free_Cash_Flow.md]]
* [[wiki/Concetti/Debt_Financing_Overview.md]]
* [[wiki/Concetti/Analisi_di_Sensibilita_e_Scenari.md]]
* [[wiki/Concetti/Efficienza_dei_Mercati.md]]
* [[wiki/Concetti/Market_Efficiency_and_Financial_Intermediaries.md]]
* [[wiki/Concetti/Mercati_Finanziari.md]]
* [[wiki/Concetti/Ciclo_di_Vita_e_Finanziamento.md]]
* [[wiki/Concetti/Governance_e_Problemi_di_Agenzia.md]]
* [[wiki/Concetti/Corporate_Governance_and_Lifecycle.md]]
* [[wiki/Concetti/Debt_Financing.md]]
* [[wiki/Concetti/Strumenti_di_Debito_Avanzati.md]]

