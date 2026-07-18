
import math

def sharpe(returns, rf=0.0):
    if not returns:
        return 0.0
    mean=sum(returns)/len(returns)
    var=sum((r-mean)**2 for r in returns)/len(returns)
    std=math.sqrt(var)
    return 0.0 if std==0 else (mean-rf)/std

def sortino(returns, rf=0.0):
    downside=[min(0,r-rf) for r in returns]
    ds=math.sqrt(sum(d*d for d in downside)/len(returns)) if returns else 0
    mean=sum(returns)/len(returns) if returns else 0
    return 0.0 if ds==0 else (mean-rf)/ds

def calmar(total_return,max_drawdown):
    return 0.0 if max_drawdown==0 else total_return/max_drawdown
