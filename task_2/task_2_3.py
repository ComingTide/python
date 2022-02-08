"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

from random import randint
from timeit import timeit
from statistics import median


if __name__ == '__main__':
    m = 5
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))

    m = 50
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))

    m = 500
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))