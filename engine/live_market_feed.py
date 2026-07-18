
class LiveMarketFeed:
    def __init__(self, mt5_client):
        self.mt5=mt5_client
    def candles(self,symbol,timeframe,bars=500):
        return self.mt5.get_candles(symbol,timeframe,bars)
