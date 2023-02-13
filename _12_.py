NAME = [
    'aSd.Fgh.jkL.qgE',
    'aSd.jfgtyD',
    'aSd.Fgh.jkL.qwE..',
    'aSd.Fgh.jkL.qwEф',
    'aSdFghjkLqwE',
    ''
]
CHAR = 'qwertyuiopasdfghjklzxcvbnm'


def check_char(s):
    for el in s:
        if el not in CHAR:
            return False
    return True


def main():
    for el in NAME:
        if '.' in el and len(el) != el.rfind('.') + 1 and check_char(el[el.rfind('.') + 1:].lower()):
            print(f'имя файла - "{el}"; расширение файла - {el[el.rfind(".") + 1:]}')
        else:
            print(f'"{el}" - некорректное имя файла')


if __name__ == '__main__':
    main()
