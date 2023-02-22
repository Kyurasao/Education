"""
Задача 7
Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
а каждое число внутри равно сумме двух расположенных над ним чисел.
"""

N = 10


def main(n: int) -> None:
    res_list = []
    for i in range(n):
        s = ''
        res_list.append([])
        res_list[i].append(1)
        for j in range(1, i):
            res_list[i].append(res_list[i - 1][j - 1] + res_list[i - 1][j])
        if i > 0:
            res_list[i].append(1)

    for i in range(n):
        print(" " * 2 * (n - i), end=" ")
        for j in range(0, i + 1):
            print('{:5}'.format(res_list[i][j]), end="")
        print()


if __name__ == '__main__':
    main(N)
