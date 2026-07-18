
class SymbolManager:
    def __init__(self,client):
        self.client=client
    def ensure(self,symbol):
        return self.client.symbol_select(symbol)
    def list(self):
        return self.client.symbols()
