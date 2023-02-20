"""
Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.
"""

MY_DICT = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}


def main(d: dict) -> None:
    print(sorted(d.values()))
    print(sorted(d.values(), reverse=True))


if __name__ == '__main__':
    main(MY_DICT)
