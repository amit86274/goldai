
from datetime import datetime
import json

class ExperimentTracker:
    def __init__(self):
        self.history=[]

    def log(self,params,metrics):
        run={
            "timestamp":datetime.utcnow().isoformat(),
            "parameters":params,
            "metrics":metrics
        }
        self.history.append(run)

    def save(self,path):
        with open(path,"w") as f:
            json.dump(self.history,f,indent=2)
