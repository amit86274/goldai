"""Feature importance utilities."""
from __future__ import annotations
import pandas as pd

def ranked_features(model, feature_names):
    if not hasattr(model, "feature_importances_"):
        raise AttributeError("Model does not expose feature_importances_.")
    df = pd.DataFrame({
        "feature": feature_names,
        "importance": model.feature_importances_
    })
    return df.sort_values("importance", ascending=False).reset_index(drop=True)
