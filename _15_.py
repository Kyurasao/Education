FIRST = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SECOND = [0, 2, 3, 15, 8, 9, 10, 1, 1]


def main():
    for el_2 in SECOND:
        if el_2 in FIRST:
            FIRST.remove(el_2)
    print(f'результат - {FIRST}')


if __name__ == '__main__':
    main()
