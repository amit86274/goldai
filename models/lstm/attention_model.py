
from tensorflow.keras.layers import Input,LSTM,Dense,Dropout,Attention
from tensorflow.keras.models import Model

def build_attention_lstm(timesteps, features, units=64):
    inp=Input(shape=(timesteps,features))
    x=LSTM(units, return_sequences=True)(inp)
    x=Attention()([x,x])
    x=LSTM(units//2)(x)
    x=Dropout(0.2)(x)
    out=Dense(1,activation="sigmoid")(x)
    model=Model(inp,out)
    model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
    return model
