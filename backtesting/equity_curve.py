
def build_equity(trades,start=10000):
    eq=[start]
    bal=start
    for t in trades:
        bal+=t
        eq.append(bal)
    return eq
