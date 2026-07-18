
def exposure(open_risk,max_risk):
    return {"allowed":open_risk<max_risk,
            "remaining":max(max_risk-open_risk,0)}
