
class StrategyBridge:
    def evaluate(self,strategy,context):
        return strategy.generate(context)
