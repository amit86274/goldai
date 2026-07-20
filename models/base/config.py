
from dataclasses import dataclass
@dataclass
class ModelConfig:
    random_seed:int=42
    validation_size:float=0.2
    # CPU is the portable default. GPU use must be explicitly enabled on a
    # host with a compatible CUDA/XGBoost installation.
    use_gpu:bool=False
    early_stopping_rounds:int=50
    learning_rate:float=0.05
    max_depth:int=6
    n_estimators:int=500
