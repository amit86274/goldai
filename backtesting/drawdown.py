
def max_drawdown(equity):
    peak=equity[0]
    mdd=0
    for v in equity:
        peak=max(peak,v)
        mdd=max(mdd,peak-v)
    return mdd
