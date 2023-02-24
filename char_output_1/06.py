"""
Задача 6
Вывести:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

N = 5


def main(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i - j, end=' ')
        print()


if __name__ == '__main__':
    main(N)
