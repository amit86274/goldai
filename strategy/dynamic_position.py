
def volatility_position(balance,risk_pct,atr,pip_value):
    risk=balance*risk_pct/100
    return risk/max(atr*pip_value,1e-9)
