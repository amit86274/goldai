
class RetrainingManager:
    def __init__(self,pipeline):
        self.pipeline=pipeline

    def retrain(self,*args,**kwargs):
        return self.pipeline.run(*args,**kwargs)
