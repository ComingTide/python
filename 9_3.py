class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия:{self.surname}, {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus


worker_1 = Position('Антон', 'Дутов', 'программист', {"wage": 100000, "bonus": 50000})
print(worker_1.get_full_name())
print(worker_1.get_total_income())