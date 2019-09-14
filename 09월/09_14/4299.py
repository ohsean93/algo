import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    d, h, m = map(int, input().split())
    ans = ((d - 11) * 24 * 60 + (h - 11) * 60 + m - 11)
    if ans < 0:
        ans = -1
    print('#{} {}'.format(test_case, ans))