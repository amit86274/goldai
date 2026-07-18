class LSTMTrainer:
    def __init__(self,m): self.model=m
    def fit(self,*a): self.model.train(*a); return self.model
