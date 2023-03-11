"""
0007
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
"""

NUMBERS = [x for x in range(1, 101)]


def main(x: list) -> None:
    print(f'Ряд чисел: {x},\nЕго сумма: {sum(x)}')


if __name__ == '__main__':
    main(NUMBERS)
