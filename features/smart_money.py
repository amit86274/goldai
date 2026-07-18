"""Initial Smart Money Concepts."""
from __future__ import annotations
import pandas as pd

def fair_value_gap(df: pd.DataFrame)->pd.Series:
    prev_high=df["high"].shift(1)
    next_low=df["low"].shift(-1)
    return next_low>prev_high

def bullish_order_block(df: pd.DataFrame)->pd.Series:
    prev_bear=df["close"].shift(1)<df["open"].shift(1)
    impulse=df["close"]>df["high"].shift(1)
    return prev_bear & impulse

def liquidity_sweep_high(df: pd.DataFrame)->pd.Series:
    return (df["high"]>df["high"].shift(1)) & (df["close"]<df["high"].shift(1))
