
class Metrics:
    def __init__(self): self.data={}
    def inc(self,key,n=1): self.data[key]=self.data.get(key,0)+n
