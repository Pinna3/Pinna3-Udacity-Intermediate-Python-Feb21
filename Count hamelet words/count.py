from collections import Counter

def count_unique_words(filename):
    with open('hamlet.txt', 'r') as hamlet:

        contents_split = hamlet.read().split('\n')
        barewords = []
        for line in contents_split:
            line_split = line.split(' ')
            for word in line_split:
                barewords.append(word.strip(r'''!()-[]{} ;:'"\,<>./?@#$%^&*_~''').lower())

        word_frequency = Counter()
        for word in barewords:
            word_frequency[word] += 1
        del word_frequency['']

        [print(f'{word_count[0]} {word_count[1]}') for word_count in word_frequency.most_common(10)]

if __name__ == '__main__':
    count_unique_words('hamlet.txt')



# # Instructor's solution... (update() method looks a lot cleaner, also looping through lines)
# def count_unique_words(filename='hamlet.txt'):
#     words = collections.Counter()
#     # Extract the data into Python.
#     with open(filename) as f:
#         for line in f:
#             words.update(line.split())
#
#     # Calculate the ten most common words.
#     for word, count in words.most_common(10):
#         print(word, count)
