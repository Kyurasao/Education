LIST_OF_SEQUENCE = [
    [1, 10, 30, 5, 5],
    [1, 10, 30, 5, 45],
    (0, 4, 6, 7, 9),
    (5, 6, 5, 7)
]     # строки ведь не нужно добавлять в список последовательностей??


def main(list_1: list) -> None:
    for seq in list_1:
        count = 0
        for el in seq:
            count += seq.count(el)
        print(f'числа последовательности "{seq}" {"уникальны" if count == len(seq) else "не уникальны"}')
    # а какая структура данных хранит только уникальные символы?

if __name__ == '__main__':
    main(LIST_OF_SEQUENCE)
