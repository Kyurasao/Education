"""
Задача 1
Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
а каждое число внутри равно сумме двух расположенных над ним чисел.
"""

N = 5


def main(n: int) -> None:
    # width = n * 9
    list_res = []
    for i in range(n):
        if i == 0:
            list_res.append([1])
            # print(' '.join(map(str, list_res[i])).center(width))
        elif i == 1:
            list_res.append([1, 1])
            # print(' '.join(map(str, list_res[i])).center(width))
        else:
            list_in = [1]
            for j in range(1, i):
                list_in.append(list_res[i - 1][j - 1] + list_res[i - 1][j])
            list_in.append(1)
            list_res.append(list_in)
            wi = len(str(list_res[i][round(i / 2)]))
            # print(' '.join(map(str, list_res[i])).center(width))
    print(wi)
    probel = wi * ' '
    width = n * 5
    list_res = []
    for i in range(n):
        if i == 0:
            list_res.append([1])
            print(probel.join(map(str, list_res[i])).center(width))
        elif i == 1:
            list_res.append([1, 1])
            print(probel.join(map(str, list_res[i])).center(width))
        else:
            list_in = [1]
            for j in range(1, i):
                list_in.append(list_res[i - 1][j - 1] + list_res[i - 1][j])
            list_in.append(1)
            list_res.append(list_in)
            print(probel.join(map(str, list_res[i])).center(width))


if __name__ == '__main__':
    main(N)
