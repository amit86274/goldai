
class TradeExecutor:
    def __init__(self,client):
        self.client=client
    def execute(self,request):
        return self.client.api.order_send(request)
