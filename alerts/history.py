
class AlertHistory:
    def __init__(self):
        self.records=[]
    def add(self,alert):
        self.records.append(alert)
    def all(self):
        return self.records
