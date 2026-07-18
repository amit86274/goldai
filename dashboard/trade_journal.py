
class TradeJournal:
    def __init__(self):
        self.entries = []

    def add(self, trade, notes=""):
        self.entries.append({"trade": trade, "notes": notes})

    def all(self):
        return self.entries
