
class RetrainingManager:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def retrain(self, X_train, y_train, X_valid, y_valid):
        return self.pipeline.run(X_train, y_train, X_valid, y_valid)
