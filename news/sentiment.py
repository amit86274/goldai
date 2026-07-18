
class NewsSentiment:
    def analyze(self, score):
        if score>0.2: return "Bullish"
        if score<-0.2: return "Bearish"
        return "Neutral"
