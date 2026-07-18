"""Liquidity level helpers."""
from __future__ import annotations
import pandas as pd

def previous_day_high(df: pd.DataFrame)->pd.Series:
    return df["high"].shift(1).cummax()

def previous_day_low(df: pd.DataFrame)->pd.Series:
    return df["low"].shift(1).cummin()

def equal_highs(df: pd.DataFrame, tolerance:float=0.05)->pd.Series:
    return (df["high"].diff().abs()<=tolerance)

def equal_lows(df: pd.DataFrame, tolerance:float=0.05)->pd.Series:
    return (df["low"].diff().abs()<=tolerance)
