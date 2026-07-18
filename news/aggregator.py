class NewsAggregator:
    def aggregate(self,sources):
        out=[]
        [out.extend(s) for s in sources]
        return out
