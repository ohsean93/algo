# print(ord('a'))  # 97

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    L, K = map(int, input().split())
    str_origin = input()
    cost_list = [tuple(map(int, input().split())) for _ in range(K)]


    print('#{} {}'.format(test_case, ans))