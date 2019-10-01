import sys

sys.stdin = open('input.txt', 'r')

vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visit = [[1] * n for _ in range(n)]
    max_num = 0
    sp = 0

    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                cnt = 1
                stat_p = matrix[i][j]
                visit[i][j] = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    value = matrix[x][y]
                    for dx, dy in vector:
                        next_x, next_y = x + dx, y + dy
                        if is_wall(next_x, next_y) and visit[next_x][next_y]:
                            next_value = matrix[next_x][next_y]
                            if next_value == value + 1:
                                cnt += 1
                                visit[next_x][next_y] = 0
                                stack.append((next_x, next_y))
                            elif next_value == value - 1:
                                cnt += 1
                                visit[next_x][next_y] = 0
                                stack.append((next_x, next_y))
                                stat_p = next_value
                if max_num < cnt:
                    max_num = cnt
                    sp = stat_p
                elif max_num == cnt:
                    if sp > stat_p:
                        sp = stat_p

    print('#{} {} {}'.format(test_case, sp, max_num))