"""Model training utilities."""
from __future__ import annotations
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self, model):
        self.model=model

    def train(self, X, y, test_size=0.2, random_state=42):
        X_train,X_test,y_train,y_test=train_test_split(
            X,y,test_size=test_size,random_state=random_state,shuffle=False
        )
        self.model.fit(X_train,y_train)
        preds=self.model.predict(X_test)
        return {
            "accuracy": accuracy_score(y_test,preds),
            "samples": len(y_test)
        }

    def save(self,path:str):
        joblib.dump(self.model,path)
