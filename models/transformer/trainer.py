
class TransformerTrainer:
    def __init__(self,model):
        self.model=model
    def fit(self,*args,**kwargs):
        return self.model.fit(*args,**kwargs)
