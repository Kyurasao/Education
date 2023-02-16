LIST_OF_SEQUENCE = [
    [1, 10, 30, 5, 5],
    [1, 10, 30, 5, 45],
    (0, 4, 6, 7, 9),
    (5, 6, 5, 7)
]


def main(list_1: list) -> None:
    for seq in list_1:
        print(f'числа последовательности "{seq}" {"уникальны" if len(set(seq)) == len(seq) else "не уникальны"}')


if __name__ == '__main__':
    main(LIST_OF_SEQUENCE)
