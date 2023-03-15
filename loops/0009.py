"""
0009
Даны три числа. Вывести на экран «yes«, если можно взять какие-то два из них и в сумме получить третье
"""

NUM = [2, 3, 5]


def main(lst: list) -> None:
    for j in range(len(lst)):
        lst_1 = lst[:]
        add_1 = lst_1[j]
        lst_1.pop(j)
        for k in range(len(lst_1)):
            lst_2 = lst_1[:]
            add_2 = lst_2[k]
            lst_2.pop(k)
            for i in range(len(lst_2)):
                if add_1 + add_2 == lst_2[i]:
                    return print(f'yes')
    print('error')


if __name__ == '__main__':
    main(NUM)
