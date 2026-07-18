
from pathlib import Path

def save_checkpoint(model,directory,name="best_model.json"):
    Path(directory).mkdir(parents=True,exist_ok=True)
    path=str(Path(directory)/name)
    model.save(path)
    return path
