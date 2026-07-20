import numpy as np

from models.xgboost.mt5_pipeline import FEATURE_COLUMNS, build_training_frame


def test_feature_builder_creates_training_features_without_future_weekly_data():
    daily = np.array([(i * 86400, 100 + i, 101 + i, 99 + i, 100 + i * 1.01, 100, 0, 0) for i in range(90)], dtype=[("time", "i8"), ("open", "f8"), ("high", "f8"), ("low", "f8"), ("close", "f8"), ("tick_volume", "i8"), ("spread", "i8"), ("real_volume", "i8")])
    weekly = np.array([(i * 604800, 100 + i, 101 + i, 99 + i, 100 + i, 100, 0, 0) for i in range(30)], dtype=daily.dtype)

    frame = build_training_frame(daily, weekly)

    assert not frame.empty
    assert set(FEATURE_COLUMNS).issubset(frame.columns)
    assert set(frame["target"].unique()).issubset({0, 1})
