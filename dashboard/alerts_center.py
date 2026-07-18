
class AlertsCenter:
    def __init__(self):
        self.alerts=[]
    def push(self,msg,level="INFO"):
        self.alerts.append({"level":level,"message":msg})
