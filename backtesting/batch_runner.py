
class BatchBacktester:
    def run(self,strategies,dataset):
        return {name:strategy(dataset) for name,strategy in strategies.items()}
