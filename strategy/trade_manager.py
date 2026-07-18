
class TradeManager:
    def breakeven(self,entry,current,trigger):
        return entry if abs(current-entry)>=trigger else None
    def trailing_stop(self,current,distance,side="BUY"):
        return current-distance if side=="BUY" else current+distance
