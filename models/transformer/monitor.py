
import time

class ModelMonitor:
    def __init__(self):
        self.calls=0
    def log(self):
        self.calls+=1
        return {"calls":self.calls,"timestamp":time.time()}
