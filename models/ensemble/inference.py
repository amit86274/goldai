
class InferenceEngine:
    def __init__(self,ensemble):
        self.ensemble=ensemble

    def predict_one(self,features):
        prob=float(self.ensemble.predict_proba(features)[0])
        return {
            "prediction":int(prob>=0.5),
            "probability":prob
        }
