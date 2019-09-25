import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    queue = [(0, 1, 0)]
    min_num = 100000

    while queue:
        p, visit, sum_num = queue.pop()
        for i in range(1, n):
            if (2 ** n - 1) != visit:
                if (1 << i & visit) == 0 and min_num > sum_num:
                    sum_num += matrix[p][i]
                    visit += 1 << i
                    if min_num > sum_num:
                        queue.append((i, visit, sum_num))
                    sum_num -= matrix[p][i]
                    visit -= 1 << i
            else:
                sum_num += matrix[p][0]
                if min_num > sum_num:
                    min_num = sum_num

    print('#{} {}'.format(test_case, min_num))