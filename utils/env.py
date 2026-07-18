
from os import getenv

def load_env(key, default=None):
    return getenv(key, default)
