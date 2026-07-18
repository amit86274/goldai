
def overview(risk_used,max_risk):
    return {"risk_used":risk_used,"remaining":max(max_risk-risk_used,0)}
