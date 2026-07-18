
class DecisionEngine:
    def decide(self,signal,confidence,min_confidence=0.7):
        if confidence<min_confidence:
            return "NO_TRADE"
        return signal
