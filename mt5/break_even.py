
class BreakEven:
    def should_move(self,entry,price,trigger):
        return abs(price-entry)>=trigger
