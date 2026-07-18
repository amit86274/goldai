
import time
class CandleStream:
    def __init__(self,client):
        self.client=client
    def stream(self,symbol,timeframe,callback,count=500,poll=1):
        while True:
            callback(self.client.candles(symbol,timeframe,count))
            time.sleep(poll)
