
def summarize(confidences):
    if not confidences:
        return {"average":0.0,"max":0.0}
    return {"average":sum(confidences)/len(confidences),"max":max(confidences)}
