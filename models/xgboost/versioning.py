
from pathlib import Path
from datetime import datetime

def next_version(directory):
    Path(directory).mkdir(parents=True,exist_ok=True)
    return "model_"+datetime.utcnow().strftime("%Y%m%d_%H%M%S")
