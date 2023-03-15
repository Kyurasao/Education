"""
0013
Перемножить все не чётные значения в диапазоне от 0 до 9435;
"""

NUMBERS = [x for x in range(9436)]


def main(lst: list) -> None:
    res = 1
    for i in lst:
        if i != 0 and i % 2 == 0:
            res *= i
    print(f'Числовой ряд: {lst},\nпроизведение его четных членов равна: {res}')


if __name__ == '__main__':
    main(NUMBERS)
