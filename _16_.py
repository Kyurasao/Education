"""
Задача 16
Выведите список файлов в указанной директории.
"""

import os

PATH = 'C:/Users/Антон/Documents/GitHub/Education' # а как вывести путь до текущего диалога?


def main(string: str) -> None:
    print(f' Содержимое каталога "{string}":\n {os.listdir(string)}')


if __name__ == '__main__':
    main(PATH)
