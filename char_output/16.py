"""
Задача 16
Вывести:
            *
           * *
          * * *
         * * * *
        * * * * *
       * * * * * *
      * * * * * * *
"""

N = 7


def main(n):
    for i in range(n):
        s = ''
        for j in range(i + 1):
            s += '*' + ' '
        print(s.center(n * 2))


if __name__ == '__main__':
    main(N)
