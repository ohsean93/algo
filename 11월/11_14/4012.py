import sys

sys.stdin = open('input.txt', 'r')

from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    d = n//2
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = 10000 * d ** 2

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] += matrix[j][i]

    for case in combinations(list(range(1, n)), d - 1):
        case_sum = 0
        another_case = []
        for num in range(1, n):
            if num not in case:
                another_case.append(num)
        case = [0] + list(case)

        for i in range(d):
            for j in range(i + 1, d):
                case_sum += matrix[case[i]][case[j]]
                case_sum -= matrix[another_case[i]][another_case[j]]

        case_sum = abs(case_sum)

        if ans > case_sum:
            ans = case_sum
            if ans == 0:
                break

    print('#{} {}'.format(test_case, ans))