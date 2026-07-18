
class PositionService:
    def __init__(self,client):
        self.client=client
    def all(self):
        return self.client.api.positions_get()
    def by_symbol(self,symbol):
        return self.client.api.positions_get(symbol=symbol)
