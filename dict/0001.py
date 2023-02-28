"""
0001
Выведите значение возраста из словаря.

# данный код
person = {"name": "Kelly", "age":25, "city": "New york"}
# требуемый вывод:
# 25
"""

PERSON = {"name": "Kelly", "age": 25, "city": "New york"}


def main(d: dict) -> None:
    print(d.get('age'))


if __name__ == '__main__':
    main(PERSON)
