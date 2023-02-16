NUM = 123456


def main(num: int) -> None:
    res = 0
    for c in str(num):
        res += int(c)
    print(f'сумма цифр целого числа {num} = {res}')


if __name__ == '__main__':
    main(NUM)
