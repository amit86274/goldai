
class EventBus:
    def __init__(self): self.handlers={}
    def subscribe(self,event,fn): self.handlers.setdefault(event,[]).append(fn)
    def publish(self,event,data=None):
        for fn in self.handlers.get(event,[]): fn(data)
