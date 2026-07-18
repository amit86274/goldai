
class NewsStream:
    def __init__(self):
        self.listeners=[]
    def subscribe(self,fn):
        self.listeners.append(fn)
    def publish(self,item):
        for fn in self.listeners:
            fn(item)
