
def validate_order(volume, price):
    if volume<=0:
        raise ValueError("Volume must be positive")
    if price<=0:
        raise ValueError("Price must be positive")
    return True
