
class EnsemblePipeline:
    def __init__(self, registry, ensemble):
        self.registry = registry
        self.ensemble = ensemble

    def predict(self, X):
        return self.ensemble.predict(X)

    def predict_proba(self, X):
        return self.ensemble.predict_proba(X)
