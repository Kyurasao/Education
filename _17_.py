NUM = 123456


def main(num: int) -> None:
    res = 0
    for c in str(num):
        res += int(c)
    print(f'сумма цифр целого числа {num} = {res}') 
    # а как можно сделать это же, но без цикла?


if __name__ == '__main__':
    main(NUM)
