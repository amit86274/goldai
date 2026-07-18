
class TradeFilter:
    def allow(self, spread, max_spread=25):
        return spread<=max_spread
