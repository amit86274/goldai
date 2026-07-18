
import numpy as np

def majority_vote(predictions):
    preds=np.asarray(predictions)
    return (preds.mean(axis=0)>=0.5).astype(int)
