
from datetime import datetime
def health(status="OK"):
    return {"status":status,"timestamp":datetime.utcnow().isoformat()}
