
def allow_trade(trend,bos=False,choch=False):
    return trend in ("bullish","bearish") and (bos or choch)
