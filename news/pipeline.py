class NewsPipeline:
    def __init__(self,a,n): self.a=a; self.n=n
    def run(self,sources): return [self.n(x) for x in self.a.aggregate(sources)]
