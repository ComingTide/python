"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
"""
чтобы найти все индексы с нечетными значениями, нужно обойти весь список, поэтому 
необходим или в алгоритм вычисления четности или в обходе. 
Делаю вывод, что lc быстрее цикла for потому, что lc тратит меньше времени на 
добавление, поскольку не вызывает метод append. 
Еще одним решением, зависящее от прикладной задачи - генератор. 
Если нужно будет перебирать массив по порядку 
"""


from timeit import timeit


from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


if __name__ == '__main__':
    nums = [randint(0, 10000) for i in range(10000)]

    print('Вариант 1:', timeit('func_1(nums)', number=1000, globals=globals()))
    print('Вариант 2:', timeit('func_2(nums)', number=1000, globals=globals()))
    print('Вариант 3:', timeit('func_3(nums)', number=1000, globals=globals()))

    print(f'Результат{" " if func_1(nums) == func_2(nums) == list(func_3(nums)) else "не "}верен')
