
def within_slippage(expected, actual, max_slippage):
    return abs(actual-expected) <= max_slippage
