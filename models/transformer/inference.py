
import numpy as np
class InferenceEngine:
    def __init__(self,model): self.model=model
    def predict_one(self,sequence):
        x=np.asarray(sequence).reshape(1,*np.asarray(sequence).shape)
        p=float(self.model.predict(x,verbose=0).reshape(-1)[0])
        return {"prediction":int(p>0.5),"probability":p}
