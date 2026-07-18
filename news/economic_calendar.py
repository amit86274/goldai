class EconomicCalendar:
    def upcoming(self,events):
        return sorted(events,key=lambda e:e.get('time',''))
