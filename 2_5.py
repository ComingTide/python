class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f'{self.name} {self.price - self.discount}'


child = ItemDiscountReport('sale', 10, 1)
print(child)
