def integer_equal_decimal(num: float) -> bool or None:
    """Проверка дробное ли число, если да - сравнение чисел до и после запятой
    :param num: float число
    :return: None - если целое число, True - числа до и после запятой равны,
    иначе False
    """
    int_dec = tuple(map(int, str(num).split('.')))
    if not int_dec[1]:
        print('Число целое')
    else:
        print('Число дробное')
        return int_dec[0] == int_dec[1]


if __name__ == '__main__':
    while True:
        input_data = input('Введите число: ')
        try:
            number = float(input_data)
        except ValueError:
            try:
                # проверяем возможно разделитель "," вместо ".", замена ","
                input_data = input_data.replace(',', '.')
                # если снова ошибка просим ввести правильное число
                number = float(input_data)
            except ValueError:
                print(f'Необходимо ввести целое или дробное число!')
                continue
        print(integer_equal_decimal(number))
        break