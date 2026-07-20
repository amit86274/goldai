"""Prediction helpers."""
from __future__ import annotations

import joblib
from pathlib import Path

from xgboost import XGBClassifier


class Predictor:
    def __init__(self, model_path: str):
        path = Path(model_path)
        if path.suffix in {".json", ".model"}:
            self.model = XGBClassifier()
            self.model.load_model(str(path))
        else:
            self.model = joblib.load(path)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X)
        return None
