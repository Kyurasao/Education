"""
Задача 9
Вывести:
1
3 2
6 5 4
10 9 8 7
"""

N = 5


def main(n):
    c = 0
    for i in range(n - 1):
        l = []
        for j in range(i + 1):
            c += 1
            l.append(c)
        l.reverse()
        for k in range(i + 1):
            print(l[k], end=' ')
        print()


if __name__ == '__main__':
    main(N)
