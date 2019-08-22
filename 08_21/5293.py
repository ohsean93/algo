import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    a, b, c, d = map(int, input().split())
    if b == (c + 1):
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * c
    elif b == c and b != 0:
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * (c - 1) + '0'
    elif c == (b + 1):
        ans = '1' * (d + 1) + '0' * (a + 1) + '10' * b
    elif a+d == 1:
        if a:
            ans = '00'
        else:
            ans = '11'
    else:
        ans = 'impossible'

    print(ans)