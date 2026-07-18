
class RiskValidator:
    def validate(self, account, volume, risk_pct):
        balance = float(account.get("balance",0))
        max_risk = balance * (risk_pct/100.0)
        return {"approved": max_risk > 0, "max_risk": max_risk, "volume": volume}
