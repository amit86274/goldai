
class TaskOrchestrator:
    def run(self,tasks):
        return [t() if callable(t) else t for t in tasks]
