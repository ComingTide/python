"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""


"""
ВЫВОДЫ:
Решение 1: самое медленное, рекурсивный вызов требует много ресурсов
Решение 2: быстрее, линейная сложность, откусываем по цифре с конца и набираем новое число
Решение 3: еще быстрее, срезы реализованы не на питоне
Решение 4: обгоняет рекурсию и цикл while, потому что там просто меньше операций
"""

from timeit import timeit
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, revers_num=''):
    enter_num = str(enter_num)
    for i in range(len(enter_num) - 1, -1, -1):
        revers_num += enter_num[i]
    return revers_num


if __name__ == '__main__':

    num_100 = randint(10000, 1000000)
    num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    print('Вариант 1: ')
    print(timeit('revers_1(num_100)', number=100000, globals=globals()))
    print(timeit('revers_1(num_1000)', number=100000, globals=globals()))
    print(timeit('revers_1(num_10000)', number=100000, globals=globals()))

    print('Вариант 2: ')
    print(timeit('revers_2(num_100)', number=100000, globals=globals()))
    print(timeit('revers_2(num_1000)', number=100000, globals=globals()))
    print(timeit('revers_2(num_10000)', number=100000, globals=globals()))

    print('Вариант 3: ')
    print(timeit('revers_3(num_100)', number=100000, globals=globals()))
    print(timeit('revers_3(num_1000)', number=100000, globals=globals()))
    print(timeit('revers_3(num_10000)', number=100000, globals=globals()))

    print('Вариант 4: ')
    print(timeit('revers_4(num_100)', number=100000, globals=globals()))
    print(timeit('revers_4(num_1000)', number=100000, globals=globals()))
    print(timeit('revers_4(num_10000)', number=100000, globals=globals()))
