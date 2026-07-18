
from datetime import datetime

def build_system_alert(level, message):
    return {
        "type": "system",
        "level": level,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }
