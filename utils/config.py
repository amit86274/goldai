
import os

class Config:
    def get(self, key, default=None):
        return os.getenv(key, default)
