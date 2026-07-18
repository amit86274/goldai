
def summary(results):
    return {"trades":len(results),"net":results[-1] if results else 0}
