NAME = [
    'aSd.Fgh.jkL.qgE',
    'aSd.jfgtyD',
    'aSd.Fgh.jkL.qwE..',
    'aSd.Fgh.jkL.qwE!',
    'aSd.Fgh.jkL.qwEф',
    'aSdFghjkLqwE',
    ''
]
LATIN_CHAR = 'qwertyuiopasdfghjklzxcvbnm'


def ext_is_good(s: str) -> bool:
    if '.' in s and s.rfind('.') + 1 != len(s):
        for el in s[s.rfind('.') + 1:].lower():
            if el not in LATIN_CHAR:
                return False
        return True


def main() -> None:
    for el in NAME:
        if ext_is_good(el):
            print(f'имя файла - "{el}"; расширение файла - {el[el.rfind(".") + 1:]}')
        else:
            print(f'"{el}" - некорректное имя файла')


if __name__ == '__main__':
    main()
