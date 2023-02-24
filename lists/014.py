N = [[3, 4, 230, 5, 6, 237, 23, 7, 8], [1, 230, 5, 6, 238, 23, 7, 8, 9], [0, -22, -7, 4, 237, 10]]


def main() -> None:
    for list_el in N:
        res = []
        for el in list_el:
            if el == 237:
                break
            if el % 2 == 0:
                res.append(el)
        print(f'результат - {res}')


if __name__ == '__main__':
    main()
