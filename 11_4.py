class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        """ добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования"""
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        """ извлекаем из значения обьект по названию группы.
        дальше можно расширить поиск по серии, марки или еще чему либо"""
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def __repr__(self):
        return f'{self.name}-{self.make}-{self.year}'


def action():
    return 'Печатает'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series


def action():
    return 'Сканирует'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


def action():
    return 'Копирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90)
sklad.add_to(scaner)
scaner = Scaner('hp', '311', 97)
sklad.add_to(scaner)
scaner = Scaner('hp', '330', 99)
sklad.add_to(scaner)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('hp')
print(sklad._dict)