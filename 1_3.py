import random


def get_rand_nums_gen(start: int, end: int, exclusions=None) -> iter:
    """ Генерирует рандомные числа
    :param start: стартовая позиция
    :param end: конечная позиция
    :param exclusions: список чисел, которые нужно исключить
    :return: yield-генератор из случайных чисел
    """
    if exclusions is None:
        exclusions = []
    while True:
        rand_num = random.randint(start, end)
        if rand_num not in exclusions:
            yield rand_num


def get_rand_nums_list(gen: iter, quantity=10) -> list:
    """ Создаёт список из случайных чисел
    :param gen: генератор случайных чисел
    :param quantity: количество элементов в списке
    :return: список из случайных чисел
    """
    nums_list = []
    for el in gen:
        nums_list.append(el)
        quantity -= 1
        if quantity <= 0:
            break
    return nums_list



def get_rand_nums_dict(gen: iter, quantity=10) -> dict:
    """ Создаёт словарь из случайных чисел
    :param gen: генератор случайных чисел
    :param quantity: количество элементов в словаре
    :return: словарь из случайных чисел
    """
    nums_list = {}
    for num, el in enumerate(gen, 1):
        nums_list.update({f'elem_{num}': el})
        quantity -= 1
        if quantity <= 0:
            break
    return nums_list


if __name__ == '__main__':
    nums_gen = get_rand_nums_gen(-3, 3, [0])
    print(get_rand_nums_list(nums_gen, 10))
    print(get_rand_nums_dict(nums_gen, 10))
