N = [1, 2, 3, 4, 230, 5, 6, 238, 237, 7, 8, 9, 10]


def main():    # нужно ли тут указывать тип данных результата??????????
    res = []
    if 237 in N:
        for el in N[:N.index(237)]:
            if el % 2 == 0:
                res.append(el)
    else:
        return print(f'число 237 не встречается в списке {N}')
    print(f'результат: {res}')


if __name__ == '__main__':
    main()
