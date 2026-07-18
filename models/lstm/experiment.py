import json
from datetime import datetime
class ExperimentTracker:
    def __init__(self): self.history=[]
    def log(self,p,m): self.history.append({"timestamp":datetime.utcnow().isoformat(),"parameters":p,"metrics":m})
    def save(self,path): json.dump(self.history,open(path,"w"),indent=2)
