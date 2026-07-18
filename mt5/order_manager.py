
class OrderManager:
    def __init__(self,executor):
        self.executor=executor
    def market_order(self,request):
        return self.executor.execute(request)
