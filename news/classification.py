
def classify(headline):
    h=headline.lower()
    if "inflation" in h: return "Inflation"
    if "rate" in h: return "Interest Rates"
    return "General"
