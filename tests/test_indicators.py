
import pandas as pd
from features.indicators import ema

def test_ema():
    df=pd.DataFrame({"close":[1,2,3,4,5]})
    assert len(ema(df,2))==5
