from collections import Counter

def price_histogram(prices, precision=1):
    rounded=[round(p,precision) for p in prices]
    return dict(Counter(rounded))
