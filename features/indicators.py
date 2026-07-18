"""
Technical indicators for Gold-AI v1.
"""
from __future__ import annotations
import pandas as pd

def ema(df: pd.DataFrame, period:int=20, column:str="close")->pd.Series:
    return df[column].ewm(span=period, adjust=False).mean()

def sma(df: pd.DataFrame, period:int=20, column:str="close")->pd.Series:
    return df[column].rolling(period).mean()

def rsi(df: pd.DataFrame, period:int=14, column:str="close")->pd.Series:
    delta=df[column].diff()
    gain=delta.clip(lower=0).rolling(period).mean()
    loss=(-delta.clip(upper=0)).rolling(period).mean()
    rs=gain/loss.replace(0,float("nan"))
    return 100-(100/(1+rs))

def macd(df: pd.DataFrame,column:str="close"):
    ema12=ema(df,12,column)
    ema26=ema(df,26,column)
    macd=ema12-ema26
    signal=macd.ewm(span=9,adjust=False).mean()
    hist=macd-signal
    return macd,signal,hist

def atr(df: pd.DataFrame,period:int=14)->pd.Series:
    h,l,c=df["high"],df["low"],df["close"]
    tr=pd.concat([(h-l),(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1)
    return tr.rolling(period).mean()
