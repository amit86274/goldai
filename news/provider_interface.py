from abc import ABC, abstractmethod

class NewsProvider(ABC):
    @abstractmethod
    def fetch(self):
        raise NotImplementedError
