
import numpy as np
def fuse(probabilities,weights=None):
    p=np.asarray(probabilities,float)
    if weights is None:
        return float(p.mean())
    w=np.asarray(weights,float)
    return float((p*w).sum()/w.sum())
