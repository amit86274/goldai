"""
Feature pipeline.
"""
from __future__ import annotations
import pandas as pd
from .indicators import ema,sma,rsi,macd,atr
from .price_action import candle_body,upper_wick,lower_wick

def build_features(df:pd.DataFrame)->pd.DataFrame:
    out=df.copy()
    out["ema20"]=ema(out,20)
    out["ema50"]=ema(out,50)
    out["sma20"]=sma(out,20)
    out["rsi14"]=rsi(out)
    m,s,h=macd(out)
    out["macd"]=m
    out["macd_signal"]=s
    out["macd_hist"]=h
    out["atr14"]=atr(out)
    out["body"]=candle_body(out)
    out["upper_wick"]=upper_wick(out)
    out["lower_wick"]=lower_wick(out)
    return out.dropna().reset_index(drop=True)
