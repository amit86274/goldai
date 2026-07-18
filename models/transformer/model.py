
from tensorflow.keras import Model
from tensorflow.keras.layers import Input,Dense,LayerNormalization,Dropout,MultiHeadAttention,GlobalAveragePooling1D

class TransformerModel(Model):
    def __init__(self, features, heads=4, d_model=64, ff_dim=128):
        super().__init__()
        self.att=MultiHeadAttention(num_heads=heads,key_dim=d_model)
        self.norm1=LayerNormalization()
        self.ff1=Dense(ff_dim,activation="relu")
        self.ff2=Dense(d_model)
        self.norm2=LayerNormalization()
        self.pool=GlobalAveragePooling1D()
        self.drop=Dropout(0.2)
        self.out=Dense(1,activation="sigmoid")

    def call(self,x):
        a=self.att(x,x)
        x=self.norm1(x+a)
        f=self.ff2(self.ff1(x))
        x=self.norm2(x+f)
        x=self.pool(x)
        x=self.drop(x)
        return self.out(x)
