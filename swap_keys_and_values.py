"""Swap the keys and values in a mapping."""

def swap_keys_and_values(d):
    c = {}
    for key, value in d.items():
            c[value] = set()
    for key, value in d.items():
            c[value].add(key)
    return c


d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
print(swap_keys_and_values(d))
