
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier

def tune(params,X,y,cv):
    model=XGBClassifier(tree_method="hist",eval_metric="logloss")
    search=RandomizedSearchCV(
        estimator=model,
        param_distributions=params,
        n_iter=20,
        cv=cv,
        scoring="f1",
        n_jobs=-1,
        random_state=42
    )
    search.fit(X,y)
    return search.best_estimator_,search.best_params_,search.best_score_
