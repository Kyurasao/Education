VAR_1 = 'Классическая музыка!'
VAR_2 = 23


def main(var_1, var_2) -> None:
    print(f'значения переменных до: var_1 = {var_1}, var_2 = {var_2}')
    (var_1, var_2) = (var_2, var_1)
    print(f'значения переменных после: var_1 = {var_1}, var_2 = {var_2}')


if __name__ == '__main__':
    main(VAR_1, VAR_2)
    # принято
