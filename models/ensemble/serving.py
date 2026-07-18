
class EnsembleService:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def infer(self, features):
        return {
            "prediction": self.pipeline.predict(features),
            "probability": self.pipeline.predict_proba(features)
        }
