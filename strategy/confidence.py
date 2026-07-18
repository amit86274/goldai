
def confidence_score(model_probs):
    if not model_probs:
        return 0.0
    return sum(model_probs)/len(model_probs)
