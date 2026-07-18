
class SignalGenerator:
    def generate(self,value,threshold=0):
        return "BUY" if value>threshold else "SELL" if value<threshold else "HOLD"
