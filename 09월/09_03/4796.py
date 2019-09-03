# 이 문제는 인풋 이슈가 있어 정답 확인이 불가하다.

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) - 1
    ans = 0
    i = 0
    a_1 = a_2 = a_3 = 0
    for num in input().split():
        if i == 0:
            a_1 = int(num)
        elif i == 1:
            a_2 = int(num)
        elif i == 2:
            a_3 = int(num)
            if a_1 < a_2 and a_3 < a_2:
                ans += 1
        else:
            a_1, a_2, a_3 = a_2, a_3, int(num)
            if a_1 < a_2 and a_3 < a_2:
                ans += 1
        i += 1

    print('#{} {}'.format(test_case, ans))