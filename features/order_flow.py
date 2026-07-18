import pandas as pd

def delta(df: pd.DataFrame):
    if "buy_volume" in df and "sell_volume" in df:
        return df["buy_volume"]-df["sell_volume"]
    raise ValueError("buy_volume/sell_volume columns required")
