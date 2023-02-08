N = [1, 2, 3, 4, 230, 5, 6, 237, 238, 7, 8, 9, 10]


def main():
    res = []
    for el in N[:N.index(237)]:
        if el % 2 == 0:
            res.append(el)
    print(f'результат: {res}')


if __name__ == '__main__':
    main()
