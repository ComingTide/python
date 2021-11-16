class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(self.__name, self.__price)


child = ItemDiscountReport('sale', 10)
child.set_price(30)
print(child.get_parent_data())