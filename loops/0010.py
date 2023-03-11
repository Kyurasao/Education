"""
0010
Дано три числа. Найти количество положительных чисел среди них;
"""
import random

res = []
for i in range(3):
    res.append(random.randint(-6, 6))


def main(x: list) -> None:
    count = 0
    for j in res:
        if j > 0:
            count += 1
    print(f'Дано: {x}, среди них положительных: {count}')


if __name__ == '__main__':
    main(res)
