"""
генератор нечётных чисел от 1 до n (включительно), использует ключевое слово yield
"""


def odd_to(n):
    for num in range(1, n + 1, 2):
        yield num


test = odd_to(15)
print(list(test))
