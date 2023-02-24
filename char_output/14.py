"""
Задача 14
Вывести:
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
"""

N = 5


def main(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=' ')
        num += 2
        print()


if __name__ == '__main__':
    main(N)
