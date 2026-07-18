
class MockBroker:
    def place_order(self,*_,**__):
        return {"status":"filled"}
