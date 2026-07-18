
class APIMetrics:
    def summary(self, requests, errors):
        total=max(requests,1)
        return {
            "requests": requests,
            "errors": errors,
            "error_rate": errors/total
        }
