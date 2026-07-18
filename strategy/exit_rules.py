
def should_exit(signal,current_signal):
    return signal!=current_signal or current_signal=="HOLD"
