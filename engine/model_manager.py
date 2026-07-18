
class ModelManager:
    def __init__(self):
        self.models={}
    def register(self,name,model):
        self.models[name]=model
    def predict(self,features):
        return {n:m.predict(features) for n,m in self.models.items() if hasattr(m,"predict")}
