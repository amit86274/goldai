
def atr_stop_takeprofit(entry, atr, sl_mult=1.5, tp_mult=3.0, side="BUY"):
    if side=="BUY":
        return {"sl":entry-atr*sl_mult,"tp":entry+atr*tp_mult}
    return {"sl":entry+atr*sl_mult,"tp":entry-atr*tp_mult}
