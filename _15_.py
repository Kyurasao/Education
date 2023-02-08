FIRST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
SECOND = [1, 2, 3, 8, 9, 10, 11]


def main():
    print(f'результат: {list(set(FIRST) - set(SECOND))}')


if __name__ == '__main__':
    main()
