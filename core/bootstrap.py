
class Bootstrap:
    def __init__(self):
        self.modules=[]
    def register(self,module):
        self.modules.append(module)
    def start(self):
        return {"started":len(self.modules)}
