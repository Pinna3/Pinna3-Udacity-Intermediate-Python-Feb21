def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        a, b, c = b, c, a + b + c
        yield a

def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    for trib in generate_tribonacci_numbers():
        if num == trib:
            return True
        elif trib > num:
            return False

print(is_tribonacci(24))
print(is_tribonacci(25))
