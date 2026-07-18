
class LightGBMTrainer:
    def __init__(self,model):
        self.model=model
    def fit(self,X_train,y_train,X_valid=None,y_valid=None):
        self.model.train(X_train,y_train,X_valid,y_valid)
        return self.model
