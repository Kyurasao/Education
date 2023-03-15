"""
0014
Записать в массив все числа в диапазоне от 54 до 9184 кратные 5;
"""


def main() -> None:
    lst = [x for x in range(54, 9184) if x % 5 == 0]
    print(f'Результат: {lst}')


if __name__ == '__main__':
    main()
