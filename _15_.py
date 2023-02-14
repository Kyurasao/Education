FIRST = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SECOND = [0, 2, 3, 8, 9, 10, 11]


def main():
    j = 0
    # for el_1 in FIRST:
    while j < len(FIRST):
        # print(f'1й - {el_1}')
        print(f'1й - {FIRST[j]}')
        i = 0
        while i < len(SECOND):
        # for el_2 in SECOND:
            # print(f'2й - {el_2}')
            print(f'2й - {SECOND[i]}')
            # if el_1 == el_2:
            if FIRST[j] == SECOND[i]:
                print(f'el_1 - {FIRST[j]}')
                # print(f'el_2 - {el_2}')
                print(f'i = {i}')
                print(f'el_2 - {SECOND[i]}')
                # FIRST.remove(el_1)
                # SECOND.remove(el_2)
                FIRST.remove(FIRST[j])
                SECOND.remove(SECOND[i])
                print(f'FIRST - {FIRST}')
                print(f'SECOND - {SECOND}')
                print(f'el_1 - {FIRST[j]}')
                print(f'i = {i}')
                print(f'el_2 - {SECOND[i]}')
            else:
                i += 1
        j += 1
    print(FIRST)

if __name__ == '__main__':
    main()
