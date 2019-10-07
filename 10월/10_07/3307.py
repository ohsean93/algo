import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    max_cnt = min_cnt = k = 0


    ans = max_cnt + min_cnt

    print('#{} {}'.format(test_case, ans))