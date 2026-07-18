
import tracemalloc
def memory_snapshot():
    tracemalloc.start()
    current, peak = tracemalloc.get_traced_memory()
    return {"current":current,"peak":peak}
