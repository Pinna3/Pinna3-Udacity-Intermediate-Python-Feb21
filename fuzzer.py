import random

def random_list(size, start=0, stop=10):
    return list(random.randrange(start, stop) for _ in range(size))

def generate_cases():
    """Generate an infinite stream of successively larger random lists."""
    case = []
    len = 0
    while True:
        case = random_list(len)
        len += 1
        yield case

if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)
