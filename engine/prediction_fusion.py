
class PredictionFusion:
    def fuse(self,predictions,weights=None):
        if not predictions:
            return None
        vals=list(predictions.values())
        if not weights:
            return sum(vals)/len(vals)
        total=sum(weights.values())
        return sum(predictions[k]*weights.get(k,0) for k in predictions)/total
