"""
0006
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
"""


def main() -> None:
    for i in range(1, 6):
        print(f'№ {i} - {"0" * 30}')


if __name__ == '__main__':
    main()