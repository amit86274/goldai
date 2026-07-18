
class EventCoordinator:
    def __init__(self): self.listeners={}
    def on(self,event,fn):
        self.listeners.setdefault(event,[]).append(fn)
    def emit(self,event,data=None):
        for fn in self.listeners.get(event,[]): fn(data)
