"""
Задача 5
Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
"""

MY_DICT = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}


def main(d: dict) -> None:
    sort_list = sorted(d.values())
    print(sort_list)
    print(f'В словаре {MY_DICT}\nтри ключа с максимальными значениями: {[key for key in d.keys() if d[key] >= sort_list[-3]]}')


if __name__ == '__main__':
    main(MY_DICT)
