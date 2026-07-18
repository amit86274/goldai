class NewsCache:
    def __init__(self): self.cache={}
    def put(self,k,v): self.cache[k]=v
    def get(self,k): return self.cache.get(k)
