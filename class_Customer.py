class Customer:
    def __init__(self, *names, tier='free', bill=0):
        self.name = ' '.join(names)
        self.tier = tier
        self.bill = bill
        self.access_list = {'tier': 'free', 'title': '1812 Overture'}
        if tier == 'premium':
            self.access_list_prem = {'tier': 'premium', 'title': 'William Tell Overture'}
    def can_access(self, tier_title_dict):
        if self.tier == 'premium':
            return tuple(tier_title_dict.items()) == tuple(self.access_list.items()) or tuple(tier_title_dict.items()) == tuple(self.access_list_prem.items())
        else:
            return tuple(tier_title_dict.items()) == tuple(self.access_list.items())
    def bill_for(self, months):
        return self.bill * months
    @classmethod
    def premium(cls, *names, tier='premium', bill=10):
        return cls(*names, tier='premium', bill=10)


if __name__ == '__main__':
    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False
    victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria
