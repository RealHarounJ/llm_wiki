---
tags: [esercitazione, npv, capital-budgeting, excel]
aliases: [Esercizio NPV Macchinario]
---

# 📝 Esercizio Svolto: Valutazione Investimento (NPV/IRR)

*Fonte: Topic 5b — Solution*

## 📌 Testo del Problema
Un'azienda valuta l'acquisto di un nuovo macchinario:
- **Prezzo d'acquisto**: €1.500 (Anno 0)
- **Ricavi aggiuntivi**: €800/anno (Anni 1-5)
- **Spese incrementali**: €40/anno (Anni 1-5)
- **Ammortamento**: €250/anno (lineare su 5 anni)
- **Capitale Circolante (NWC)**: 11% dei ricavi (10% scorte, 5% crediti, -4% debiti). Si accumula tra Anno 1 e 2, si azzera all'Anno 5.
- **Valore di recupero**: €250 (fine Anno 5)
- **Tax Rate**: 35%
- **Costo del Capitale (r)**: 10%

## 📐 Tabella dei Flussi di Cassa

| Voce | Anno 0 | Anno 1 | Anno 2 | Anno 3 | Anno 4 | Anno 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Investimento Fisso** | -1500 | | | | | 250 |
| **Operating Cash Flow** | | 581.5 | 581.5 | 581.5 | 581.5 | 581.5 |
| **Variazione NWC** | | -88 | -88 | 0 | 0 | 176 |
| **Flusso di Cassa Totale** | **-1500** | **493.5** | **493.5** | **581.5** | **581.5** | **1007.5** |

### Calcolo OCF (Operating Cash Flow)
$$OCF = (\text{Ricavi} - \text{Spese} - \text{Ammortamento}) \cdot (1 - \text{Tax}) + \text{Ammortamento}$$
$$OCF = (800 - 40 - 250) \cdot (1 - 0.35) + 250 = 331.5 + 250 = 581.5$$

## 🏆 Risultati
- **NPV**: **€816,13** (Accettare il progetto poiché NPV > 0)
- **IRR**: **27,21%** (Accettare poiché IRR > Costo del Capitale 10%)
- **Payback Period**: **2,88 anni** (2 anni e circa 322 giorni)

---
**Vedi anche:**
- [[Topic_5_NPV_Investment_Criteria]]
- [[Analisi_di_Sensibilita_e_Scenari]]

## Fonti
* [[raw/f622fc49-8a32-46b5-bf7d-77a21e56ac5b_Chapter_13)_Political_and_Institutional_Limits_to_the_Rise_of_Platform_Work..md]]
* [[wiki/Fonti/Fonte_Sociologia_Digitalizzazione.md]]
