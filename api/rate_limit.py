
import time

class RateLimiter:
    def __init__(self):
        self._requests = {}

    def allow(self, key, limit=60, window=60):
        now = time.time()
        history = [t for t in self._requests.get(key, []) if now - t < window]
        if len(history) >= limit:
            return False
        history.append(now)
        self._requests[key] = history
        return True
