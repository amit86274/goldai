
import time

class LatencyMonitor:
    def measure(self, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return {
            "latency_ms": (time.perf_counter() - start) * 1000,
            "result": result
        }
