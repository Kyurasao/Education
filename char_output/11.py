"""
Задача 11
Вывести:
5 4 3 2 1 1 2 3 4 5
5 4 3 2 2 3 4 5
5 4 3 3 4 5
5 4 4 5
5 5
"""

N = 5


def main(n):
    for i in range(n):
        for j in range(1, n + 1 - i):
            print(n + 1 - j, end=' ')
        for j in range(n - i, 0, -1):
            print(n + 1 - j, end=' ')
        print()


if __name__ == '__main__':
    main(N)
