
import time

class AlertThrottle:
    def __init__(self):
        self._last={}
    def allow(self,key,interval=60):
        now=time.time()
        last=self._last.get(key,0)
        if now-last>=interval:
            self._last[key]=now
            return True
        return False
