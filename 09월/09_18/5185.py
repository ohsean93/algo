import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, origin_str = input().split()
    n = int(n)
    num = int(origin_str, 16)
    ans = bin(num)[2:]
    checker = len(ans) % n
    if checker:
        ans = ('0' * (n - checker)) + ans
    print('#{} {}'.format(test_case, ans))