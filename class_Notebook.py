class Notebook:
    def __init__(self, pages, size='a4', spacing='college'):
        self.pages = pages
        self.size = size
        self.spacing = spacing
        self.color = 'rainbow'

notebook1 = Notebook(100, 'a6', 'wide')
notebook2 = Notebook(1000, size='a5', spacing='double')
notebook3 = Notebook(1111)

if __name__ == '__main__':
    print(notebook1.__dict__)
    print(notebook1.spacing)
    print(notebook1.color, end='\n\n')

    print(notebook2.__dict__)
    print(notebook2.spacing)
    print(notebook2.color, end='\n\n')

    print(notebook3.__dict__)
    print(notebook3.spacing)
    print(notebook3.color, end='\n\n')
