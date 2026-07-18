
def win_rate(wins,trades):
    return 0 if trades==0 else wins/trades*100
def profit_factor(gross_profit,gross_loss):
    return float("inf") if gross_loss==0 else gross_profit/gross_loss
