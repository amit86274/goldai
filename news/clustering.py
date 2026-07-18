
from collections import defaultdict
def cluster(items,key="topic"):
    out=defaultdict(list)
    for i in items: out[i.get(key,"General")].append(i)
    return dict(out)
