
import numpy as np

def update_weights(metrics, eps=1e-9):
    scores = np.asarray(metrics, dtype=float)
    scores = np.maximum(scores, eps)
    return (scores / scores.sum()).tolist()
