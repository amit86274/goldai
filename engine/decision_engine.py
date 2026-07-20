from dataclasses import dataclass

@dataclass
class DecisionResult:
    action:str
    confidence:float
    reason:str

class DecisionEngine:
    def __init__(self,min_confidence=0.75):
        self.min_confidence=min_confidence
    def decide(self,signal,confidence):
        if signal=="HOLD":
            return DecisionResult("WAIT",confidence,"Model returned HOLD")
        if confidence<self.min_confidence:
            return DecisionResult("WAIT",confidence,"Low confidence")
        if signal=="BUY":
            return DecisionResult("BUY",confidence,"Model approved")
        if signal=="SELL":
            return DecisionResult("SELL",confidence,"Model approved")
        return DecisionResult("WAIT",confidence,"Unknown signal")
