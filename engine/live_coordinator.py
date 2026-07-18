
class LiveTradingCoordinator:
    def cycle(self,feed,orchestrator):
        market=feed()
        return orchestrator.run(market)
