"""Candlestick pattern detection."""
from __future__ import annotations
import pandas as pd

def doji(df, threshold=0.1):
    body=(df["close"]-df["open"]).abs()
    rng=(df["high"]-df["low"]).replace(0,1e-9)
    return (body/rng)<=threshold

def hammer(df):
    body=(df["close"]-df["open"]).abs()
    lower=df[["open","close"]].min(axis=1)-df["low"]
    upper=df["high"]-df[["open","close"]].max(axis=1)
    return (lower>body*2) & (upper<body)

def bullish_engulfing(df):
    prev=df.shift(1)
    return (prev["close"]<prev["open"]) & (df["close"]>df["open"]) & (df["open"]<prev["close"]) & (df["close"]>prev["open"])
