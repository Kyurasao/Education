FIRST = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SECOND = [0, 2, 3, 15, 8, 9, 10, 11]


def main():
    for el_2 in SECOND:
        print(f'2й список - текущий элемент - {el_2}')
        if el_2 in FIRST:
            print(f'список FIRST до удаления - {FIRST}')
            FIRST.remove(el_2)
            print(f'список FIRST после удаления - {FIRST}')
    print(f'список FIRST - результат - {FIRST}')

if __name__ == '__main__':
    main()
