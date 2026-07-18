
from datetime import datetime
class HealthMonitor:
    def status(self,connected):
        return {"connected":connected,"timestamp":datetime.utcnow().isoformat()}
