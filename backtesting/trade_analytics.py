
def analyze(trades):
    return {
        "total":len(trades),
        "avg_profit":sum(trades)/len(trades) if trades else 0.0,
        "best":max(trades) if trades else 0.0,
        "worst":min(trades) if trades else 0.0
    }
