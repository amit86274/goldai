from __future__ import annotations

from typing import Any, Dict

import numpy as np


class ModelSignalPipeline:
    def __init__(self, model: Any | None = None) -> None:
        self.model = model

    def generate_signal(self, features: Any) -> Dict[str, Any]:
        if self.model is None:
            return {"action": "WAIT", "confidence": 0.0, "reason": "model unavailable"}

        array = np.asarray(features, dtype=float).reshape(1, -1)
        if not hasattr(self.model, "predict_proba"):
            return {"action": "WAIT", "confidence": 0.0, "reason": "model has no probability interface"}

        probabilities = self.model.predict_proba(array)[0]
        positive_prob = float(probabilities[1]) if len(probabilities) > 1 else float(probabilities[0])

        if positive_prob >= 0.7:
            return {"action": "BUY", "confidence": positive_prob, "reason": "model probability"}
        if positive_prob <= 0.3:
            return {"action": "SELL", "confidence": 1.0 - positive_prob, "reason": "model probability"}
        return {"action": "WAIT", "confidence": abs(0.5 - positive_prob) * 2.0, "reason": "model probability"}
