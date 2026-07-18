
def get_feature_importance(model,feature_names):
    scores=model.feature_importance()
    return dict(zip(feature_names,scores))
