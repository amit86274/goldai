
from catboost import CatBoostClassifier
from models.base.base_model import BaseModel
from models.base.config import ModelConfig

class CatBoostModel(BaseModel):
    def __init__(self, config=None):
        super().__init__(config or ModelConfig())
        self.model=CatBoostClassifier(
            iterations=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            depth=self.config.max_depth,
            random_seed=self.config.random_seed,
            verbose=False
        )

    def train(self,X_train,y_train,X_valid=None,y_valid=None):
        eval_set=(X_valid,y_valid) if X_valid is not None else None
        self.model.fit(X_train,y_train,eval_set=eval_set)

    def predict(self,X): return self.model.predict(X)
    def predict_proba(self,X): return self.model.predict_proba(X)
    def feature_importance(self): return self.model.get_feature_importance()

    def save(self,path):
        self.model.save_model(path)

    @classmethod
    def load(cls,path):
        obj=cls()
        obj.model.load_model(path)
        return obj
