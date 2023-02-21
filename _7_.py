"""
Задача 7
Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
а каждое число внутри равно сумме двух расположенных над ним чисел.
"""

N = 10


def main(n: int) -> None:
    list1 = []
    for i in range(n):
        if i == 0:
            list1.append([1])
            print(list1)
        elif i == 1:
            list1.append([1, 1])
            print(list1)
        elif i >= 2:
            list_j = [1]
            for j in range(1, i):
                list_j.append(list1[i - 1][j - 1] + list1[i - 1][j])
            list_j.append(1)
            list1.append(list_j)
            print(list1)


if __name__ == '__main__':
    main(N)
