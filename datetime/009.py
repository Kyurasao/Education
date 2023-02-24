"""
Задача 9
Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
"""

import datetime


def main() -> None:
    now = datetime.datetime.now()
    print(f'Текущее время (в формате: день:час:минута:секунда): {now.strftime("%d:%H:%M:%S")}')


if __name__ == '__main__':
    main()
