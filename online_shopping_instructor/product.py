class Product:
    def __init__(self, name, description, price, seller, available=True):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.available = available
        self.reviews = []

    def __str__(self):
        return f'Product({self.name}, {self.description}, at ${self.price})'
