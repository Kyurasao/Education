LIST_OF_NUMBERS = [1, 10, 30, 5, 45]


def main(list_1: list) -> None:
    print(f'элементы кратные 15: {list(filter(lambda x: (x % 15 == 0), list_1))}')


if __name__ == '__main__':
    main(LIST_OF_NUMBERS)
    # принято. Огонь!