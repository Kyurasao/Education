"""
Задача 4
Напишите программу для слияния нескольких словарей в один.
"""

# мне нужно как-то учесть замену значения при наличии одинаковых ключей в словарях??

DICT_1 = {'a': {500, 0}, 'b': [1, 2], 'c': '560', 'd': 400, 'e': 5874, 'f': 20}
DICT_2 = {'a': 50, 'b': [1], 'g': 874}


def main(d_1, d_2: dict) -> None:
    list_of_duble_key = []
    list_of_duble_value = []
    for key_1 in d_1.keys():
        for key_2 in d_2.keys():
            if key_1 == key_2:
                list_of_duble_key.append(key_1)
                list_of_duble_value.append(d_1[key_1])
    d_duble = dict(zip(list_of_duble_key, list_of_duble_value))
    d_1.update(d_2)
    print(f'Результат объединения:\n{d_1},\nэлементы с одинаковыми ключами, которые были утеряны в результате объединения:\n{d_duble}')


if __name__ == '__main__':
    main(DICT_1, DICT_2)
