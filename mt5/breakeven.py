
def breakeven(entry, current, trigger, side="BUY"):
    move=(current-entry) if side=="BUY" else (entry-current)
    return entry if move>=trigger else None
