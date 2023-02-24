"""
Задача 7
Вывести:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

N = 5


def main(n):
    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            print(j + 1, end=' ')
        print()


if __name__ == '__main__':
    main(N)
