"""
Задача 10
Вывести:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""

N = 5


def main(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=' ')
        for k in range(j, 0, -1):
            print(k, end=' ')
        print()


if __name__ == '__main__':
    main(N)
