
def predict(model,features):
    return {"prediction":model.predict(features),
            "probability":model.predict_proba(features)}
