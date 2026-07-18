
class LiveFeatureExtractor:
    def extract(self,candles):
        return {"last_close":candles[-1]["close"] if candles else None,
                "count":len(candles)}
