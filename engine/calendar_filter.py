
class CalendarFilter:
    def allow_trade(self,events):
        high=[e for e in events if e.get("impact")=="high"]
        return len(high)==0
