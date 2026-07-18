
class TradeLifecycle:
    def __init__(self):
        self.state="NEW"

    def update(self, state):
        self.state=state
        return self.state
