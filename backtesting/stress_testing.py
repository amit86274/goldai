
def stress_test(trades, shock=-0.2):
    return [t*(1+shock) for t in trades]
