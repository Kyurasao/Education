"""
Задача 3
Вывести:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

N = 5


def main(n):
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end=' ')
        print()


if __name__ == '__main__':
    main(N)
