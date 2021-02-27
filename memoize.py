import functools
import time

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
            function._cache[key] = function(*args, **kwargs)
        return function._cache[key]
    return wrapper

# # My solution is twice as slow as the instructors because I envoke function(*args, **kwargs) twice as often
# def memoize(function):
#     function.__cache__ = {}
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         if (args, tuple(kwargs.items())) in function.__cache__.keys():
#             return function.__cache__[(args, tuple(kwargs.items()))]
#         else:
#             function.__cache__[(args, tuple(kwargs.items()))] = function(*args, **kwargs)
#             return function(*args, **kwargs)
#     return wrapper

@memoize
def long_operation(x, y):
    time.sleep(3)   # Or some other suitable long expression.
    return x + y

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(long_operation(2, 10))
    print(long_operation(2, 10))
    print(long_operation(2, 11))
    print(long_operation(2, 11))
    print(long_operation(2, 11))
    print(long_operation(2, 11))
    print(long_operation(1, 10))
    print(long_operation(1, 10))
    print(long_operation(1, 10))
    print(long_operation(1, 10))
    print(long_operation._cache)



#####################################################  Reference

# # Standard Decorator Template
# import functools
#
# def decorator(function):
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs)
#     return wrapper
