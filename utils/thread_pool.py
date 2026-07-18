
from concurrent.futures import ThreadPoolExecutor
class ThreadPoolManager:
    def __init__(self,max_workers=4):
        self.pool=ThreadPoolExecutor(max_workers=max_workers)
