# import sys
#
# sys.stdin = open('input_3.txt', 'r')


def d(p1_x, p1_y, p2_x, p2_y):
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)


T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    mineral = []

    for i in range(n):
        line = list(map(int, input().split()))
        for j, num in enumerate(line):
            if num:
                if num == 1:
                    robot = (i, j)
                else:
                    mineral.append((i, j, num))

    k = len(mineral)
    cost_mineral = []
    for x, y, price in mineral:
        cost = 2 * d(x, y, *robot)
        cost_mineral.append((cost, price))

    stack = [(0, 0)]
    max_price = 0

    for i in range(k):
        dc, dp = cost_mineral[i]
        next_stack = []
        for cost, price in stack:
            next_cost = dc + cost
            next_price = dp + price
            if next_cost <= c:
                next_stack.append((next_cost, next_price))
                if next_price > max_price:
                    max_price = next_price
        stack += next_stack
    print('#{} {}'.format(test_case, max_price))
