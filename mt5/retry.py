
import time

def retry(func, attempts=3, delay=1):
    last=None
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            last=e
            time.sleep(delay)
    raise last
