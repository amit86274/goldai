
import shap

def explain(model,X):
    explainer=shap.TreeExplainer(model.model)
    values=explainer.shap_values(X)
    return values
