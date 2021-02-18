"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil without lifting."""
EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')

def is_efficient(letters):
    return set(letters) <= EFFICIENT_LETTERS

print(is_efficient('UNCONSCIOUS'))
