
class GoldAIError(Exception): pass

def safe_call(fn,*args,**kwargs):
    try:
        return fn(*args,**kwargs)
    except Exception as e:
        raise GoldAIError(str(e))
