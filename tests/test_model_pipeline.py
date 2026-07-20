import numpy as np
import pytest

from models.xgboost.model import XGBoostModel
from strategy.model_pipeline import ModelSignalPipeline


def test_model_signal_pipeline_uses_model_predictions():
    model = XGBoostModel()
    X = np.array([[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]])
    y = np.array([1, 0])
    model.train(X, y)

    pipeline = ModelSignalPipeline(model=model)
    signal = pipeline.generate_signal(X[0])

    assert signal["action"] in {"BUY", "SELL", "WAIT"}
    assert signal["confidence"] >= 0.0


class ReversedClassesModel:
    classes_ = np.array([1, 0])

    def predict_proba(self, _features):
        return np.array([[0.85, 0.15]])


def test_model_signal_pipeline_uses_the_probability_for_class_one():
    signal = ModelSignalPipeline(ReversedClassesModel()).generate_signal([1.0, 2.0])

    assert signal["action"] == "BUY"
    assert signal["confidence"] == 0.85


def test_model_signal_pipeline_rejects_invalid_thresholds():
    with pytest.raises(ValueError, match="thresholds"):
        ModelSignalPipeline(sell_threshold=0.8, buy_threshold=0.7)
