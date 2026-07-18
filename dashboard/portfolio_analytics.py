
def portfolio_stats(equity, balance):
    pnl=equity-balance
    return {"equity":equity,"balance":balance,"pnl":pnl}
