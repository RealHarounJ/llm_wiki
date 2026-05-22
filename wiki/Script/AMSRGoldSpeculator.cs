#region Using declarations
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Media;
using System.Xml.Serialization;
using NinjaTrader.Cbi;
using NinjaTrader.Gui;
using NinjaTrader.Gui.Chart;
using NinjaTrader.Gui.SuperDom;
using NinjaTrader.Gui.Tools;
using NinjaTrader.NinjaScript;
using NinjaTrader.Data;
using NinjaTrader.NinjaScript.Indicators;
using NinjaTrader.NinjaScript.DrawingTools;
#endregion

// ----------------------------------------------------------------------------------
// 🏆 Strategia Speculativa sull'Oro — Modello AMSR per NinjaTrader 8
// ----------------------------------------------------------------------------------
// Autore: Second Brain Quantitative Assistant
// Descrizione: 
//   1. Esegue il crossover SMA (20 vs 50) per filtrare il trend di fondo.
//   2. Calcola la Median Absolute Deviation (MAD) standardizzata a 20 periodi per
//      estrarre il Robust Z-Score, indicando l'ipercomprato/ipervenduto.
//   3. Interroga in tempo reale il file bridge 'gold_sentiment.txt' generato dal
//      modulo Python per modulare le soglie di ingresso sulla base del sentiment.
//   4. Gestisce in modalità Demo/Simulazione l'inserimento degli ordini con Stop Loss
//      e Take Profit dinamici basati sulla volatilità robusta (MAD).
// ----------------------------------------------------------------------------------
namespace NinjaTrader.NinjaScript.Strategies
{
    [Description("Strategia quantitativa multi-day sull'oro (Modello AMSR) basata su SMA crossover, Robust Z-Score (MAD) e sentiment delle notizie.")]
    public class AMSRGoldSpeculator : Strategy
    {
        private SMA smaFast;
        private SMA smaSlow;

        [NinjaScriptProperty]
        [Range(1, int.MaxValue)]
        [Display(Name="FastWindow", Description="Finestra temporale SMA veloce (Z-Score)", Order=1, GroupName="Parametri AMSR")]
        public int FastWindow { get; set; }

        [NinjaScriptProperty]
        [Range(1, int.MaxValue)]
        [Display(Name="SlowWindow", Description="Finestra temporale SMA lenta (Trend)", Order=2, GroupName="Parametri AMSR")]
        public int SlowWindow { get; set; }

        [NinjaScriptProperty]
        [Range(0.1, 5.0)]
        [Display(Name="ZThreshold", Description="Soglia Z-Score statistica iniziale", Order=3, GroupName="Parametri AMSR")]
        public double ZThreshold { get; set; }

        [NinjaScriptProperty]
        [Display(Name="SentimentFilePath", Description="Percorso assoluto del file gold_sentiment.txt (esportato da Python)", Order=4, GroupName="Parametri AMSR")]
        public string SentimentFilePath { get; set; }

        protected override void OnStateChange()
        {
            if (State == State.SetDefaults)
            {
                Description                                  = "Strategia quantitativa multi-day sull'oro (Modello AMSR) basata su SMA crossover, Robust Z-Score (MAD) e sentiment delle notizie.";
                Name                                         = "AMSRGoldSpeculator";
                Calculate                                    = Calculate.OnBarClose;
                EntriesPerDirection                          = 1;
                EntryHandling                                = EntryHandling.AllEntries;
                IsExitOnSessionCloseStrategy                 = true;
                ExitOnSessionCloseSeconds                    = 30;
                IsFillLimitOnTouch                           = false;
                MaximumBarsLookBack                          = MaximumBarsLookBack.Infinite;
                OrderFillResolution                          = OrderFillResolution.Standard;
                Slippage                                     = 0;
                StartBehavior                                = StartBehavior.WaitUntilFlat;
                TimeInForce                                  = TimeInForce.Gtc;
                RealtimeErrorHandling                        = RealtimeErrorHandling.IgnoreAllErrors;
                
                // Valori di default ottimizzati sul backtest reale
                FastWindow                                   = 20;
                SlowWindow                                   = 50;
                ZThreshold                                   = 1.0;
                SentimentFilePath                            = @"C:\Users\jaafa\Downloads\llm_wiki-main\data\gold_sentiment.txt";
            }
            else if (State == State.DataLoaded)
            {
                // Inizializza gli indicatori tecnici sul grafico
                smaFast = SMA(FastWindow);
                smaSlow = SMA(SlowWindow);
                
                AddChartIndicator(smaFast);
                AddChartIndicator(smaSlow);
            }
        }

