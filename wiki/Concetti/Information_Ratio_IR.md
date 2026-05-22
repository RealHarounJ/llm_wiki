---
tags: [concetto, finanza, quantitativa, portfolio-management, risk-adjusted, active-alpha, tracking-error]
aliases: [Information_Ratio, IR, Rapporto_Informativo]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 2
---

# 📊 Information Ratio (IR)

L'**Information Ratio (IR)** è la metrica di performance corretta per il rischio più importante nella gestione attiva del portafoglio (*Active Portfolio Management*). Esso misura la capacità di un gestore o di un modello quantitativo di generare rendimenti in eccesso rispetto ad un benchmark (chiamato anche **Active Alpha** o rendimento residuale) per unità di rischio attivo assunto (chiamato **Active Risk** o **Tracking Error**).

---

## 1. Formulazione Matematica

L'Information Ratio rappresenta l'efficienza della gestione attiva ed è definito come il rapporto tra l'alfa atteso e il tracking error forecast:

$$IR = \frac{\alpha}{\omega}$$

Dove:
- $\alpha$ è il **Rendimento Attivo** o residuale atteso (Active/Residual Return).
- $\omega$ è il **Rischio Residuale** o rischio attivo previsto (Residual Risk / Active Risk o Tracking Error), definito come la deviazione standard del rendimento attivo:
  $$\omega = \sqrt{\text{Var}(R_p - R_b)}$$

### Decomposizione del Rischio Residuale nel CAPM
Secondo la finanza classica (CAPM), il rendimento totale di un portafoglio $R_p$ può essere espresso come:
$$R_p = R_f + \beta_p (R_m - R_f) + \theta_p + \epsilon_p$$

Se definiamo l'alfa residuale $\alpha_p$ come la sovraperformance corretta per il beta, il rischio residuale $\omega$ misura la variabilità di $\epsilon_p$ (ovvero la componente non sistematica e diversificabile del portafoglio):
$$\omega = \text{StDev}(\epsilon_p)$$

---

## 2. Ex-Ante vs. Ex-Post Information Ratio

È fondamentale distinguere la componente decisionale (ex-ante) dai risultati effettivi registrati (ex-post):

### A. Ex-Ante Information Ratio
Utilizzato nella fase di costruzione del portafoglio. È basato sulle previsioni (*forecasts*) di rendimento e di rischio:
$$IR_{\text{ex-ante}} = \frac{\alpha_{\text{expected}}}{\omega_{\text{forecast}}}$$
Questo rapporto esprime le aspettative del gestore o le predizioni dell'algoritmo quantitativo prima dell'esecuzione sul mercato.

### B. Ex-Post Information Ratio
Misurato storicamente a partire dai dati realizzati. Valuta la reale performance storica di un fondo o di un modello:
$$IR_{\text{ex-post}} = \frac{\overline{R}_p - \overline{R}_b}{\text{StDev}(R_p - R_b)} = \frac{\text{Rendimento Attivo Medio Realizzato}}{\text{Tracking Error Storico}}$$
L'IR storico indica quanta sovraperformance costante il modello è stato in grado di estrarre per ogni punto percentuale di deviazione dal benchmark.

---

## 3. Confronto: Sharpe Ratio vs. Information Ratio

Sebbene siano simili nella struttura, lo Sharpe Ratio e l'Information Ratio rispondono a domande d'investimento differenti:

| Caratteristica | Sharpe Ratio (SR) | Information Ratio (IR) |
|---|---|---|
| **Punto di Riferimento** | Tasso privo di rischio ($R_f$) | Portafoglio di Benchmark ($R_b$) |
| **Numeratore** | Excess Return ($R_p - R_f$) | Active Return / Alpha ($R_p - R_b$) |
| **Denominatore** | Rischio Totale ($\sigma_p$) | Rischio Attivo / Tracking Error ($\omega$) |
| **Obiettivo** | Valutare l'efficienza di un portafoglio totale (es. investitore globale). | Valutare l'efficienza del gestore attivo rispetto ad un indice specifico. |
| **Formula** | $$SR = \frac{R_p - R_f}{\sigma_p}$$ | $$IR = \frac{R_p - R_b}{\omega}$$ |

> [!NOTE]
> Quando il benchmark di riferimento dell'Information Ratio coincide esattamente con il tasso risk-free ($R_b = R_f$), l'Information Ratio si riduce matematicamente allo Sharpe Ratio.

---

## 4. Distribuzione Empirica dell'IR (Standard di Grinold)

Nelle gestioni quantitative professionali, l'Information Ratio è la metrica fondamentale per valutare se un modello ha un vantaggio competitivo reale (*alpha mojo*). Grinold & Kahn propongono una scala empirica per valutare la consistenza dell'IR su base annuale:

- **$IR = 0.50$ (Buono)**: Colloca il gestore nel primo quartile (top 25%) dei fondi istituzionali. È un traguardo eccellente per modelli quantitativi robusti.
- **$IR = 1.00$ (Eccezionale)**: Riservato al top 1% dei gestori attivi. Indica una capacità predittiva straordinaria e costante.
- **$IR = 2.00$ (Sovrumano / Sospetto)**: Quasi mai realizzabile nel lungo termine su mercati liquidi ed efficienti. Se si riscontra in una simulazione di backtesting, indica solitamente un errore sistematico (es. *data leakage*, assenza di costi di transazione modellizzati o overfitting).

---

## Fonti
* [[wiki/Fonti/Fonte_Grinold_Kahn_APM.md]]
* [[wiki/Fonti/Fonte_Chincarini_QEPM.md]]
* [[wiki/Concetti/Topic_6_Risk_and_Return.md]]
