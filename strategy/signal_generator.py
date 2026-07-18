
from dataclasses import dataclass

@dataclass
class TradingSignal:
    direction:str
    confidence:float
    probability:float

class SignalGenerator:
    def generate(self, probability:float, buy=0.60, sell=0.40):
        if probability>=buy:
            return TradingSignal("BUY", probability, probability)
        if probability<=sell:
            return TradingSignal("SELL", 1-probability, probability)
        return TradingSignal("HOLD", abs(probability-0.5)*2, probability)
