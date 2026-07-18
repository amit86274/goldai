
class XGBoostPredictor:
    def __init__(self,model):
        self.model=model
    def predict(self,X):
        return self.model.predict(X)
    def predict_proba(self,X):
        return self.model.predict_proba(X)
