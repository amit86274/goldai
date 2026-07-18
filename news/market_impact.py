
def predict_impact(sentiment,importance):
    value=sentiment*importance
    if value>0.3: return "Bullish"
    if value<-0.3: return "Bearish"
    return "Neutral"
