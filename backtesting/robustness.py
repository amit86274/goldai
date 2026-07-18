
def robustness_score(results):
    if not results:
        return 0.0
    return min(results)/max(results) if max(results)!=0 else 0.0
