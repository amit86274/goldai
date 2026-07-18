
class MultiSymbolBacktester:
    def run(self, datasets, callback):
        return {symbol:[callback(row) for row in data] for symbol,data in datasets.items()}
