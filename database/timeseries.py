
class TimeSeriesStore:
    def __init__(self):
        self.data = {}

    def insert(self, symbol, record):
        self.data.setdefault(symbol, []).append(record)

    def query(self, symbol):
        return self.data.get(symbol, [])
