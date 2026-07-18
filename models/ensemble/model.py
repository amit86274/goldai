
import numpy as np

class EnsembleModel:
    def __init__(self, models):
        self.models=models

    def predict_proba(self, X):
        probs=[m.predict_proba(X)[:,1] for m in self.models]
        return np.mean(np.vstack(probs), axis=0)

    def predict(self, X, threshold=0.5):
        p=self.predict_proba(X)
        return (p>=threshold).astype(int)
