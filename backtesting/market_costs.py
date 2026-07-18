
def apply_costs(pnl, spread=0.0, commission=0.0, swap=0.0):
    return pnl - spread - commission - swap
