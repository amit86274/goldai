import numpy as np
class InferenceEngine:
    def __init__(self,m): self.model=m
    def predict_one(self,seq):
        x=np.asarray(seq).reshape(1,*np.asarray(seq).shape)
        p=float(self.model.predict_proba(x).reshape(-1)[0])
        return {"prediction":int(p>0.5),"probability":p}
