
import numpy as np

def merge_sequences(*arrays):
    return np.concatenate(arrays,axis=-1)
