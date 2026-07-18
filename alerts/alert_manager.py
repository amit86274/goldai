
class AlertManager:
    def __init__(self):
        self.handlers = []

    def register(self, handler):
        self.handlers.append(handler)

    def dispatch(self, payload):
        return [handler(payload) for handler in self.handlers]
