DEFAULT_SCORES={'reuters':0.99,'bloomberg':0.98,'forexfactory':0.95}
def score(src): return DEFAULT_SCORES.get(src.lower(),0.5)
