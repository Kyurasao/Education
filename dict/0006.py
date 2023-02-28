import random

"""
0006
Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте
функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто
встречаемых чисел.
"""

LIST = [random.randint(0, 10) for x in range(10)]
STRING = ''.join(str(el) for el in LIST)


def count_it(s: str) -> dict:
    list_keys = []
    list_values = []
    for el in s:
        list_keys.append(el)
        list_values.append(s.count(el))
    dict_from_str = dict(zip(list_keys, list_values))
    dict_from_str_rev = dict(sorted(dict_from_str.items(), reverse=True, key=lambda el: el[1]))
    list_fin = []
    count = 0
    for item in dict_from_str_rev.items():
        if count < 3:
            list_fin.append(item)
            count += 1
    # print(dict_from_str)
    # print(dict_from_str_rev)
    return dict(list_fin)


def main() -> None:
    print(f'Исходная строка: "{STRING}"')
    print(count_it(STRING))


if __name__ == '__main__':
    main()
