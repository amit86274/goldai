
class OrderService:
    def __init__(self,client):
        self.client=client
    def pending(self):
        return self.client.api.orders_get()
