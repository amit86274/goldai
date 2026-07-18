
from collections import deque
class RetryQueue:
    def __init__(self):
        self.queue=deque()
    def add(self,item):
        self.queue.append(item)
    def pop(self):
        return self.queue.popleft() if self.queue else None
