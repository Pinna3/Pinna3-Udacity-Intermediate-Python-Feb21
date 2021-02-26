import functools


def memoize(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@memoize
def long_operation(x, y):
    time.sleep(5)   # Or some other suitable long expression.
    return x + y
