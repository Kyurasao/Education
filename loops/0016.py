"""
0016
[for] Доработать предыдущую задачу так, чтобы выводились только числа, делящиеся на 5 без остатка.
"""

NUMBERS = '-2 -12'


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
            res = ', '.join([str(i) for i in range(int(lo // 1) + 1, int(hi // 1) + 1) if i % 5 == 0])
        else:
            res = ', '.join([str(i) for i in range(int(lo // 1) + 1, int(hi // 1)) if i % 5 == 0])
        print(f'между введенными числами "{lst[0]}" и "{lst[1]}" находятся: {res}')


if __name__ == '__main__':
    main(NUMBERS)
