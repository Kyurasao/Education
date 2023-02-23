N = 5


def main(n):
    # 18
    # for i in range(n):
    #     for j in range(i + 1):
    #         print('*', end=' ')
    #     print()

    # 17
    # for i in range(n):
    #     s = ''
    #     for j in range(n - i, 0, -1):
    #         s += '*' + ' '
    #     print(s.center(n * 2))

    # 16
    # for i in range(n):
    #     s = ''
    #     for j in range(i + 1):
    #         s += '*' + ' '
    #     print(s.center(n * 2))

    # 15
    # for i in range(n):
    #     for j in range(n - i, 0, -1):
    #         print(' ', end=' ')
    #     for j in range(i + 1):
    #         print(j + 1, end=' ')
    #     print()

    # 14
    # num = 1
    # for i in range(n):
    #     for j in range(i + 1):
    #         print(num, end=' ')
    #     num += 2
    #     print()

    # 13
    # for i in range(n):
    #     num = 0
    #     for j in range(i + 1):
    #         print(num, end=' ')
    #         num += i
    #     print()

    # 12
    # for i in range(n):
    #     num = 10
    #     for j in range(i + 1):
    #         print(num, end=' ')
    #         num -= 2
    #     print()

    # 11
    # for i in range(n):
    #     for j in range(1, n + 1 - i):
    #         print(n + 1 - j, end=' ')
    #     for j in range(n - i, 0, -1):
    #         print(n + 1 - j, end=' ')
    #     print()

    # 10
    # for i in range(n):
    #     for j in range(i + 1):
    #         print(j + 1, end=' ')
    #     for k in range(j, 0, -1):
    #         print(k, end=' ')
    #     print()

    # 999999999999999999999999999999999999999999999999999999999999999999
    # c = 11
    # for i in range(n):
    #
    #     for j in range(i + 1):
    #         c -= 1
    #
    #         print(c, end=' ')
    #
    #     print()

    # 8
    # stop = 1
    # c = 0
    # for i in range(n):
    #     for j in range(stop):
    #         c += 1
    #         if c >= 26:
    #             return
    #         print('{0:2}'.format(c), end=' ')
    #     stop += 2
    #     print()

    # 7
    # for i in range(1, n + 1):
    #     for j in range(n + 1 - i):
    #         print(j + 1, end=' ')
    #     print()

    # 6
    # for i in range(1, n + 1):
    #     for j in range(i):
    #         print(i - j, end=' ')
    #     print()

    # 5
    # for i in range(1, n + 1):
    #     for j in range(n + 1 - i):
    #         print(n, end=' ')
    #     print()

    # 4
    # for i in range(1, n + 1):
    #     for j in range(n + 1 - i):
    #         print(n + 1 - i, end=' ')
    #     print()

    # 3
    # for i in range(n):
    #     for j in range(1, i + 2):
    #         print(j, end=' ')
    #     print()

    # 2
    # for i in range(1, n + 1):
    #     for j in range(n - i + 1):
    #         print(i, end=' ')
    #     print()

    # 1
    # for i in range(1, n + 1):
    #     for j in range(i):
    #         print(i, end=' ')
    #     print()


if __name__ == '__main__':
    main(N)
