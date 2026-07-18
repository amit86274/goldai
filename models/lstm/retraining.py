class RetrainingManager:
    def __init__(self,p): self.pipeline=p
    def retrain(self,*a): return self.pipeline.run(*a)
