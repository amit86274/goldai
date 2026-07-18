
from sklearn.calibration import CalibratedClassifierCV

def calibrate(meta_model, method="sigmoid"):
    return CalibratedClassifierCV(meta_model, method=method, cv=3)
