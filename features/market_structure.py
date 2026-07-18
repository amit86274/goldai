"""Basic market structure."""
from __future__ import annotations
import pandas as pd

def swing_high(df, lookback=3):
    return df["high"]==df["high"].rolling(lookback*2+1, center=True).max()

def swing_low(df, lookback=3):
    return df["low"]==df["low"].rolling(lookback*2+1, center=True).min()

def trend(df, ema_fast="ema20", ema_slow="ema50"):
    return (df[ema_fast]>df[ema_slow]).map({True:"UP",False:"DOWN"})
