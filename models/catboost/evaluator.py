
from models.base.metrics import classification_metrics

def evaluate(model,X,y):
    pred=model.predict(X)
    prob=model.predict_proba(X)[:,1]
    return classification_metrics(y,pred,prob)
