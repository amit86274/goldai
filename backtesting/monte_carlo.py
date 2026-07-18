
import random
def simulate(trades,iterations=100):
    return [sum(random.sample(trades,len(trades))) for _ in range(iterations)]
