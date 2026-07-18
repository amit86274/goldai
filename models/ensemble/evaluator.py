
from models.base.metrics import classification_metrics
import numpy as np

def evaluate(model, X, y):
    prob=np.asarray(model.predict_proba(X)).reshape(-1)
    pred=(prob>=0.5).astype(int)
    return classification_metrics(y,pred,prob)
