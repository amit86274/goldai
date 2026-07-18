
import importlib

def gpu_available():
    return importlib.util.find_spec("cupy") is not None
