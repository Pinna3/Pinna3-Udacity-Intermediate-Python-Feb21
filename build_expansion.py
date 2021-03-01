class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
    def build_expansion(self, additional):
        self.size = self.size + additional
        #self.size += additional

if __name__ == '__main__':
    home = House(2000)
    print(home.size)  # 2000
    home.build_expansion(500)
    print(home.size)  # 2500
