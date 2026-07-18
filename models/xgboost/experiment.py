
import json
from datetime import datetime

class ExperimentTracker:
    def __init__(self):
        self.runs=[]

    def log(self,params,metrics):
        run={
            "timestamp":datetime.utcnow().isoformat(),
            "parameters":params,
            "metrics":metrics
        }
        self.runs.append(run)
        return run

    def save(self,path):
        with open(path,"w") as f:
            json.dump(self.runs,f,indent=2)
