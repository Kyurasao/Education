NAME = [
    'aSd.Fgh.jkL.qgE',
    'aSd.jfgtyD',
    'aSd.Fgh.jkL.qwE..',
    'aSd.Fgh.jkL.qwEф',
    'aSdFghjkLqwE',
    ''
]


def main():     # нужно ли тут указывать тип данных результата??????????
    for el in NAME:
        if '.' in el and len(el) != el.rfind('.') + 1 and el[el.rfind('.') + 1:].isalpha(): # что делает len(el) != el.rfind('.') + 1?
            print(f'имя файла - "{el}"; расширение файла - {el[el.rfind(".") + 1:]}')
        else:
            print(f'"{el}" - некорректное имя файла')


if __name__ == '__main__':
    main()
