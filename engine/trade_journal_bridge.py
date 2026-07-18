
class TradeJournalBridge:
    def record(self,journal,trade):
        return journal.add(trade)
