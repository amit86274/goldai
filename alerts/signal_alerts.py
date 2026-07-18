
def build_signal_alert(symbol, signal, confidence):
    return {
        "type": "signal",
        "symbol": symbol,
        "signal": signal,
        "confidence": confidence
    }
