import sys

sys.stdin = open("input.txt", "r")
vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(hieght):
    while queue:
        p_x, p_y = queue.pop(0)
        for dal_x, dal_y in vector:
            x, y = p_x + dal_x, p_y + dal_y
            if is_wall(x, y):
                if matrix[x][y] > hieght and visit[x][y] == 0:
                    visit[x][y] = 1
                    queue.append((x, y))


def is_wall(p_x, p_y):
    if 0 <= p_x < N and 0 <= p_y < N:
        return True
    return False


N = int(input())
matrix = [0] * N
min_num = 100
max_num = 0

for i in range(N):
    line = list(map(int, input().split()))
    matrix[i] = line
    a = min(line)
    b = max(line)
    if min_num > a:
        min_num = a
    if max_num < b:
        max_num = b

queue = []
ans = 1
for h in range(min_num, max_num):
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > h and visit[i][j] == 0:
                queue.append((i, j))
                visit[i][j] = 1
                bfs(h)
                cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)