"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil without lifting."""
EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')

def is_efficient(letters):
    return set(letters) <= EFFICIENT_LETTERS

if __name__ == '__main__':
    letters = input('What word would you like  to check for efficiency?')
    print(is_efficient(letters))
