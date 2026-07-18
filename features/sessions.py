"""Trading session tagging."""
from __future__ import annotations
import pandas as pd

def add_sessions(df: pd.DataFrame, time_col="time")->pd.DataFrame:
    out=df.copy()
    h=pd.to_datetime(out[time_col]).dt.hour
    out["asian_session"]=((h>=0)&(h<8)).astype(int)
    out["london_session"]=((h>=8)&(h<16)).astype(int)
    out["newyork_session"]=((h>=13)&(h<21)).astype(int)
    return out
