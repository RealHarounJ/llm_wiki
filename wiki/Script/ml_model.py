#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMSR ML Adaptive Model
Modello di Machine Learning che impara dai trade passati per prevedere
se una determinata combinazione delle 47 variabili umane porterà a un profitto (TP) o perdita (SL).
Utilizza RandomForestClassifier (se sklearn è installato) o un fallback in Numpy (Logistic Regression).
"""

import os
import json
import numpy as np
from pathlib import Path

# Tentativo di importazione librerie avanzate
HAS_ML_LIBS = False
try:
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    HAS_ML_LIBS = True
except ImportError:
    pass

MODEL_PATH = Path("data/ml_model.pkl")
FALLBACK_MODEL_PATH = Path("data/ml_fallback_weights.json")
HISTORY_PATH = Path("data/feature_history.csv")

class PureNumpyLogisticRegression:
    """
    Modello di regressione logistica multi-classe implementato in puro NumPy
    come fallback se scikit-learn non è installato.
    """
    def __init__(self, input_dim=47, num_classes=3, lr=0.01, epochs=100):
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.lr = lr
        self.epochs = epochs
        # Inizializza pesi e bias
        self.weights = np.zeros((input_dim, num_classes))
        self.bias = np.zeros(num_classes)
        
    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
        
    def fit(self, X, y):
        # Converti y in one-hot
        num_samples = X.shape[0]
        y_onehot = np.zeros((num_samples, self.num_classes))
        # Mappa i target (-1, 0, 1) a indici (0, 1, 2)
        y_mapped = y + 1 
        y_onehot[np.arange(num_samples), y_mapped] = 1
        
        # Standardizzazione interna delle features
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0) + 1e-9
        X_scaled = (X - self.mean) / self.std
        
        # Gradient Descent
        for _ in range(self.epochs):
            scores = np.dot(X_scaled, self.weights) + self.bias
            probs = self.softmax(scores)
            
            # Calcolo gradienti
            dw = (1.0 / num_samples) * np.dot(X_scaled.T, (probs - y_onehot))
            db = (1.0 / num_samples) * np.sum(probs - y_onehot, axis=0)
            
            # Aggiornamento
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict_proba(self, X):
        X_scaled = (X - self.mean) / self.std
        scores = np.dot(X_scaled, self.weights) + self.bias
        return self.softmax(scores)
        
    def predict(self, X):
        probs = self.predict_proba(X)
        indices = np.argmax(probs, axis=1)
        return indices - 1 # rimappa a (-1, 0, 1)

    def save(self, filepath):
        data = {
            "weights": self.weights.tolist(),
            "bias": self.bias.tolist(),
            "mean": self.mean.tolist(),
            "std": self.std.tolist(),
            "input_dim": self.input_dim,
            "num_classes": self.num_classes
        }
        with open(filepath, "w") as f:
            json.dump(data, f)
            
    def load(self, filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
        self.weights = np.array(data["weights"])
        self.bias = np.array(data["bias"])
        self.mean = np.array(data["mean"])
        self.std = np.array(data["std"])
        self.input_dim = data["input_dim"]
        self.num_classes = data["num_classes"]

class AdaptiveMLModel:
    """
    Gestisce il training adattivo e la predizione dei segnali.
    """
    def __init__(self, feature_keys):
        self.feature_keys = sorted(feature_keys)
        self.num_features = len(self.feature_keys)
        self.model = None
        self.fallback_model = None
        self.is_trained = False
        self.load_model()
        
    def load_model(self):
        """Carica il modello dal disco se esiste."""
        if HAS_ML_LIBS and MODEL_PATH.exists():
            try:
                self.model = joblib.load(MODEL_PATH)
                self.is_trained = True
                print("[ML] Modello Random Forest caricato con successo.")
                return
            except Exception as e:
                print(f"[ML] Errore nel caricamento del modello Random Forest: {e}")
                
        if FALLBACK_MODEL_PATH.exists():
            try:
                self.fallback_model = PureNumpyLogisticRegression(input_dim=self.num_features)
                self.fallback_model.load(FALLBACK_MODEL_PATH)
                self.is_trained = True
                print("[ML] Modello Fallback NumPy caricato con successo.")
            except Exception as e:
                print(f"[ML] Errore nel caricamento del modello Fallback NumPy: {e}")

    def save_model(self):
        """Salva il modello corrente sul disco."""
        os.makedirs("data", exist_ok=True)
        if HAS_ML_LIBS and self.model is not None:
            try:
                joblib.dump(self.model, MODEL_PATH)
                print(f"[ML] Modello Random Forest salvato in {MODEL_PATH}")
                return
            except Exception as e:
                print(f"[ML] Errore nel salvataggio del modello Random Forest: {e}")
                
        if self.fallback_model is not None:
            try:
                self.fallback_model.save(FALLBACK_MODEL_PATH)
                print(f"[ML] Modello Fallback NumPy salvato in {FALLBACK_MODEL_PATH}")
            except Exception as e:
                print(f"[ML] Errore nel salvataggio del modello Fallback NumPy: {e}")

    def add_to_history(self, symbol, features, label):
        """
        Salva le feature calcolate e la label (-1, 0, 1) nel database storico.
        Utilizza il Triple-Barrier Method di Lopez de Prado.
        """
        os.makedirs("data", exist_ok=True)
        # Ordina le feature nello stesso ordine delle keys del modello
        row_data = [symbol, label]
        for key in self.feature_keys:
            row_data.append(features.get(key, 0.0))
            
        # Scrittura su file CSV
        file_exists = HISTORY_PATH.exists()
        try:
            with open(HISTORY_PATH, "a", encoding="utf-8") as f:
                if not file_exists:
                    # Scrivi header
                    header = "symbol,label," + ",".join(self.feature_keys) + "\n"
                    f.write(header)
                row_str = ",".join(map(str, row_data)) + "\n"
                f.write(row_str)
        except Exception as e:
            print(f"[ML ERROR] Impossibile salvare storico feature: {e}")

    def train(self):
        """
        Addestra il modello sui dati storici salvati in data/feature_history.csv.
        """
        if not HISTORY_PATH.exists():
            print("[ML] Nessun dato storico trovato per il training.")
            return False
            
        try:
            if HAS_ML_LIBS:
                df = pd.read_csv(HISTORY_PATH)
                if len(df) < 50:
                    print(f"[ML] Dati insufficienti per il training ({len(df)}/50). Attendo accumulo dati.")
                    return False
                    
                X = df[self.feature_keys].values
                y = df["label"].values
                
                # Allena Random Forest
                self.model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
                self.model.fit(X, y)
                self.is_trained = True
                self.save_model()
                print(f"[ML] Training completato con successo su {len(df)} campioni.")
                return True
            else:
                # Fallback NumPy
                # Legge il CSV manualmente senza pandas
                X_list = []
                y_list = []
                with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                if len(lines) < 30: # 1 header + 29 campioni
                    print(f"[ML Fallback] Dati insufficienti ({len(lines)-1}/30).")
                    return False
                    
                header = lines[0].strip().split(',')
                feat_indices = [header.index(k) for k in self.feature_keys]
                label_idx = header.index("label")
                
                for line in lines[1:]:
                    parts = line.strip().split(',')
                    if len(parts) < len(header):
                        continue
                    try:
                        y_val = int(parts[label_idx])
                        x_vals = [float(parts[idx]) for idx in feat_indices]
                        X_list.append(x_vals)
                        y_list.append(y_val)
                    except ValueError:
                        continue
                        
                X = np.array(X_list)
                y = np.array(y_list)
                
                self.fallback_model = PureNumpyLogisticRegression(input_dim=self.num_features)
                self.fallback_model.fit(X, y)
                self.is_trained = True
                self.save_model()
                print(f"[ML Fallback] Training completato con successo su {len(X)} campioni.")
                return True
                
        except Exception as e:
            print(f"[ML ERROR] Errore nel training: {e}")
            return False

    def predict(self, features):
        """
        Predice il label futuro per la configurazione corrente di features.
        Restituisce:
          +1: segnale rialzista forte (TP atteso)
          -1: segnale ribassista forte (SL atteso se long)
           0: segnale neutro / timeout
        """
        if not self.is_trained:
            return 0 # Modello non addestrato
            
        try:
            # Estrae features ordinate
            x_vals = []
            for key in self.feature_keys:
                x_vals.append(features.get(key, 0.0))
            X_input = np.array([x_vals])
            
            if HAS_ML_LIBS and self.model is not None:
                pred = self.model.predict(X_input)[0]
                return int(pred)
            elif self.fallback_model is not None:
                pred = self.fallback_model.predict(X_input)[0]
                return int(pred)
            return 0
        except Exception as e:
            print(f"[ML ERROR] Errore nella predizione: {e}")
            return 0
            
    def predict_probability(self, features):
        """
        Restituisce le probabilità associate a ciascuna classe (-1, 0, 1).
        Utile per determinare la confidenza della predizione ML.
        """
        if not self.is_trained:
            return [0.33, 0.34, 0.33]
            
        try:
            x_vals = []
            for key in self.feature_keys:
                x_vals.append(features.get(key, 0.0))
            X_input = np.array([x_vals])
            
            if HAS_ML_LIBS and self.model is not None:
                probs = self.model.predict_proba(X_input)[0]
                # Mappa le probabilità in ordine [-1, 0, 1]
                classes = list(self.model.classes_)
                ordered_probs = [0.0, 0.0, 0.0]
                for idx, cls in enumerate(classes):
                    mapped_idx = int(cls) + 1
                    ordered_probs[mapped_idx] = float(probs[idx])
                return ordered_probs
            elif self.fallback_model is not None:
                probs = self.fallback_model.predict_proba(X_input)[0]
                return [float(p) for p in probs]
            return [0.33, 0.34, 0.33]
        except Exception as e:
            print(f"[ML ERROR] Errore nel calcolo delle probabilità ML: {e}")
            return [0.33, 0.34, 0.33]
