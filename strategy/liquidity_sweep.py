
def detect_liquidity_sweep(high, low, prev_high, prev_low):
    return {
        "buy_side_sweep": high > prev_high,
        "sell_side_sweep": low < prev_low
    }
