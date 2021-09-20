from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "чайник", "шлёпа", "дверь"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "после еды", "после сна", "обычно"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "в депрессии", "приуныл", "доволен собой"]


def get_jokes(n, repeat=False):
    """
    Возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков -
    nouns=[],adverbs=[],adjectives=[] - (по одному из каждого)

    :param n: кол-во шуток
    :param repeat: флаг, разрешающий/запрещающий повторы слов в шутках
    :return: случайные шутки

    """
    new_nouns, new_adverbs, new_adjectives = nouns.copy(), adverbs.copy(), adjectives.copy()
    create_joke = []
    minimal_list = min(new_nouns, new_adverbs, new_adjectives)

    while n and len(minimal_list):
        id_num = randrange(len(minimal_list))  # работа в диапазоне минимального списка
        if repeat:  # удаляем элемент при помощи .pop / если есть флаг
            create_joke.append(f"{new_nouns.pop(id_num)} {new_adverbs.pop(id_num)} {new_adjectives.pop(id_num)}")
        else:  # используем choice - выбираем один элемент случайным образом из списка, строки, кортежа или range()
            create_joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1  # уменьшаем кол.во итераций
    return create_joke


print(get_jokes(10, True))
