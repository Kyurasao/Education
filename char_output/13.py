"""
Задача 13
Вывести:
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
0 5 10 15 20 25
0 6 12 18 24 30 36
"""

N = 7


def main(n):
    for i in range(n):
        num = 0
        for j in range(i + 1):
            print(num, end=' ')
            num += i
        print()


if __name__ == '__main__':
    main(N)
