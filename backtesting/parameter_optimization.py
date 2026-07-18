
from itertools import product

def grid_search(param_grid):
    keys=list(param_grid.keys())
    for vals in product(*param_grid.values()):
        yield dict(zip(keys,vals))
