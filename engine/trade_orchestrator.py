
class TradeOrchestrator:
    def __init__(self,pipeline,executor):
        self.pipeline=pipeline
        self.executor=executor
    def run(self,market):
        result=self.pipeline.run(market)
        return self.executor.execute(result["decision"])
