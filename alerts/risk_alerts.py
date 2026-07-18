
def build_risk_alert(risk_used, max_risk):
    return {
        "type": "risk",
        "risk_used": risk_used,
        "max_risk": max_risk,
        "triggered": risk_used >= max_risk
    }
