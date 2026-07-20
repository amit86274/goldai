from __future__ import annotations

from typing import Any, Dict

import numpy as np


class ModelSignalPipeline:
    """Convert binary classifier probabilities into trading signals."""

    def __init__(
        self,
        model: Any | None = None,
        buy_threshold: float = 0.7,
        sell_threshold: float = 0.3,
    ) -> None:
        if not 0.0 <= sell_threshold < buy_threshold <= 1.0:
            raise ValueError("thresholds must satisfy 0 <= sell < buy <= 1")
        self.model = model
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def generate_signal(self, features: Any) -> Dict[str, Any]:
        if self.model is None:
            return {"action": "WAIT", "confidence": 0.0, "reason": "model unavailable"}

        try:
            array = np.asarray(features, dtype=float).reshape(1, -1)
        except (TypeError, ValueError):
            return {"action": "WAIT", "confidence": 0.0, "reason": "invalid model features"}
        if not hasattr(self.model, "predict_proba"):
            return {"action": "WAIT", "confidence": 0.0, "reason": "model has no probability interface"}

        try:
            probabilities = np.asarray(self.model.predict_proba(array), dtype=float)
        except (TypeError, ValueError):
            return {"action": "WAIT", "confidence": 0.0, "reason": "invalid model probabilities"}
        if probabilities.ndim != 2 or probabilities.shape[0] != 1:
            return {"action": "WAIT", "confidence": 0.0, "reason": "invalid model probabilities"}

        positive_prob = self._positive_probability(probabilities[0])
        if not 0.0 <= positive_prob <= 1.0:
            return {"action": "WAIT", "confidence": 0.0, "reason": "invalid model probability"}

        if positive_prob >= self.buy_threshold:
            return {"action": "BUY", "confidence": positive_prob, "reason": "model probability"}
        if positive_prob <= self.sell_threshold:
            return {"action": "SELL", "confidence": 1.0 - positive_prob, "reason": "model probability"}
        return {"action": "WAIT", "confidence": abs(0.5 - positive_prob) * 2.0, "reason": "model probability"}

    def _positive_probability(self, probabilities: np.ndarray) -> float:
        """Return the probability for class ``1`` when class labels are exposed."""
        classes = getattr(self.model, "classes_", None)
        if classes is not None:
            matches = np.flatnonzero(np.asarray(classes) == 1)
            if len(matches) == 1 and matches[0] < len(probabilities):
                return float(probabilities[matches[0]])

        # sklearn binary classifiers conventionally expose [negative, positive].
        return float(probabilities[1]) if len(probabilities) > 1 else float(probabilities[0])
