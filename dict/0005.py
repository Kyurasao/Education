"""
0005
Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им
словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it».
Воссоздайте эту функцию.
"""

MY_DICT = {'first_one': 'we can do it'}


def biggest_dict(my: dict, **kwargs) -> dict:
    my |= kwargs
    return my


def main() -> None:
    print(biggest_dict(MY_DICT, a=1, b=2, c=3))


if __name__ == '__main__':
    main()
