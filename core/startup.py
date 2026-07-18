
def startup_sequence(steps):
    return [step() if callable(step) else step for step in steps]
