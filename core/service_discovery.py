
class ServiceDiscovery:
    def __init__(self):
        self.services={}
    def register(self,name,endpoint):
        self.services[name]=endpoint
    def find(self,name):
        return self.services.get(name)
