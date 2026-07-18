import pandas as pd

def bos(df: pd.DataFrame):
    return df["high"] > df["high"].shift(1).rolling(20).max()

def choch(df: pd.DataFrame):
    return (df["low"] < df["low"].shift(1)) & (df["close"] > df["open"])

def liquidity_sweep(df: pd.DataFrame):
    return (df["high"] > df["high"].shift(1)) & (df["close"] < df["high"].shift(1))
