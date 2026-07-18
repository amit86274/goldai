
from sklearn.model_selection import TimeSeriesSplit
class TimeSeriesDataset:
    def __init__(self,n_splits=5):
        self.cv=TimeSeriesSplit(n_splits=n_splits)
    def split(self,X):
        return self.cv.split(X)
