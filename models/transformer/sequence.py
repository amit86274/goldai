
import numpy as np

def create_windows(data,window):
    return np.asarray([data[i:i+window] for i in range(len(data)-window)])
