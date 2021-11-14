str_from_list = lambda rows_list: '\t'.join(rows_list)


def print_multiplication_table(a: int, b: int) -> None:
    """ Вывод таблицы умножения
    :param a: значения первых переменных от 2 до a (включительно)
    :param b: значения вторых переменных от 1 до b (включительно)
    """
    try:
        for col in range(2, a + 1):
            rows_list = [f'{col} x {row} = {col * row}' for row in
                         range(1, b + 1)]
            print(str_from_list(rows_list))
    except TypeError as e:
        print(f'Функция принимает только числа! TypeError: {e}')


if __name__ == '__main__':
    print_multiplication_table(9, 9)
    print_multiplication_table('9', 9)