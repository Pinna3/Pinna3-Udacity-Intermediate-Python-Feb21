class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = set()
    def teach(self, trick):
        self.tricks.add(trick)

# Change the broken code above so that the following lines work:
#
if __name__ == '__main__':
    buddy = Dog('Buddy')
    pascal = Dog('Pascal')
    buddy.teach('sit')
    pascal.teach('fetch')
    buddy.teach('roll over')
    print(buddy.tricks)  # {'sit', 'roll over'}
    print(pascal.tricks)  # {'fetch'}
