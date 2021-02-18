english_words_small = set((
    "open",
    "peon",
    "nope",
    "stone",
    "notes",
    "onset",
    "tones",
    "cone",
    "pots",
    "post",
    "stop",
    "opts",
    "tops",
))

def find_anagrams(letters, words):
    try:
        canonical_dict = {}
        letters_canonical = ''.join(sorted(letters))
        for word in words:
            canonical = ''.join(sorted(word))
            if canonical not in canonical_dict.keys():
                canonical_dict[canonical] = set()
            canonical_dict[canonical].add(word)
        return canonical_dict[letters_canonical]
    except KeyError:
        return '0'

if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ").strip().lower()
        for anagram in find_anagrams(letters, english_words_small):
            print(anagram)
