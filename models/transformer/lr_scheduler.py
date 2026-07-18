
from tensorflow.keras.callbacks import ReduceLROnPlateau

def callback():
    return ReduceLROnPlateau(monitor="val_loss",factor=0.5,patience=3)
