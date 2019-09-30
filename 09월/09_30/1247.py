import sys

sys.stdin = open('input.txt', 'r')


def d(p1_x, p1_y, p2_x, p2_y):
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    point_list = []
    for i, num in enumerate(map(int, input().split())):
        if i % 2:
            point_list.append((temp, num))
        else:
            temp = num

    matrix = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(i, n + 2):
            matrix[i][j] = matrix[j][i] = d(*point_list[i], *point_list[j])

    min_cost = 30000
    stack = [(0, 0, 0)]
    while stack:
        visit, cost, last_point = stack.pop()
        if visit == (2**n - 1):
            next_cost = cost + matrix[last_point][1]
            if next_cost < min_cost:
                min_cost = next_cost
            continue
        if cost >= min_cost:
            continue
        for i in range(n):
            if visit & (1 << i) == 0:
                next_point = i + 2
                next_visit = visit + (1 << i)
                next_cost = cost + matrix[last_point][i+2]
                if next_cost < min_cost:
                    stack.append((next_visit, next_cost, next_point))

    print('#{} {}'.format(test_case, min_cost))