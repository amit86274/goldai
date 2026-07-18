
class AccountService:
    def __init__(self,client):
        self.client=client
    def info(self):
        info=self.client.api.account_info()
        return info._asdict() if info else None
