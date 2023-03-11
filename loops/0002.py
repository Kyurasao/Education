"""
Евгению предоставили строку, состоящую из русских букв разных регистров, и попросили очистить ее от заглавных литер.
Как ему показалось, он написал верный код, но результат совсем не порадовал.
Ниже представлен пример работы «чистильщика строк», которому срочно требуется ваша помощь.

Пример – IDE
----
letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'

for letter in letters:
____if letter.upper() = letters:
________letters.replace(letter, '')

print(letters)
"""

LETTERS = 'ЫгВЫоЯСремДШНККАыкЩЙФа'


def main(string: str) -> None:
    print(f'Исходная строка: {string},\n'
          f'После обработки: {"".join([letter for letter in string if not letter.isupper()])}')


if __name__ == '__main__':
    main(LETTERS)
