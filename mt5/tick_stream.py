
import time
class TickStream:
    def __init__(self,client):
        self.client=client
    def stream(self,symbol,callback,interval=0.2):
        while True:
            callback(self.client.tick(symbol))
            time.sleep(interval)
