from functools import wraps


# A new closure will be returned as a chain of Closures in the incoming list order
def chain_closures(closure_list=None):
    if not closure_list:
        return None

    def chain(f):
        @wraps(f)
        def r(*args, **kwargs):
            newfunc = f
            for c in reversed(closure_list):
                newfunc = c(newfunc)
            return newfunc(*args, **kwargs)

        return r

    return chain