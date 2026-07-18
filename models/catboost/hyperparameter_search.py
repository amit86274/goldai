
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostClassifier

def tune(params, X, y, cv):
    model = CatBoostClassifier(verbose=False)
    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=params,
        n_iter=20,
        scoring="f1",
        cv=cv,
        n_jobs=-1,
        random_state=42
    )
    search.fit(X, y)
    return search.best_estimator_, search.best_params_, search.best_score_
