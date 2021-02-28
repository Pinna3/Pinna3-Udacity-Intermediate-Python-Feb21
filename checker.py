import functools
import inspect

# My solution ASSISTED...
def check_types(severity=1):
    if severity == 0:
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        elif severity == 2:
            raise TypeError(msg)

    def checker(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                annotations = function.__annotations__
                if not annotations:
                    return function(*args, **kwargs)
                param_dict = {}
                for key in args:
                    param_dict[key] = type(key)
                for key, value in kwargs.items():
                    param_dict[key] = type(value)
                param_dict['return'] = type(function(*args, **kwargs))
                if tuple(param_dict.values()) == tuple(annotations.values()):
                    return function(*args, **kwargs)
                else:
                    compare = []
                    for index in range(len(param_dict.values())):
                        side_by_side = [list(param_dict.values())[index], list(annotations.values())[index]]
                        compare.append(side_by_side)
                    for item in range(len(compare)-1):
                        if compare[item][0] is not compare[item][1]:
                            message(f'''Error: Parameter #{item+1} should be {compare[item][1]}.''')
                    if param_dict['return'] != annotations['return']:
                        message(f'''Error: Return value should be {annotations['return']}.''')
            return wrapper
    return checker


# # My solution UNASSISTED (WONKY BUT WORKING)
# def check_types(severity=1):
#     def checker(function):
#         if severity == 0:
#             @functools.wraps(function)
#             def wrapper(*args, **kwargs):
#                 return function(*args, **kwargs)
#             return wrapper
#         elif severity == 1:
#             @functools.wraps(function)
#             def wrapper(*args, **kwargs):
#                 annotations = function.__annotations__
#                 param_dict = {}
#                 for key in args:
#                     param_dict[key] = type(key)
#                 for key, value in kwargs.items():
#                     param_dict[key] = type(value)
#                 param_dict['return'] = type(function(*args, **kwargs))
#                 if tuple(param_dict.values()) == tuple(annotations.values()):
#                     print('Correct')
#                     return function(*args, **kwargs)
#                 else:
#                     compare = []
#                     for index in range(len(param_dict.values())):
#                         side_by_side = [list(param_dict.values())[index], list(annotations.values())[index]]
#                         compare.append(side_by_side)
#                     for item in range(len(compare)-1):
#                         if compare[item][0] is not compare[item][1]:
#                             print(f'''Error: Parameter #{item+1} is of the wrong type.''')
#                     if param_dict['return'] != annotations['return']:
#                         print(f'''Error: Return value is of the wrong type.''')
#             return wrapper
#         elif severity == 2:
#             @functools.wraps(function)
#             def wrapper(*args, **kwargs):
#                 annotations = function.__annotations__
#                 param_dict = {}
#                 for key in args:
#                     param_dict[key] = type(key)
#                 for key, value in kwargs.items():
#                     param_dict[key] = type(value)
#                 param_dict['return'] = type(function(*args, **kwargs))
#                 if tuple(param_dict.values()) == tuple(annotations.values()):
#                     print('Correct')
#                     return function(*args, **kwargs)
#                 else:
#                     compare = []
#                     for index in range(len(param_dict.values())):
#                         side_by_side = [list(param_dict.values())[index], list(annotations.values())[index]]
#                         compare.append(side_by_side)
#                     for item in range(len(compare)-1):
#                         if compare[item][0] is not compare[item][1]:
#                             raise TypeError(f'''Error: Parameter #{item+1} is of the wrong type.''')
#                     if param_dict['return'] != annotations['return']:
#                         raise TypeError(f'''Error: Return value is of the wrong type.''')
#             return wrapper
#     return checker


# # ELEGENT INSTRUCTOR SOLUTION
# def check_types(severity=1):
#     if severity == 0:
#         return lambda function: function
#
#     def message(msg):
#         if severity == 1:
#             print(msg)
#         else:
#             raise TypeError(msg)
#     def checker(function):
#         expected = function.__annotations__
#
#         assert(all(map(lambda exp: isinstance(exp, type), expected.values())))
#         if not expected:
#             return function
#         @functools.wraps(function)
#         def wrapper(*args, **kwargs):
#             bound_arguments = helper.bind_args(function, *args, **kwargs)
#             for arg, val in bound_arguments.items():
#                 if arg not in expected:
#                     continue
#                 if not isinstance(val, expected[arg]):
#                     message(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg]}")
#             retval = function(*args, **kwargs)
#             if 'return' in expected and not isinstance(retval, expected['return']):
#                 message(f"Bad Return Value! Received {retval}, but expected value of type {expected['return']}")
#             return retval
#         return wrapper
#     return checker


@check_types(severity=1)
def foo(a: int, b: str) -> bool:
    return b[a] == str(0)

@check_types()
def foo2():
    return 2 * 3

if __name__ == '__main__':
    print(foo2())
    foo(a=1, b=[1,1,1,1])
    # print(foo.__annotations__) # => {'a': int, 'b': str, 'return': bool}
    # print(bind_args(foo, 1, '1011'))
    # print(bind_args(foo, 1, 1))