        protected override void OnBarUpdate()
        {
            // Assicurati di avere barre sufficienti per calcolare gli indicatori
            if (CurrentBar < SlowWindow)
                return;

            // 1. Calcola la mediana del prezzo a FastWindow periodi
            double[] lastFastPrices = new double[FastWindow];
            for (int i = 0; i < FastWindow; i++)
            {
                lastFastPrices[i] = Close[i];
            }
            double medianPrice = GetMedian(lastFastPrices);

            // 2. Calcola la Median Absolute Deviation (MAD) standardizzata a 20 periodi
            double[] absDeviations = new double[FastWindow];
            for (int i = 0; i < FastWindow; i++)
            {
                absDeviations[i] = Math.Abs(Close[i] - medianPrice);
            }
            double mad = GetMedian(absDeviations);

            // Gaussian consistency factor (1.4826)
            double stdMad = mad * 1.4826;
            if (stdMad < 0.0001) stdMad = 0.0001; // Previene divisioni per zero o valori troppo piccoli

            // 3. Calcola il Robust Z-Score dell'oro
            double zScore = (Close[0] - smaFast[0]) / stdMad;

            // 4. Lettura del sentiment dal file bridge condiviso
            double sentiment = 0.0;
            try
            {
                if (System.IO.File.Exists(SentimentFilePath))
                {
                    string content = System.IO.File.ReadAllText(SentimentFilePath).Trim();
                    // Utilizza InvariantCulture per interpretare correttamente i punti decimali (es. +0.883)
                    sentiment = double.Parse(content, System.Globalization.CultureInfo.InvariantCulture);
                }
            }
            catch (Exception ex)
            {
                // In caso di lock temporaneo del file, continuiamo con sentiment neutro (0.0) per non bloccare NinjaTrader
                Log("AMSR Bridge: Errore lettura sentiment (utilizzo 0.0): " + ex.Message, LogLevel.Warning);
            }

            // 5. Calcola la soglia di Z-Score corretta per il Sentiment (Modulazione)
            double adjustedZThreshold = ZThreshold - (sentiment * 0.3);

            // 6. Calcolo del Trend basato su SMA crossover
            int trend = 0;
            if (smaFast[0] > smaSlow[0])
                trend = 1;  // Bullish (Trend Rialzista)
            else if (smaFast[0] < smaSlow[0])
                trend = -1; // Bearish (Trend Ribassista)

            // 7. Logica Operativa per Demo / Simulatore
            if (Position.MarketPosition == MarketPosition.Flat)
            {
                // INGRESSO LONG: Trend rialzista e Z-Score indica ipervenduto robusto (dip)
                if (trend == 1 && zScore < -adjustedZThreshold)
                {
                    // SL a 2.0 * stdMad e TP a 3.5 * stdMad convertiti in Ticks
                    double slDistance = 2.0 * stdMad;
                    double tpDistance = 3.5 * stdMad;
                    
                    SetStopLoss("LongEntry", CalculationMode.Ticks, slDistance / TickSize, false);
                    SetProfitTarget("LongEntry", CalculationMode.Ticks, tpDistance / TickSize);
                    
                    EnterLong("LongEntry");
                    
                    Print(string.Format("🟢 AMSR LONG ENTRY inviato a ${0} | SL: ${1} (MAD) | TP: ${2} (MAD)", 
                        Close[0], Close[0] - slDistance, Close[0] + tpDistance));
                }
                // INGRESSO SHORT: Trend ribassista e Z-Score indica ipercomprato robusto (peak)
                else if (trend == -1 && zScore > adjustedZThreshold)
                {
                    // SL a 2.0 * stdMad e TP a 3.5 * stdMad convertiti in Ticks
                    double slDistance = 2.0 * stdMad;
                    double tpDistance = 3.5 * stdMad;
                    
                    SetStopLoss("ShortEntry", CalculationMode.Ticks, slDistance / TickSize, false);
                    SetProfitTarget("ShortEntry", CalculationMode.Ticks, tpDistance / TickSize);
                    
                    EnterShort("ShortEntry");
                    
                    Print(string.Format("🔴 AMSR SHORT ENTRY inviato a ${0} | SL: ${1} (MAD) | TP: ${2} (MAD)", 
                        Close[0], Close[0] + slDistance, Close[0] - tpDistance));
                }
            }
            else if (Position.MarketPosition == MarketPosition.Long)
            {
                // USCITA LONG PER INVERSIONE TREND: Se le SMA incrociano al ribasso
                if (trend == -1)
                {
                    ExitLong("LongEntry");
                    Print("⚠️ AMSR LONG EXIT: Chiusura posizione per inversione di trend SMA.");
                }
            }
            else if (Position.MarketPosition == MarketPosition.Short)
            {
                // USCITA SHORT PER INVERSIONE TREND: Se le SMA incrociano al rialzo
                if (trend == 1)
                {
                    ExitShort("ShortEntry");
                    Print("⚠️ AMSR SHORT EXIT: Chiusura posizione per inversione di trend SMA.");
                }
            }
        }

        // Funzione helper matematica per calcolare il valore mediano di un array
        private double GetMedian(double[] sourceNumbers)
        {
            if (sourceNumbers == null || sourceNumbers.Length == 0)
                return 0.0;

            double[] sortedP = (double[])sourceNumbers.Clone();
            Array.Sort(sortedP);

            int size = sortedP.Length;
            int mid = size / 2;
            double median = (size % 2 != 0) ? sortedP[mid] : (sortedP[mid - 1] + sortedP[mid]) / 2.0;
            return median;
        }
    }
}
