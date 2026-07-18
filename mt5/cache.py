
class MarketCache:
    def __init__(self):
        self._cache={}
    def set(self,key,val):
        self._cache[key]=val
    def get(self,key):
        return self._cache.get(key)
