"""
0015
[for] Пользователь вводит числа a и b. Вывести все целые числа, расположенные между ними.
"""

NUMBERS = '0 6'


def main(s: str) -> None:
    lst = s.split(' ')
    if float(lst[0]) < float(lst[1]):
        lo, hi = float(lst[0]), float(lst[1])
    else:
        lo, hi = float(lst[1]), float(lst[0])
    if hi - lo < 1:
        print(f'между введенными числами {lst[0]} и {lst[1]} нету целых чисел')
    else:
        if hi % 1 != 0:
            res = ', '.join([str(i) for i in range(int(lo // 1) + 1, int(hi // 1) + 1)])
        else:
            res = ', '.join([str(i) for i in range(int(lo // 1) + 1, int(hi // 1))])
        print(f'между введенными числами "{lst[0]}" и "{lst[1]}" находятся: {res}')


if __name__ == '__main__':
    main(NUMBERS)
