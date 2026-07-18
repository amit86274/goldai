
class EnsemblePredictor:
    def __init__(self, ensemble):
        self.ensemble=ensemble

    def predict(self, X):
        return self.ensemble.predict(X)

    def predict_proba(self, X):
        return self.ensemble.predict_proba(X)
