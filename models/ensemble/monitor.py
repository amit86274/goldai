
import time

class EnsembleMonitor:
    def __init__(self):
        self.requests = 0

    def log_request(self):
        self.requests += 1
        return {
            "requests": self.requests,
            "timestamp": time.time()
        }
