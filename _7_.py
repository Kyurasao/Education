"""
Задача 7
Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
а каждое число внутри равно сумме двух расположенных над ним чисел.
"""

N = 10


def main(n: int) -> None:
    list_res = []
    for i in range(n):
        if i == 0:
            list_res.append([1])
            print(' '.join(map(str, list_res[i])).center(40))
        elif i == 1:
            list_res.append([1, 1])
            print(' '.join(map(str, list_res[i])).center(40))
        else:
            list_in = [1]
            for j in range(1, i):
                list_in.append(list_res[i - 1][j - 1] + list_res[i - 1][j])
            list_in.append(1)
            list_res.append(list_in)
            print(' '.join(map(str, list_res[i])).center(40))


if __name__ == '__main__':
    main(N)
