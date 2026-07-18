
import time

def retry(func, attempts=3, delay=1):
    for i in range(attempts):
        try:
            return func()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(delay)
