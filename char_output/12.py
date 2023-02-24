"""
Задача 12
Вывести:
10
10 8
10 8 6
10 8 6 4
10 8 6 4 2
"""

N = 5


def main(n):
    for i in range(n):
        num = 10
        for j in range(i + 1):
            print(num, end=' ')
            num -= 2
        print()


if __name__ == '__main__':
    main(N)
