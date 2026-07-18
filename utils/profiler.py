
import time
class Profiler:
    def __enter__(self):
        self.start=time.perf_counter(); return self
    def __exit__(self,*_):
        self.elapsed=time.perf_counter()-self.start
