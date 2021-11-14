bank_dep_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
bank_dep_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
bank_dep_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
bank_deposits = [bank_dep_1, bank_dep_2, bank_dep_3]


def calculate_total_amount(amount: float, term: int) -> float or str:
    """ Функция возвращает сумму вклада на конец срока
    :param amount: сумму вклада
    :param term: срок вклада
    :return: сумма вклада на конец срока
    """
    total_amount = 0
    try:
        for bank_deposit in bank_deposits:
            if bank_deposit['begin_sum'] <= amount < bank_deposit['end_sum']:
                total_amount = amount
                percent = bank_deposit[term] / 100

                total_amount += amount * percent * (term / 12)
        if not total_amount:
            raise ValueError('Указана неправильная сумма вклада')
        return total_amount
    except KeyError as e:
        return f'Указан неправильный срок вклада. KeyError {e}'
    except ValueError as e:
        return e


if __name__ == '__main__':
    print(calculate_total_amount(10, 1))
    print(calculate_total_amount(1000, 3))

    print(calculate_total_amount(1000, 24))
    print(calculate_total_amount(9999, 12))
    print(calculate_total_amount(1000, 12))
    print(calculate_total_amount(10000, 6))