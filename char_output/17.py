"""
Задача 17
Вывести:
        * * * * * *
         * * * * *
          * * * *
           * * *
            * *
             *
"""

N = 6


def main(n):
    for i in range(n):
        s = ''
        for j in range(n - i, 0, -1):
            s += '*' + ' '
        print(s.center(n * 2))


if __name__ == '__main__':
    main(N)
