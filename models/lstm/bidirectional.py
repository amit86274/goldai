
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional,LSTM,Dense

def build_bidirectional(units=64):
    model=Sequential([
        Bidirectional(LSTM(units)),
        Dense(1,activation="sigmoid")
    ])
    model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
    return model
