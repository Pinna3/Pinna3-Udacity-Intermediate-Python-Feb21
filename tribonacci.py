def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True: #1, 2, 4, 7, 13, 24, 44, 81
        a, b, c = b, c, a + b + c
        yield a

# def is_tribonacci(num):
#     """Return whether `num` is a Tribonacci number."""
#     # Be careful to not loop infinitely!
#     return False

a = generate_tribonacci_numbers()
