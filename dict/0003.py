"""
0003
Исправьте ошибки в коде, что бы получить требуемый вывод.

# данный код
d1 = {"a": 100. "b": 200. "c":300}
d2 = {a: 300, b: 200, d:400}
print(d1["b"] == d2["b"])
# требуемый вывод:
# True
"""

D1 = {"a": 100, "b": 200, "c": 300}
D2 = {'a': 300, 'b': 200, 'd': 400}

# результат типа None будет, правильно?


def main(d1, d2: dict) -> None:
    print(d1["b"] == d2["b"])


if __name__ == '__main__':
    main(D1, D2)
