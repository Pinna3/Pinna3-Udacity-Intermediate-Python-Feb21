import functools
import inspect

def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments

def check_types(severity=1):
    def checker(function):
        if severity == 0:
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                return function(*args, **kwargs)
            return wrapper

        elif severity == 1:
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                annotations = function.__annotations__
                param_dict = {}
                for key in args:
                    param_dict[key] = type(key)
                for key, value in kwargs.items():
                    param_dict[key] = type(value)
                param_dict['return'] = type(function(*args, **kwargs))
                if tuple(param_dict.values()) == tuple(annotations.values()):
                    print('Correct')
                    return function(*args, **kwargs)
                else:
                    compare = []
                    for index in range(len(param_dict.values())):
                        side_by_side = [list(param_dict.values())[index], list(annotations.values())[index]]
                        compare.append(side_by_side)
                    for item in range(len(compare)-1):
                        if compare[item][0] is not compare[item][1]:
                            print(f'''Error: Parameter #{item+1} is of the wrong type.''')
                    if param_dict['return'] != annotations['return']:
                        print(f'''Error: Return value is of the wrong type.''')
            return wrapper

        elif severity == 2:
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                annotations = function.__annotations__
                param_dict = {}
                for key in args:
                    param_dict[key] = type(key)
                for key, value in kwargs.items():
                    param_dict[key] = type(value)
                param_dict['return'] = type(function(*args, **kwargs))
                if tuple(param_dict.values()) == tuple(annotations.values()):
                    print('Correct')
                    return function(*args, **kwargs)
                else:
                    compare = []
                    for index in range(len(param_dict.values())):
                        side_by_side = [list(param_dict.values())[index], list(annotations.values())[index]]
                        compare.append(side_by_side)
                    for item in range(len(compare)-1):
                        if compare[item][0] is not compare[item][1]:
                            raise TypeError(f'''Error: Parameter #{item+1} is of the wrong type.''')
                    if param_dict['return'] != annotations['return']:
                        raise TypeError(f'''Error: Return value is of the wrong type.''')
            return wrapper
    return checker





@check_types(severity=2)
def foo(a: int, b: str) -> bool:
    return b[a] == str(0)

foo(a=1, b=[1,0,1,1])
# print(foo.__annotations__) # => {'a': int, 'b': str, 'return': bool}
# print(bind_args(foo, 1, '1011'))
# print(bind_args(foo, 1, 1))
