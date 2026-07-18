def best_result(results,key="net"):
    return max(results,key=lambda r:r.get(key,0)) if results else None
