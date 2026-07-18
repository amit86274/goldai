
class ExecutionRules:
    def can_enter(self, signal, confidence, minimum=0.65):
        return signal in ("BUY","SELL") and confidence>=minimum
