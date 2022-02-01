"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""

from collections import deque
import timeit

list_test = [i for i in range(999)]
deque_test = deque([i for i in range(999)])

list_append_code = """
for i in range(100):
    list_test.append(i)
"""

deque_append_code = """
for i in range(100):
    deque_test.append(i)
"""

list_popfirst_code = """
for i in range(100):
    list_test.pop(0)
"""

deque_popleft_code = """
for i in range(100):
    deque_test.popleft()
"""

list_insertfirst_code = """
for i in range(100):
    list_test.insert(i, 0)
"""

deque_insertleft_code = """
for i in range(100):
    deque_test.appendleft(i)
"""

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_append_code, setup='from __main__ import list_test', number=100000))
print(timeit.timeit(deque_append_code, setup='from __main__ import deque_test', number=100000))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_popfirst_code, setup='from __main__ import list_test', number=10))
print(timeit.timeit(deque_popleft_code, setup='from __main__ import deque_test', number=10))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')

print("Длинна объектов Лист / Дека - ДО: ", len(list_test), len(deque_test))
print(timeit.timeit(list_insertfirst_code, setup='from __main__ import list_test', number=10))
print(timeit.timeit(deque_insertleft_code, setup='from __main__ import deque_test', number=10))
print("Длинна объектов Лист / Дека - ПОСЛЕ: ", len(list_test), len(deque_test), '\n')