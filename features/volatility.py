"""Volatility features."""
from __future__ import annotations
import pandas as pd

def true_range(df: pd.DataFrame)->pd.Series:
    h,l,c=df["high"],df["low"],df["close"]
    return pd.concat([(h-l),(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1)

def rolling_volatility(df: pd.DataFrame, period:int=20)->pd.Series:
    return df["close"].pct_change().rolling(period).std()

def average_range(df: pd.DataFrame, period:int=20)->pd.Series:
    return (df["high"]-df["low"]).rolling(period).mean()
