
class EscalationPolicy:
    def next_level(self, level):
        order=["LOW","MEDIUM","HIGH","CRITICAL"]
        i=order.index(level.upper()) if level.upper() in order else 0
        return order[min(i+1,len(order)-1)]
