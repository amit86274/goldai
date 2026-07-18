
from .trainer import XGBoostTrainer
from .evaluator import evaluate

class TrainingPipeline:
    def __init__(self, model):
        self.model=model
        self.trainer=XGBoostTrainer(model)

    def run(self,X_train,y_train,X_valid,y_valid):
        self.trainer.fit(X_train,y_train,X_valid,y_valid)
        metrics=evaluate(self.model,X_valid,y_valid)
        return {"model":self.model,"metrics":metrics}
