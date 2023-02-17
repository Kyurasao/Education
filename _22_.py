TEXT = 'Город и порт в Грузии, расположенный у побережья Чёрного моря. Порт!"@ Акцентировать'


def main(string: str) -> None:
    count = 0
    length = 0
    list_new = []
    frequently_word = ''
    longest_word = ''
    for el in string.split():
        el_new = ''
        for char in el:
            if char.isalpha():
                el_new += char.lower()
        list_new.append(el_new)

        if list_new.count(el_new) > count:
            count = list_new.count(el_new)
            frequently_word = el_new
        elif list_new.count(el_new) == count:
            frequently_word += ', ' + el_new

        if len(el_new) > length:
            length = len(el_new)
            longest_word = el_new
        elif len(el_new) == length:
            longest_word += ', ' + el_new

    print(f'{"чаще всего встречается слово:" if len(frequently_word.split()) == 1 else "чаще встречающихся слов несколько:"} {frequently_word}')
    print(f'{"слово встечается" if count == 1 else "слова встречаются"} {count} раз(а)')
    print(f'{"самое длинное слово:" if len(longest_word.split()) == 1 else "самых длинных слов несколько:"} {longest_word}')

# не знаю как тут лучше, можно ли более 2 условий в принт прописать???


if __name__ == '__main__':
    main(TEXT)
