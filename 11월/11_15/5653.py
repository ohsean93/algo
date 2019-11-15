import sys

sys.stdin = open('input.txt', 'r')


def is_wall(p_x, p_y):
    if 0 <= p_x < N and 0 <= p_y < M:
        return True
    return False


# 바이러스의 상태(0:비활성, n:활성, -1:사망)
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    M = 2 * k + m
    N = 2 * k + n
    base_line = [0] * M
    attach_line = [0] * k
    matrix = [[0] * M for _ in range(N)]
    live_vi = 0
    active_vi = []
    dead_vi = dict()

    status = dict()

    for i in range(n):
        line = list(map(int, input().split()))
        for j, num in enumerate(line):
            if num:
                live_vi += 1
                if status.get(num):
                    status[num].append((i + k, j + k))
                else:
                    status[num] = [(i + k, j + k)]
        matrix[k + i] = attach_line.copy() + line + attach_line.copy()

    t = 0
    spread_vi = dict()
    while t != k:
        new_vi = 0
        dead = 0
        t += 1
        if status.get(t):
            active_vi = status[t]
        else:
            active_vi = []
        for key, value in spread_vi.items():
            new_vi += 1
            num = value + t
            if status.get(num):
                status[num].append(key)
            else:
                status[num] = [key]
            matrix[key[0]][key[1]] = value

        spread_vi = dict()
        for vi_x, vi_y in active_vi:
            num = matrix[vi_x][vi_y]
            temp = num + t
            if dead_vi.get(temp):
                dead_vi[temp].append((vi_x, vi_y))
            else:
                dead_vi[temp] = [(vi_x, vi_y)]
            for d_x, d_y in vector:
                n_x, n_y = vi_x + d_x, vi_y + d_y
                if is_wall(n_x, n_y) and matrix[n_x][n_y] == 0:
                    if spread_vi.get((n_x, n_y)):
                        temp = spread_vi[(n_x, n_y)]
                        if temp >= num:
                            continue
                    spread_vi[(n_x, n_y)] = num

        if dead_vi.get(t):
            dead = len(dead_vi[t])

        live_vi = live_vi - dead + new_vi
    print('#{} {}'.format(test_case, live_vi))