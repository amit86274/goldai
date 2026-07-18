
class DecisionEngine:
    def decide(self, signal, confidence, mtf_ok, smc_ok, news_ok):
        if signal=="HOLD":
            return "NO_TRADE"
        if confidence >= 0.70 and mtf_ok and smc_ok and news_ok:
            return signal
        return "WAIT"
