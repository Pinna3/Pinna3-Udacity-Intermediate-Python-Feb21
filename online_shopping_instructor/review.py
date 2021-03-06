class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return f'Review pf {self.product} by {self.user}: "{self.content}"'
