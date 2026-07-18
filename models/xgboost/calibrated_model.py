
from sklearn.calibration import CalibratedClassifierCV

def build(model,method="sigmoid"):
    return CalibratedClassifierCV(model,method=method,cv=3)
