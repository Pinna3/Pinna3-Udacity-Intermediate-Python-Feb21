class Dog:
    def __init__(self, name, tricks=set()):
        self.name = name
        self.tricks = tricks
    def teach(self, trick):
        self.tricks.add(trick)

# Change the broken code above so that the following lines work:
if __name__ == '__main__':
    buddy = Dog('Buddy')
    pascal = Dog('Pascal')
    kimber = Dog('Kimber', tricks={'lie down', 'shake'})
    buddy.teach('sit')
    pascal.teach('fetch')
    buddy.teach('roll over')
    kimber.teach('fetch')
    print(buddy.tricks)  # {'sit', 'roll over'}
    print(pascal.tricks)  # {'fetch'}
    print(kimber.tricks)  # {'lie down', 'shake', 'fetch'}
