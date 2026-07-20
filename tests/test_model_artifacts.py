import os
import tempfile

from models.predictor import Predictor
from models.xgboost.model import XGBoostModel


def test_predictor_loads_saved_model_artifact():
    model = XGBoostModel()
    X = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]]
    y = [1, 0]
    model.train(X, y)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "model.json")
        model.save(path)
        predictor = Predictor(path)
        prediction = predictor.predict_proba([[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]])
        assert prediction is not None
