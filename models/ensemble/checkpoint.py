
import joblib
from pathlib import Path

def save_checkpoint(model, directory, name="ensemble.pkl"):
    Path(directory).mkdir(parents=True, exist_ok=True)
    path=str(Path(directory)/name)
    joblib.dump(model,path)
    return path
