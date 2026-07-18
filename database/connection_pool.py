
class ConnectionPool:
    def __init__(self, size=10):
        self.size=size
        self.available=size

    def acquire(self):
        if self.available>0:
            self.available-=1
            return True
        return False

    def release(self):
        if self.available<self.size:
            self.available+=1
