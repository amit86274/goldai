
class ServiceRegistry(dict):
    def register(self,name,service):
        self[name]=service
