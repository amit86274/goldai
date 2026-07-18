
from datetime import datetime,timedelta
def is_breaking(ts,minutes=30):
    return datetime.utcnow()-ts<=timedelta(minutes=minutes)
