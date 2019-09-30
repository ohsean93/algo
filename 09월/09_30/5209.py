import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    stack = [(0, 0, 0)]
    ans = 1500

    while stack:
        visit, cost, deep = stack.pop()
        if cost > ans:
            continue
        if deep == n:
            if cost < ans:
                ans = cost
            continue
        for i in range(n):
            if visit & 1 << i == 0:
                next_cost = cost + matrix[deep][i]
                next_visit = visit + (1 << i)
                if next_cost < ans:
                    stack.append((next_visit, next_cost, deep + 1))
    print('#{} {}'.format(test_case, ans))