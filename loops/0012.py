"""
0012
Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
"""

NUMBERS = [x for x in range(15)]


def main(lst: list) -> None:
    print(f'Числовой ряд: {lst},\nсумма его членов равна: {sum(lst)}')


if __name__ == '__main__':
    main(NUMBERS)
