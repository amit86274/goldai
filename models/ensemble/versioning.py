
from datetime import datetime
def next_version():
    return "ensemble_"+datetime.utcnow().strftime("%Y%m%d_%H%M%S")
