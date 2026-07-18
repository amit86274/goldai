
def basic_stats(trades):
    total=sum(trades)
    wins=sum(1 for t in trades if t>0)
    losses=sum(1 for t in trades if t<=0)
    return {"net_profit":total,"wins":wins,"losses":losses}
