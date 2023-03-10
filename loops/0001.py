"""
На вход функция more_than_five(lst) получает список из целых чисел.
Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.
"""

LST = [x for x in range(-10, 10, 2)]


def more_than_five(lst: list) -> list:
    res_list = []
    for i in lst:
        if abs(i) > 5:
            res_list.append(i)
    return res_list


def main():
    print(more_than_five(LST))


if __name__ == '__main__':
    main()
