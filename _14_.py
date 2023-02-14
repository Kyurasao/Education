N = [[1, 2, 3, 4, 230, 5, 6, 238, 23, 7, 8, 9, 10], [1, 2, 3, 4, 230, 5, 6, 238, 237, 7, 8, 9, 10], [0, -2, 4, 237]]


def main() -> None:
    for elem in N:
        res = []
        if 237 in elem:
            for el in elem[:elem.index(237)]:
                if el % 2 == 0:
                    res.append(el)
        print(f'результат - {res if res else "число 237 не встречается в списке"}')


if __name__ == '__main__':
    main()
