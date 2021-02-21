def create_profile(name, *surnames, **details):
    print(name, *surnames)
    for key, value in details.items():
        print(key, value, sep=': ')

if __name__ == '__main__':
    create_profile('Mike', 'Pinna', 'the', 'Stooge', age=102, eyes='blue',
                    hair='green', height_in=98.5)



# My original (shitty) solution, still worked but now I know better... *surnames
# syntax versus for-loop redundently looping through variatidic positional argument

# def create_profile(name, *surnames, **details):
#     print(name, sep=' ')
#     # for surname in surnames:
#     #     print(surname, end=' ')
#     # print('')
#     for key, value in details.items():
#         print(key, value, sep=': ')
