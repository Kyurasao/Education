"""
Задача 1
Вывести:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

N = 5


def main(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print()


if __name__ == '__main__':
    main(N)
