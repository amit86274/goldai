
import time

class PerformanceMonitor:
    def measure(self, func, *args, **kwargs):
        start=time.perf_counter()
        result=func(*args, **kwargs)
        return {"result":result,"elapsed":time.perf_counter()-start}
