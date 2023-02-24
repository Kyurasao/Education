"""
Задача 15
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
        for j in range(n - i, 0, -1):
            print(' ', end=' ')
        for j in range(i + 1):
            print(j + 1, end=' ')
        print()


if __name__ == '__main__':
    main(N)
