
from abc import ABC, abstractmethod
from .config import ModelConfig
class BaseModel(ABC):
    def __init__(self,config=None):
        self.config=config or ModelConfig()
    @abstractmethod
    def train(self,*args,**kwargs): ...
    @abstractmethod
    def predict(self,X): ...
    @abstractmethod
    def predict_proba(self,X): ...
    @abstractmethod
    def save(self,path): ...
    @classmethod
    @abstractmethod
    def load(cls,path): ...
