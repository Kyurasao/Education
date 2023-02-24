"""
Задача 18
Вывести:
*
* *
* * *
* * * *
* * * * *
"""

N = 5


def main(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()


if __name__ == '__main__':
    main(N)
