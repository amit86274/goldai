
from sklearn.model_selection import TimeSeriesSplit
def get_cv(n_splits=5):
    return TimeSeriesSplit(n_splits=n_splits)
