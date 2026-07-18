
class HistoricalReplay:
    def __init__(self,data):
        self.data=data
    def run(self,callback):
        results=[]
        for row in self.data:
            results.append(callback(row))
        return results
