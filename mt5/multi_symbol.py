
class MultiSymbolExecutor:
    def execute(self, executor, orders):
        return [executor.market_order(**o) for o in orders]
