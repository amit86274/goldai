
class MarketRegimeDetector:
    def detect(self,volatility):
        if volatility>0.8: return "volatile"
        if volatility<0.3: return "range"
        return "trend"
