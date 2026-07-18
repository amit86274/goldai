
import numpy as np

def detect_drift(reference, current, threshold=0.1):
    reference = np.asarray(reference)
    current = np.asarray(current)
    drift = abs(reference.mean() - current.mean())
    return {
        "drift_score": float(drift),
        "drift_detected": bool(drift > threshold)
    }
