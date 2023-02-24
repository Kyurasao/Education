"""
Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.
"""

MY_DICT = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}


def main(d: dict) -> None:
    print(dict(sorted(d.items(), key=lambda el: el[1])))
    print(dict(sorted(d.items(), reverse=True, key=lambda el: el[1])))


if __name__ == '__main__':
    main(MY_DICT)
