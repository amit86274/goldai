
from concurrent.futures import ThreadPoolExecutor

class BackgroundTaskRunner:
    def __init__(self, workers=2):
        self.executor=ThreadPoolExecutor(max_workers=workers)

    def submit(self, fn, *args, **kwargs):
        return self.executor.submit(fn, *args, **kwargs)
