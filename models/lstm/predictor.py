class LSTMPredictor:
    def __init__(self,m): self.model=m
    def predict(self,X): return self.model.predict(X)
    def predict_proba(self,X): return self.model.predict_proba(X)
