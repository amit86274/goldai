
class MarketDataRepository:
    def save(self, candle):
        return {"status": "saved", "market_data": candle}
