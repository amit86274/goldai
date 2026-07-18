
from lightgbm import LGBMClassifier
from models.base.base_model import BaseModel
from models.base.config import ModelConfig

class LightGBMModel(BaseModel):
    def __init__(self, config=None):
        super().__init__(config or ModelConfig())
        self.model=LGBMClassifier(
            n_estimators=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            max_depth=self.config.max_depth,
            random_state=self.config.random_seed
        )

    def train(self,X_train,y_train,X_valid=None,y_valid=None):
        eval_set=[(X_valid,y_valid)] if X_valid is not None else None
        self.model.fit(X_train,y_train,eval_set=eval_set)

    def predict(self,X): return self.model.predict(X)
    def predict_proba(self,X): return self.model.predict_proba(X)
    def feature_importance(self): return self.model.feature_importances_
    def save(self,path):
        import joblib; joblib.dump(self.model,path)
    @classmethod
    def load(cls,path):
        import joblib
        obj=cls()
        obj.model=joblib.load(path)
        return obj
