
from dataclasses import dataclass
@dataclass
class ModelConfig:
    random_seed:int=42
    validation_size:float=0.2
    use_gpu:bool=True
    early_stopping_rounds:int=50
    learning_rate:float=0.05
    max_depth:int=6
    n_estimators:int=500
