
class PredictionService:
    def __init__(self,inference_engine):
        self.engine=inference_engine

    def predict(self,features):
        return self.engine.predict_one(features)
