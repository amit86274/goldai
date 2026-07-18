"""
Price action features.
"""
from __future__ import annotations
import pandas as pd

def candle_body(df):
    return (df["close"]-df["open"]).abs()

def upper_wick(df):
    return df["high"]-df[["open","close"]].max(axis=1)

def lower_wick(df):
    return df[["open","close"]].min(axis=1)-df["low"]

def bullish(df):
    return df["close"]>df["open"]

def bearish(df):
    return df["close"]<df["open"]

def breakout_high(df,lookback=20):
    return df["close"]>df["high"].shift(1).rolling(lookback).max()

def breakout_low(df,lookback=20):
    return df["close"]<df["low"].shift(1).rolling(lookback).min()
