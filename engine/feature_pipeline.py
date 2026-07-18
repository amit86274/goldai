
class FeaturePipeline:
    def __init__(self,*steps):
        self.steps=list(steps)
    def transform(self,data):
        for step in self.steps:
            data=step(data)
        return data
