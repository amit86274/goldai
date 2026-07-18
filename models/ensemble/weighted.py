
import numpy as np

def weighted_average(probabilities, weights):
    probs=np.asarray(probabilities)
    w=np.asarray(weights).reshape(-1,1)
    return (probs*w).sum(axis=0)/w.sum()
