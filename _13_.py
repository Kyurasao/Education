N = 5


def main(n: int) -> int:
    summ = n + n * n + n * n * n  # как можно составить прогамму чтобы тело этой функции было в одну строку?
    print(f'сумма для N = {N}: {summ}')


if __name__ == '__main__':
    main(N)
