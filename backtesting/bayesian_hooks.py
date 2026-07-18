
class BayesianOptimizerHook:
    def suggest(self, history):
        return history[-1]["params"] if history else {}
