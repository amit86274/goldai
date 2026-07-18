
from datetime import datetime

class AuditLogger:
    def __init__(self):
        self.records=[]
    def log(self, action, details):
        self.records.append({
            "time": datetime.utcnow().isoformat(),
            "action": action,
            "details": details
        })
