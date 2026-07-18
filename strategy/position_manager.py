class PositionManager:
    def __init__(self):
        self.active=[]
    def add(self,trade):
        self.active.append(trade)
    def close_all(self):
        closed=self.active[:]
        self.active.clear()
        return closed
