"""
Задача 5
Вывести:
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
"""

N = 5


def main(n):
    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            print(n, end=' ')
        print()


if __name__ == '__main__':
    main(N)
