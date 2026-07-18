
class EnsembleCoordinator:
    def combine(self,predictions):
        if not predictions:
            return None
        vals=list(predictions.values())
        return sum(vals)/len(vals)
