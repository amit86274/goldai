
class NotificationService:
    def __init__(self):
        self.channels={}
    def register(self,name,handler):
        self.channels[name]=handler
    def notify(self,channel,*args,**kwargs):
        return self.channels[channel](*args,**kwargs)
