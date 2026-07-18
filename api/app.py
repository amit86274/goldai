
class APIApplication:
    def __init__(self):
        self.routes={}
    def register(self,path,handler):
        self.routes[path]=handler
