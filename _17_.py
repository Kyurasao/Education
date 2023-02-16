NUM = 123456


def main(num: int) -> None:
    print(f'сумма цифр целого числа {num} = {sum(int(c) for c in str(num))}')


if __name__ == '__main__':
    main(NUM)
