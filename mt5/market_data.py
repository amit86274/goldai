
class MarketDataService:
    def __init__(self,client):
        self.client=client
    def candles(self,symbol,timeframe,count=1000):
        return self.client.candles(symbol,timeframe,count)
    def tick(self,symbol):
        return self.client.tick(symbol)
