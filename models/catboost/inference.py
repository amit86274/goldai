
import numpy as np

class InferenceEngine:
    def __init__(self, model):
        self.model=model

    def predict_one(self, features):
        x=np.asarray(features).reshape(1,-1)
        return {
            "prediction": int(self.model.predict(x)[0]),
            "probability": self.model.predict_proba(x)[0].tolist()
        }
