
import numpy as np

def compute_weights(scores):
    s=np.asarray(scores,dtype=float)
    s=s/s.sum() if s.sum()>0 else np.ones_like(s)/len(s)
    return s
