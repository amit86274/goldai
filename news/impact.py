
def impact_score(severity, reliability=1.0):
    return max(0.0, min(1.0, severity*reliability))
