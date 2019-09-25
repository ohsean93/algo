import sys

sys.stdin = open('input.txt', 'r')


def baby_jin(num_list):
    if sum(num_list) < 3:
        return False
    if max(num_list) == 3:
        return True
    for i in range(8):
        if num_list[i] * num_list[i + 1] * num_list[i + 2]:
            return True


T = int(input())
for test_case in range(1, T+1):
    p = [[0] * 10, [0] * 10]
    card_list = list(map(int, input().split()))
    checker = 0

    card_list.reverse()
    ans = 0
    while card_list:
        num = card_list.pop()
        p[checker][num] += 1
        if baby_jin(p[checker]):
            ans = checker+1
            break
        checker += 1
        checker %= 2
    print('#{} {}'.format(test_case, ans))