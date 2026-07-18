
def require_keys(data,*keys):
    return all(k in data for k in keys)
