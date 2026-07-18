
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization

class AttentionBlock:
    def __init__(self, heads=8, key_dim=64):
        self.att=MultiHeadAttention(num_heads=heads,key_dim=key_dim)
        self.norm=LayerNormalization()

    def __call__(self,x):
        return self.norm(x+self.att(x,x))
