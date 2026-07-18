
import os
from xgboost import XGBClassifier
from models.base.base_model import BaseModel
from models.base.config import ModelConfig

class XGBoostModel(BaseModel):
    def __init__(self, config=None):
        super().__init__(config or ModelConfig())
        tree_method="hist"
        device="cuda" if self.config.use_gpu else "cpu"
        self.model=XGBClassifier(
            objective="binary:logistic",
            n_estimators=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            max_depth=self.config.max_depth,
            random_state=self.config.random_seed,
            tree_method=tree_method,
            device=device,
            eval_metric="logloss"
        )

    def train(self,X_train,y_train,X_valid=None,y_valid=None):
        kwargs={}
        if X_valid is not None:
            kwargs["eval_set"]=[(X_valid,y_valid)]
        self.model.fit(X_train,y_train,verbose=False,**kwargs)

    def predict(self,X): return self.model.predict(X)
    def predict_proba(self,X): return self.model.predict_proba(X)
    def feature_importance(self): return self.model.feature_importances_
    def save(self,path): self.model.save_model(path)
    @classmethod
    def load(cls,path):
        m=cls(); m.model.load_model(path); return m
