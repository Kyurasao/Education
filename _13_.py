N = 4


def main(n: int) -> None:
    i = 1
    summ = 0
    for el in range(1, n + 1):
        summ += n ** i
        i += 1
    print(f'сумма для N = {N}: {summ}')


if __name__ == '__main__':
    main(N)
