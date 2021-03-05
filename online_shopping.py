class User:
    def __init__(self, id, name, reviews=set()):
        self.id = id
        self.name = name
        self.reviews = reviews
    def sell_product(self, product, description, price):
        product = Product(product, description, price, self.name)
        return product
    def buy_product(self, product):
        product.available = False
    def write_review(self, description, product):
        product_review = Review(product, description, self.name)
        tuple = (product.product, description)
        self.reviews.add(tuple)
        product.reviews.add(tuple)
        return tuple
    def __str__(self):
        return f'User({self.name}, {self.id})'

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')


class Product:
    def __init__(self, product, description, price, seller, reviews=set(), available=True):
        self.product = product
        self.description = description
        self.seller = seller
        self.reviews = reviews
        self.price = price
        self.available = available
    def __str__(self):
        return f'Product({self.product}, seller={self.seller}, availability={self.available})'

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)
mary.buy_product(keyboard)
print(keyboard.available)


class Review:
    def __init__(self, product, description, user):
        self.product = product
        self.description = description
        self.user = user
    def  __str__(self):
        return f'Review({self.product}, description={self.description}, user={self.user})'

review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)
print(review in keyboard.reviews)
