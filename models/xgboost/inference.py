
import numpy as np

class InferenceEngine:
    def __init__(self,model):
        self.model=model

    def predict_one(self,row):
        arr=np.asarray(row).reshape(1,-1)
        pred=self.model.predict(arr)[0]
        prob=self.model.predict_proba(arr)[0]
        return {"prediction":int(pred),"probability":prob.tolist()}
