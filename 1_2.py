import os


def get_files_generator(files: os.scandir) -> iter:
    """ Функция возвращает yield-генератор путей и имён файлов в кортежах
    :param files: итерируемые объект, образованный от os.scandir
    :return: yield-генератор из кортежей путей и имён файлов
    """

    for file in files:
        if file.is_dir():
            with os.scandir(os.path.abspath(file.path)) as files:
                yield from get_files_generator(files)
        else:
            yield os.path.abspath(file.path), file.name


def print_directory_contents(s_path: str) -> None:
    """ Функция распечатывает имена и пути файлов, в том числе вложенные
    Про каталоги в задании не сказано, соответственно выводятся только файлы
    :param s_path: путь до каталога
    """
    with os.scandir(s_path) as files:
        for file in get_files_generator(files):
            print(file)


if __name__ == '__main__':
    print_directory_contents('../../python_developer')