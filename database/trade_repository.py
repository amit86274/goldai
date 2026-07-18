
class TradeRepository:
    def save(self, trade):
        return {"status": "saved", "trade": trade}
