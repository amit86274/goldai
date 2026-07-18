
class TradeAPI:
    def execute(self,executor,order):
        return executor.market_order(**order)
