
from sklearn.calibration import CalibratedClassifierCV

def calibrate(model,method="sigmoid",cv=3):
    return CalibratedClassifierCV(model,method=method,cv=cv)
