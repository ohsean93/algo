import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    max_num = sum(score[-k:])
    print('#{} {}'.format(test_case, max_num))
