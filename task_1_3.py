"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
"""
"""
До:    31.6 MiB      0.5 MiB       10003       array = [randint(0, 100000) for i in range(10000)]
После: 31.6 MiB      0.0 MiB       10003       array_np = np.array([randint(0, 100000) for i in range(10000)])
"""

from memory_profiler import profile
from random import randint
import numpy as np


@profile
def func_1():
    array = [randint(0, 100000) for i in range(10000)]
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@profile
def func_2():
    array_np = np.array([randint(0, 100000) for i in range(10000)])
    u, c = np.unique(array_np, return_counts=True)
    m_idx = c.argmax()
    num = u[m_idx]
    m = c[m_idx]

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == "__main__":
    print(func_1())
    print(func_2())