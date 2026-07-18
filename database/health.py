
from datetime import datetime

def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }
