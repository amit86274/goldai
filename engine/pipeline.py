
class PredictionPipeline:
    def __init__(self,features,manager,ensemble,confidence,signals,decision):
        self.features=features
        self.manager=manager
        self.ensemble=ensemble
        self.confidence=confidence
        self.signals=signals
        self.decision=decision
    def run(self,raw):
        feats=self.features.transform(raw)
        preds=self.manager.predict(feats)
        value=self.ensemble.combine(preds)
        conf=self.confidence.score(preds)
        sig=self.signals.generate(value)
        return {
            "prediction":value,
            "confidence":conf,
            "signal":sig,
            "decision":self.decision.decide(sig,conf)
        }
