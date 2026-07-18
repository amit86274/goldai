
def build_heatmap(predictions):
    return [{"symbol": p["symbol"], "confidence": p["confidence"]} for p in predictions]
