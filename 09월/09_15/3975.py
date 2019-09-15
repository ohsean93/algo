import sys

sys.stdin = open('input.txt', 'r')
ans_list = []
T = int(input())
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    checker = a * d - c * b
    ans = ''
    if checker > 0:
        ans = 'ALICE'
    elif checker < 0:
        ans = 'BOB'
    else:
        ans = 'DRAW'
    ans_list.append('#{} {}'.format(test_case, ans))

print('\n'.join(ans_list))