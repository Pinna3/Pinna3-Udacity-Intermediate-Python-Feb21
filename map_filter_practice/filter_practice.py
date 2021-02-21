# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)

a = filter(lambda x: x % 3 == 0, range(100))
b = filter(lambda x: x % 5 == 0, range(100))
c = filter(lambda x: x % 15 == 0, range(100))
d = filter(lambda x: x % 3 != 0 and x % 5 != 0, range(100))

if __name__ == '__main__':
    print(tuple(a))
    print(tuple(b))
    print(tuple(c))
    print(tuple(d))
