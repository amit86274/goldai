
from .trainer import TransformerTrainer
from .evaluator import evaluate

class TrainingPipeline:
    def __init__(self,model):
        self.model=model
        self.trainer=TransformerTrainer(model)

    def run(self,X_train,y_train,X_valid,y_valid,**fit_kwargs):
        self.trainer.fit(X_train,y_train,
                         validation_data=(X_valid,y_valid),
                         **fit_kwargs)
        return {"model":self.model,
                "metrics":evaluate(self.model,X_valid,y_valid)}
