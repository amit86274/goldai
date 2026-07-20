"""Chronological XGBoost training on MT5 D1 candles with W1 context."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, roc_auc_score
from xgboost import XGBClassifier


FEATURE_COLUMNS = [
    "return_1", "return_5", "range_pct", "atr_pct", "volatility_20",
    "ema_gap", "rsi_14", "volume_zscore", "weekly_return_4", "weekly_trend",
]


@dataclass(frozen=True, slots=True)
class TrainingResult:
    rows: int
    train_rows: int
    validation_rows: int
    accuracy: float
    precision: float
    auc: float | None
    artifact_path: str


class ModelQualityError(ValueError):
    """Raised when chronological validation does not meet deployment criteria."""


def _frame(rates: Any) -> pd.DataFrame:
    frame = pd.DataFrame(rates)
    if frame.empty:
        raise ValueError("MT5 returned no candle data")
    frame["time"] = pd.to_datetime(frame["time"], unit="s", utc=True).astype("datetime64[ns, UTC]")
    return frame.sort_values("time").reset_index(drop=True)


def build_training_frame(daily_rates: Any, weekly_rates: Any, horizon: int = 5, move_threshold: float = 0.003) -> pd.DataFrame:
    """Build leak-free D1 features, using only previously closed W1 candles."""
    if horizon < 1 or not 0 < move_threshold < 1:
        raise ValueError("horizon must be positive and move_threshold must be between 0 and 1")
    daily = _frame(daily_rates)
    weekly = _frame(weekly_rates)

    previous_close = daily["close"].shift(1)
    true_range = pd.concat(
        [daily["high"] - daily["low"], (daily["high"] - previous_close).abs(), (daily["low"] - previous_close).abs()], axis=1
    ).max(axis=1)
    daily["return_1"] = daily["close"].pct_change()
    daily["return_5"] = daily["close"].pct_change(5)
    daily["range_pct"] = (daily["high"] - daily["low"]) / daily["close"]
    daily["atr_pct"] = true_range.rolling(14).mean() / daily["close"]
    daily["volatility_20"] = daily["return_1"].rolling(20).std()
    daily["ema_gap"] = daily["close"].ewm(span=10, adjust=False).mean() / daily["close"].ewm(span=30, adjust=False).mean() - 1
    delta = daily["close"].diff()
    gain, loss = delta.clip(lower=0).rolling(14).mean(), (-delta.clip(upper=0)).rolling(14).mean()
    daily["rsi_14"] = (100 - 100 / (1 + gain / loss.replace(0, np.nan))).where(loss.ne(0), 100.0)
    volume_mean, volume_std = daily["tick_volume"].rolling(20).mean(), daily["tick_volume"].rolling(20).std()
    daily["volume_zscore"] = ((daily["tick_volume"] - volume_mean) / volume_std.replace(0, np.nan)).fillna(0.0)

    weekly["weekly_return_4"] = weekly["close"].pct_change(4)
    weekly["weekly_trend"] = weekly["close"].ewm(span=8, adjust=False).mean() / weekly["close"].ewm(span=21, adjust=False).mean() - 1
    weekly = weekly[["time", "weekly_return_4", "weekly_trend"]].dropna()
    # Shift one week: a D1 bar must not see the partially formed current week.
    weekly["time"] = weekly["time"] + pd.Timedelta(days=7)
    data = pd.merge_asof(daily, weekly, on="time", direction="backward")
    data["target"] = (data["close"].shift(-horizon) / data["close"] - 1 >= move_threshold).astype(int)
    return data.iloc[:-horizon].dropna(subset=FEATURE_COLUMNS).reset_index(drop=True)


class MT5XGBoostTrainer:
    def __init__(self, validation_fraction: float = 0.2, minimum_auc: float = 0.55) -> None:
        if not 0.1 <= validation_fraction < 0.5:
            raise ValueError("validation_fraction must be between 0.1 and 0.5")
        self.validation_fraction = validation_fraction
        if not 0.5 < minimum_auc <= 1.0:
            raise ValueError("minimum_auc must be greater than 0.5 and at most 1")
        self.minimum_auc = minimum_auc

    def train(self, daily_rates: Any, weekly_rates: Any, artifact_path: str | Path) -> TrainingResult:
        data = build_training_frame(daily_rates, weekly_rates)
        split = int(len(data) * (1 - self.validation_fraction))
        if split < 100 or len(data) - split < 30:
            raise ValueError("not enough D1 history; at least 130 labelled rows are required")
        X_train, X_valid = data[FEATURE_COLUMNS].iloc[:split], data[FEATURE_COLUMNS].iloc[split:]
        y_train, y_valid = data["target"].iloc[:split], data["target"].iloc[split:]
        if y_train.nunique() < 2 or y_valid.nunique() < 2:
            raise ValueError("training and validation periods must contain both target classes")
        model = XGBClassifier(
            objective="binary:logistic", eval_metric="logloss", tree_method="hist", device="cpu",
            n_estimators=300, max_depth=3, learning_rate=0.03, subsample=0.8,
            colsample_bytree=0.8, min_child_weight=5, reg_lambda=5.0, random_state=42,
        )
        model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
        probabilities = model.predict_proba(X_valid)[:, 1]
        predictions = (probabilities >= 0.5).astype(int)
        auc = float(roc_auc_score(y_valid, probabilities)) if y_valid.nunique() == 2 else None
        if auc is None or auc < self.minimum_auc:
            raise ModelQualityError(
                f"validation AUC {auc:.3f} is below the required {self.minimum_auc:.3f}; model was not saved"
            )
        target = Path(artifact_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump({"model": model, "features": FEATURE_COLUMNS, "trained_until": str(data["time"].iloc[-1])}, target)
        return TrainingResult(len(data), len(X_train), len(X_valid), float(accuracy_score(y_valid, predictions)), float(precision_score(y_valid, predictions, zero_division=0)), auc, str(target))
