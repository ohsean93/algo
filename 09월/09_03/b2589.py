import sys

sys.stdin = open("input.txt", "r")

vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_wall(p_x, p_y):
    if 0 <= p_x < N and 0 <= p_y < M:
        return True
    return False


def bfs():
    k = 0
    while queue:
        p_x, p_y = queue.pop(0)
        for dal_x, dal_y in vector:
            x, y = p_x + dal_x, p_y + dal_y
            if is_wall(x, y):
                if matrix[x][y] == 'L' and visit[x][y] == 0:
                    k = visit[x][y] = visit[p_x][p_y] + 1
                    queue.append((x, y))
    return k


N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
queue = []
ans = 0
for i in range(N):
    for j in range(M):
        local_max = 0
        if matrix[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            queue.append((i, j))
            visit[i][j] = 1
            local_max = bfs()
        if ans < local_max:
            ans = local_max


print(ans - 1)