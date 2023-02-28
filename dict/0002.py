"""
0002
Допишите словарь с ключами BMW, ВАЗ, Tesla и списками из 3х моделей в качестве значений.

# данный код
models_data = {..., "Tesla": ["Modes S", ...]}
print(models_data["Tesla"][0])
# требуемый вывод:
# Modes S
"""

MODELS_DATA = {"Tesla": ["Modes S"]}


def main(d: dict) -> None:
    d['Tesla'].append('Model Y')
    d['Tesla'].append('Model 3')
    d['BMW'] = ['M3', 'M2', 'M1']
    d['ВАЗ'] = ['2102', '2104', '2106']
    print(d["Tesla"][2])


if __name__ == '__main__':
    main(MODELS_DATA)
