STRING = 'Классическая музыка!'
S = 'с'


def main(string, s: str) -> None:
    print(f'Символ "{s}" встречается в строке "{string}" {string.count(s)} раз')


if __name__ == '__main__':
    main(STRING, S)
