
def confirm_timeframes(signals):
    return all(signals.values()), {"confirmed": [k for k,v in signals.items() if v]}
