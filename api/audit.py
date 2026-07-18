
from datetime import datetime

class APILogger:
    def log(self, endpoint, method, status):
        return {
            "time": datetime.utcnow().isoformat(),
            "endpoint": endpoint,
            "method": method,
            "status": status
        }
