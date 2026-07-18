
from datetime import datetime

def next_version():
    return "catboost_"+datetime.utcnow().strftime("%Y%m%d_%H%M%S")
