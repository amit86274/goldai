
from datetime import datetime
def health():
    return {"status":"ok","time":datetime.utcnow().isoformat()}
