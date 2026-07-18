
def sentiment_view(score):
    if score>0.2: return "Bullish"
    if score<-0.2: return "Bearish"
    return "Neutral"
