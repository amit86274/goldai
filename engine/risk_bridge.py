
class RiskBridge:
    def approve(self,risk_manager,signal):
        return risk_manager.validate(signal)
