
def detect_fvg(prev_high, next_low, prev_low, next_high):
    bullish = next_low > prev_high
    bearish = next_high < prev_low
    return {"bullish": bullish, "bearish": bearish}
