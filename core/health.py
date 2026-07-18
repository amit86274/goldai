
class HealthAggregator:
    def aggregate(self,checks):
        return {k:v() if callable(v) else v for k,v in checks.items()}
