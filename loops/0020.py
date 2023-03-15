"""
0020
[while] Дано натуральное число. Определить сумму цифр в нем.
"""

NUM = 123456


def main(number: int) -> None:
    res = 0
    num = number
    while num != 0:
        val = num % 10
        res += val
        num = num // 10
    print(f'Сумма цифр числа {number} равна {res}')


if __name__ == '__main__':
    main(NUM)
