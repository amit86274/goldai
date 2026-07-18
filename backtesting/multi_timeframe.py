
class MultiTimeframeReplay:
    def replay(self, data):
        return {tf:list(rows) for tf,rows in data.items()}
