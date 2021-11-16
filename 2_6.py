class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        print(self.price)


one = ItemDiscountReportOne('sale', 5)
one.get_info()

two = ItemDiscountReportTwo('wholesale', 10)
two.get_info()

for obj in (one, two):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(one)
obj_handler(two)