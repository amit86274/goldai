
from tensorflow.keras import mixed_precision

def enable():
    mixed_precision.set_global_policy("mixed_float16")
