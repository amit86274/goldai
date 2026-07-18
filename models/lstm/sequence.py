
import numpy as np
def create_sequences(X,y,window):
    xs,ys=[],[]
    for i in range(len(X)-window):
        xs.append(X[i:i+window])
        ys.append(y[i+window])
    return np.asarray(xs),np.asarray(ys)
