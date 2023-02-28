from collections import OrderedDict

"""
0007
Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

DICT = OrderedDict({'1': 'value 1', '2': 'value 2', '3': 'value 3', '4': 'value 4', '5': 'value 5'})


def main(d: dict) -> None:
    print(f'Исходный словарь:\n {d}')
    old_id = id(d)
    d.move_to_end('1', last=True)
    d.popitem(last=False)
    d.move_to_end('5', last=False)
    d['new_key'] = 'new_value'
    print(f'Полученный словарь:\n {d}')
    new_id = id(d)
    print(f'ID исходного словаря:   "{old_id}"\nID полученного словаря: "{new_id}"')


if __name__ == '__main__':
    main(DICT)
