
class HistoryDownloader:
    def __init__(self,client):
        self.client=client
    def download(self,symbol,timeframe,bars):
        return self.client.candles(symbol,timeframe,bars)
