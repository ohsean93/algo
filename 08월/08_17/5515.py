import sys

sys.stdin = open("input.txt", "r")

add_month = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

T = int(input())
for test_case in range(T):
    m, d = map(int, input().split())
    ans = (add_month[m-1] + d + 3) % 7

    print('#{} {}'.format(test_case + 1, ans))