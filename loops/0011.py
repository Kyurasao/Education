"""
0011
Вывести на экран все чётные значения в диапазоне от 1 до 497;
"""


def main() -> None:
    print([i for i in range(1, 498) if i % 2 == 0])


if __name__ == '__main__':
    main()
