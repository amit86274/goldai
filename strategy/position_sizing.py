
def fixed_fractional(balance,risk_percent,stop_loss_pips,pip_value):
    risk_amount=balance*(risk_percent/100)
    return risk_amount/(stop_loss_pips*pip_value)
