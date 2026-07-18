
import time
def benchmark(fn,*args,**kwargs):
    s=time.perf_counter()
    r=fn(*args,**kwargs)
    return {"elapsed":time.perf_counter()-s,"result":r}
