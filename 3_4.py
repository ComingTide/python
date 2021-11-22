import random
import string
from os import getcwd
from os.path import join


def file_output(path: str) -> None:
    """Построчный вывод содержимого файла
    :param path: абсолютный путь файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)


def create_text_file(file_name: str, length=100) -> None:
    """Создавать текстовый файл из рандомных букв и цифр
    :param file_name: имя файла
    :param length: количество строк
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            letters = string.ascii_lowercase
            rand_string = ''.join(
                random.choice(letters) for _ in range(length))
            texts_list = [letter * 23 for letter in rand_string]

            nums_list = [random.randint(0, 10000000000) for _ in range(length)]

            texts_nums_zip = zip(texts_list, nums_list)

            for el in texts_nums_zip:
                file.write(f'{el[0]} {el[1]}\n')
    except FileExistsError:
        print('Файл уже существует!')
    finally:
        file_output(join(getcwd(), file_name))


if __name__ == '__main__':
    create_text_file('task_4.txt')