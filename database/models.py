from dataclasses import dataclass
@dataclass
class Trade:
    symbol:str
    side:str
    entry:float
    exit:float|None=None
