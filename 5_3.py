tutor = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Илья', 'Игорь', 'Алёна'
]
klass = [
    '9А', '7В', '9Б', '9В', '8Б', '11А', '10Б', '9А'
]


# реализация генератора, возвращающий кортежи вида (<tutor>, <klass>)


def school(tutor, klass):
    tutor_gen = (element for element in tutor)
    klass_gen = (element for element in klass)
    for school_gen in zip(klass_gen, tutor_gen):
        yield school_gen[::-1]
    for rest in tutor_gen:
        yield rest, None


# Количество генерируемых кортежей не больше длины списка tutor
# Если в списке klass меньше элементов, чем в списке tutor
# выводит последние кортежи в виде: (<tutor>, None)

students = school(tutor, klass)

for item in students:
    print(item)
