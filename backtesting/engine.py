
class BacktestEngine:
    def run(self,signals):
        equity=0
        history=[]
        for s in signals:
            equity+=s
            history.append(equity)
        return history
