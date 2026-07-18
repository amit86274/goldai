
from sklearn.feature_selection import VarianceThreshold

def variance_filter(X,threshold=0.0):
    selector=VarianceThreshold(threshold)
    return selector.fit_transform(X),selector
