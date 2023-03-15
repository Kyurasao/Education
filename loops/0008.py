"""
0008
Даны три числа. Вывести на экран «yes«, если среди них есть одинаковые, иначе вывести “ERROR”;
"""

NUM = [1, 2, 6]


def main(x: list) -> None:
    for j in range(len(x)):
        count = 0
        same = x[j]
        for k in range(j, len(x)):
            if same == x[k]:
                count += 1
            if count == 2:
                return print(f'yes')
    print('error')


if __name__ == '__main__':
    main(NUM)
