
from .signal_generator import generate_signal
def allow_entry(features):
    return generate_signal(features) in ("BUY","SELL")
