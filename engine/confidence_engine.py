
class ConfidenceEngine:
    def score(self,predictions):
        if not predictions:
            return 0.0
        vals=list(predictions.values())
        spread=max(vals)-min(vals)
        return max(0.0,1.0-spread)
