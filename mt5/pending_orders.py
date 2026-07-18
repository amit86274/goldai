
class PendingOrders:
    def buy_limit(self, client, symbol, volume, price, sl=None, tp=None):
        return client.buy_limit(symbol, volume, price, sl=sl, tp=tp)
    def sell_limit(self, client, symbol, volume, price, sl=None, tp=None):
        return client.sell_limit(symbol, volume, price, sl=sl, tp=tp)
    def buy_stop(self, client, symbol, volume, price, sl=None, tp=None):
        return client.buy_stop(symbol, volume, price, sl=sl, tp=tp)
    def sell_stop(self, client, symbol, volume, price, sl=None, tp=None):
        return client.sell_stop(symbol, volume, price, sl=sl, tp=tp)
