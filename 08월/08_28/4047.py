import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    ans = 0

    card_count = {
        'S': [0, 13],
        'D': [0, 13],
        'H': [0, 13],
        'C': [0, 13]
    }

    cards_str = input()
    while cards_str != '':
        card = cards_str[:3]
        cards_str = cards_str[3:]
        shape = card[0]
        num = int(card[1]) * 10 + int(card[2])
        checker, cnt = card_count[shape][0], card_count[shape][1]

        if checker & (2 ** num):
            ans = 'ERROR'
            break
        else:
            checker += (2 ** num)
            card_count[shape][0] = checker
            card_count[shape][1] = cnt - 1

    if ans == 0:
        print('#{}'.format(test_case + 1), end=' ')
        for shape in 'SDHC':
            print(card_count[shape][1], end=' ')
        print()
    else:
        print('#{} {}'.format(test_case+1, ans))
