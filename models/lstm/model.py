
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from models.base.base_model import BaseModel
from models.base.config import ModelConfig

class LSTMModel(BaseModel):
    def __init__(self, config=None):
        super().__init__(config or ModelConfig())
        self.model=Sequential([
            LSTM(64, return_sequences=True),
            Dropout(0.2),
            LSTM(32),
            Dense(1, activation="sigmoid")
        ])
        self.model.compile(optimizer="adam",
                           loss="binary_crossentropy",
                           metrics=["accuracy"])

    def train(self,X_train,y_train,X_valid=None,y_valid=None):
        val=(X_valid,y_valid) if X_valid is not None else None
        self.model.fit(X_train,y_train,
                       validation_data=val,
                       epochs=20,
                       batch_size=32,
                       verbose=0)

    def predict(self,X):
        return (self.model.predict(X,verbose=0)>0.5).astype(int)

    def predict_proba(self,X):
        return self.model.predict(X,verbose=0)

    def feature_importance(self):
        return None

    def save(self,path):
        self.model.save(path)

    @classmethod
    def load(cls,path):
        from tensorflow.keras.models import load_model
        obj=cls()
        obj.model=load_model(path)
        return obj
