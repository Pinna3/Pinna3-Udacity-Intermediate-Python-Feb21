def read_content(filename='words.txt'):
    with open(filename, 'r') as f:
        return f.read().strip().replace(',', ' ')

word_frequency_content = read_content()

def parse_content(content):
    string = ''
    for i, ch in enumerate(content):
        if ch.isalpha() is True and content[i-1].isalpha() is False and i != 0:
            string += ' '
            string += ch
        elif ch.isalpha():
            string += ch
        elif ch.isnumeric() is True and content[i-1].isnumeric() is False:
            string += ' '
            string += ch
        elif ch.isnumeric() and content[i-1].isnumeric():
            string += ch
    split = string.split(' ')

    keys = []
    values = []
    for i, item in enumerate(split):
        if i % 2 != 0:
            values.append(item)
        else:
            keys.append(item)

    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict

print(parse_content(word_frequency_content))



# def parse_content(content):
#     words = {}
#     for line in content.split('\n'):
#         word, frequency = line.split()
#         words[word] = int(frequency)
#     return words
