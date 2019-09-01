import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    ans = 0
    str_origin = input().replace('()', 'r')

    cnt = 0
    for char in str_origin:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
            ans += 1
        else:
            ans += cnt

    print('#{} {}'.format(test_case+1, ans))