
import time
class RateLimiter:
    def __init__(self,interval):
        self.interval=interval; self.last=0
    def allow(self):
        now=time.time()
        if now-self.last>=self.interval:
            self.last=now; return True
        return False
