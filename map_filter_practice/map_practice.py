# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)


a = map(len, ["apple", "orange", "pear"])
b = map(lambda str: str.upper(), ["apple", "orange", "pear"])
# b = map(str.upper, ["apple", "orange", "pear"]) instructor solution (str.upper new syntax for me)
c = map(lambda str: str[::-1], ["apple", "orange", "pear"])
d = map(lambda str: str[0:2], ["apple", "orange", "pear"])


if __name__ == '__main__':
    print(tuple(a))
    print(tuple(b))
    print(tuple(c))
    print(tuple(d))
