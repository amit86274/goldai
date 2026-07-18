
import numpy as np

def consensus(probabilities, threshold=0.5):
    probs = np.asarray(probabilities)
    mean = probs.mean(axis=0)
    agreement = (probs >= threshold).mean(axis=0)
    return {
        "probability": mean,
        "prediction": (mean >= threshold).astype(int),
        "agreement": agreement
    }
