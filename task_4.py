"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
import timeit

common_dict = {i: i * i for i in range(999)}
ordered_dict = OrderedDict({i: i * i for i in range(999)})

common_dict_insert = """
for i in range(1001, 999999):
    common_dict[i] = i
"""

ordered_dict_insert = """
for i in range(1001, 999999):
    ordered_dict[i] = i
"""

common_dict_pop = """
for i in range(999):
    common_dict.popitem()
"""

ordered_dict_pop = """
for i in range(999):
    ordered_dict.popitem()
"""

common_dict_max = """
max(common_dict)
"""

ordered_dict_max = """
max(ordered_dict)
"""

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_insert, setup='from __main__ import common_dict', number=1), 'Dict')
print(timeit.timeit(ordered_dict_insert, setup='from __main__ import ordered_dict', number=1), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_pop, setup='from __main__ import common_dict', number=100), 'Dict')
print(timeit.timeit(ordered_dict_pop, setup='from __main__ import ordered_dict', number=100), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')

print("Длинна объектов Dict / OrderedDict - ДО: ", len(common_dict), len(ordered_dict))
print(timeit.timeit(common_dict_max, setup='from __main__ import common_dict', number=100), 'Dict')
print(timeit.timeit(ordered_dict_max, setup='from __main__ import ordered_dict', number=100), 'OrderedDict')
print("Длинна объектов Dict / OrderedDict - ПОСЛЕ: ", len(common_dict), len(ordered_dict), '\n')