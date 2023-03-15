"""
0021
Пользователь вводит число n и цифру a.
Определить, сколько раз цифра встречается в числе.
(не использовать метод count)
"""

NUM = 1234561231
DIG = 1


def main(num: int, dig: int) -> None:
    res = 0
    for i in range(len(str(num))):
        if int(str(num)[i]) == dig:
            res += 1
    print(f'Цифра {dig} встречается в числе {num} - {res} раз')


if __name__ == '__main__':
    main(NUM, DIG)
