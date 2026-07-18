
class ConfigSync:
    def merge(self,*configs):
        result={}
        for c in configs:
            result.update(c)
        return result
