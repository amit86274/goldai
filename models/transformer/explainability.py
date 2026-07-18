
import numpy as np

def feature_sensitivity(model,x,eps=1e-3):
    base=float(model.predict(x,verbose=0).reshape(-1)[0])
    scores=[]
    for i in range(x.shape[-1]):
        xp=np.array(x,copy=True)
        xp[...,i]+=eps
        scores.append(abs(float(model.predict(xp,verbose=0).reshape(-1)[0])-base))
    return scores
