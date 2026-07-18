
class TrailingStop:
    def next_sl(self,current_sl,price,distance):
        target=price-distance
        return max(current_sl,target)
