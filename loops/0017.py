"""
0017
[for] Пользователь вводит число. Вывести таблицу умножения на это число.
"""

NUMBER = '3'


def main(s: str) -> None:
    for i in range(1, 11):
        print(f'{s} * {i} = {int(s) * i}')


if __name__ == '__main__':
    main(NUMBER)
