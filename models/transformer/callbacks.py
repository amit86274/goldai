
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint

def default_callbacks(path="transformer.keras"):
    return [
        EarlyStopping(patience=5,restore_best_weights=True),
        ModelCheckpoint(path,save_best_only=True)
    ]
