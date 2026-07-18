"""Prediction helpers."""
from __future__ import annotations
import joblib

class Predictor:
    def __init__(self, model_path:str):
        self.model=joblib.load(model_path)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        if hasattr(self.model,"predict_proba"):
            return self.model.predict_proba(X)
        return None
