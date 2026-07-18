
class PositionManager:
    def __init__(self,client):
        self.client=client
    def positions(self,symbol=None):
        return self.client.api.positions_get(symbol=symbol) if symbol else self.client.api.positions_get()
