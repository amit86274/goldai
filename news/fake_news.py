
def credibility(source_score,agreement):
    score=0.7*source_score+0.3*float(agreement)
    return {"score":score,"credible":score>=0.7}
