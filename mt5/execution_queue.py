
from collections import deque

class ExecutionQueue:
    def __init__(self):
        self._q=deque()
    def add(self, order):
        self._q.append(order)
    def next(self):
        return self._q.popleft() if self._q else None
