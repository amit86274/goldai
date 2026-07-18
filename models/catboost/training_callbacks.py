
import time

class TrainingLogger:
    def __init__(self):
        self.start = time.time()

    def summary(self):
        return {"elapsed_seconds": round(time.time()-self.start,2)}
