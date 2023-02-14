N = 5


def main(n: int) -> int:
    summ = n + n * n + n * n * n
    print(f'сумма для N = {N}: {summ}')


if __name__ == '__main__':
    main(N)
