
class TradeHistory:
    def __init__(self,client):
        self.client=client
    def between(self,date_from,date_to):
        return self.client.api.history_deals_get(date_from,date_to)
