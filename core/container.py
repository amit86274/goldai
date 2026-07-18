
class Container:
    def __init__(self):
        self.services={}
    def add(self,name,obj):
        self.services[name]=obj
    def get(self,name):
        return self.services.get(name)
