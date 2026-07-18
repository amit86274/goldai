
import json
from datetime import datetime
class ExperimentTracker:
    def __init__(self): self.history=[]
    def log(self,params,metrics):
        self.history.append({"timestamp":datetime.utcnow().isoformat(),
                             "parameters":params,
                             "metrics":metrics})
    def save(self,path):
        json.dump(self.history,open(path,"w"),indent=2)
