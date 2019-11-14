import sys

sys.stdin = open('input.txt', 'r')

# 상 좌 우 하
vector = ((-1, 0), (0, -1), (0, 1), (1, 0))
pipe = ((), (0, 3, 1, 2), (0, 3), (1, 2), (0, 2), (3, 2), (3, 1), (0, 1))


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < m:
        return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    n, m, s_x, s_y, time = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    visit = [[1 for _ in range(m)] for __ in range(n)]
    visit[s_x][s_y] = 0
    queue = [(s_x, s_y, 1)]
    ans = 1

    while queue:
        now_x, now_y, now_t = queue.pop(0)
        if now_t >= time:
            continue
        for d in pipe[matrix[now_x][now_y]]:
            d_x, d_y = vector[d]
            next_x, next_y = now_x + d_x, now_y + d_y

            if is_wall(next_x, next_y) and visit[next_x][next_y] and 3-d in pipe[matrix[next_x][next_y]]:
                visit[next_x][next_y] = 0
                queue.append((next_x, next_y, now_t + 1))
                ans += 1

    print('#{} {}'.format(test_case, ans))