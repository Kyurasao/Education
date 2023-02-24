"""
Задача 4
Вывести:
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

N = 5


def main(n):
    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            print(n + 1 - i, end=' ')
        print()


if __name__ == '__main__':
    main(N)
