"""
0005
Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им
словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it».
Воссоздайте эту функцию.
"""

MY_DICT = {'first_one': 'we can do it'}
D = {'a': 1, 'b': 2, 'c': 3}
С = {'g': 1, 'h': 2, 'l': 3}


def biggest_dict(**kwargs) -> None:
    MY_DICT.update(kwargs)


# КЛЮЧ + ЗНАЧЕНИЕ = KEY + WORD >> KEYWORD >> KW

def main() -> None:
    print(f'Словарь до объединения: {MY_DICT}')
    biggest_dict(a=1, b=2, c=3, g=1, h=2, l='zikkurat')
    print(f'Словарь после объединения: {MY_DICT}')


if __name__ == '__main__':
    main()
