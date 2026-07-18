
from sklearn.linear_model import LogisticRegression

class StackingClassifier:
    def __init__(self):
        self.meta=LogisticRegression()

    def fit(self, base_predictions, y):
        self.meta.fit(base_predictions, y)

    def predict(self, base_predictions):
        return self.meta.predict(base_predictions)

    def predict_proba(self, base_predictions):
        return self.meta.predict_proba(base_predictions)
