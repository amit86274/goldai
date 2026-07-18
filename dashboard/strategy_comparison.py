
def rank_strategies(results):
    return sorted(results, key=lambda x: x.get("net_profit", 0), reverse=True)
