
class SmartRouter:
    def select(self, routes):
        return min(routes, key=lambda r: r.get("latency", float("inf")))
