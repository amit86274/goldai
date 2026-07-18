
class NewsHistory:
    def __init__(self): self.items=[]
    def add(self,item): self.items.append(item)
    def search(self,keyword):
        return [i for i in self.items if keyword.lower() in i.get("title","").lower()]
