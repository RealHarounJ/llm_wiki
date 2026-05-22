---
tags: [corporate-finance, cash-budgeting, working-capital, esercitazione, excel]
aliases: [Cash Budget, Piano di Tesoreria]
---

# Esercitazione Pratica: Cash Budgeting (Piano di Tesoreria)

Come hai correttamente intuito prima, il **Cash Budgeting** è uno strumento fondamentale a breve termine. Serve al Financial Manager per prevedere le entrate (Inflows) e le uscite (Outflows) di cassa mensili o trimestrali, per capire in anticipo se l'azienda avrà bisogno di un prestito a breve termine (Short-Term Debt) o se avrà liquidità in eccesso da investire.

Ecco una simulazione pratica stile esame, come la vedresti su un foglio Excel.

### Dati e Assunzioni della Simulazione:
*   **Saldo di Cassa Iniziale a Gennaio (Beginning Cash):** 50.000 €
*   **Requisito Minimo di Cassa (Minimum Cash Balance):** L'azienda vuole avere sempre almeno 40.000 € in banca per emergenze.
*   **Regola degli Incassi:** Il 50% delle vendite viene incassato subito in contanti, il restante 50% il mese successivo (Crediti).
*   (Nota: A Gennaio incassiamo 40.000 € di vecchi crediti di Dicembre).

---

### Tabella Excel: Modello di Cash Budget (Migliaia di €)

| Voce (Item) | Gennaio | Febbraio | Marzo |
| :--- | :--- | :--- | :--- |
| **A. Entrate di Cassa (Cash Inflows)** | | | |
| Vendite del mese (50% in contanti) | 50 | 75 | 100 |
| Incasso Crediti mese precedente (50%) | 40 | 50 | 75 |
| **Totale Inflows** | **90** | **125** | **175** |
| | | | |
| **B. Uscite di Cassa (Cash Outflows)** | | | |
| Pagamento Fornitori / Materiali | 50 | 80 | 70 |
| Salari, Affitti, Tasse | 30 | 40 | 30 |
| Spese Straordinarie (es. acquisto macchinario) | 0 | 0 | 120 |
| **Totale Outflows** | **80** | **120** | **220** |
| | | | |
| **C. Net Cash Flow (A - B)** | **+10** | **+5** | **-45** |
| | | | |
| **D. Saldo di Cassa (Cash Balance)** | | | |
| Saldo Iniziale (Beginning Balance) | 50 | 60 | 65 |
| Net Cash Flow del mese (C) | +10 | +5 | -45 |
| **Saldo Finale (Ending Balance)** | **60** | **65** | **20** |
| | | | |
| **E. Analisi del Finanziamento** | | | |
| Requisito Minimo di Cassa | 40 | 40 | 40 |
| **Fabbisogno di Debito a Breve Termine** | **0** | **0** | **20** |
| Saldo Finale *Corretto* (dopo prestito) | 60 | 65 | 40 |

---

### Come leggere questa tabella all'esame:

1.  **Gennaio e Febbraio:** L'azienda genera Net Cash Flow positivo. Il Saldo Finale rimane sempre sopra il requisito minimo di 40.000 €. Non serve nessun finanziamento bancario.
2.  **Marzo:** C'è una spesa straordinaria di 120.000 € (Acquisto Macchinario). Il Net Cash Flow crolla a -45.000 €.
3.  **Il campanello d'allarme:** Il Saldo Finale a Marzo scenderebbe a soli 20.000 €. Poiché la politica aziendale impone di avere almeno 40.000 € in cassa, il manager sa già mesi prima che a Marzo dovrà chiedere una **Linea di Credito (Bank Loan)** di 20.000 € per tappare il buco e rispettare il limite minimo di cassa.

## Fonti
* [[wiki/Fonti/Fonte_Corporate_Finance_Book.md]]
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
