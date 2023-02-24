"""
Задача 8
Вывести:
1
2 3 4
5 6 7 8 9
"""

N = 5


def main(n):
    stop = 1
    c = 0
    for i in range(n):
        for j in range(stop):
            c += 1
            if c >= 10:
                return
            print('{0:1}'.format(c), end=' ')
        stop += 2
        print()


if __name__ == '__main__':
    main(N)
