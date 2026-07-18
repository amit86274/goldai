
class TradeStatistics:
    def summary(self, trades):
        total=len(trades)
        wins=sum(1 for t in trades if t.get("profit",0)>0)
        return {"total":total,"wins":wins,"win_rate":wins/total if total else 0.0}
