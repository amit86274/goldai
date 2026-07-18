
def batch_predict(model, dataset):
    return [model.predict(item) for item in dataset]
