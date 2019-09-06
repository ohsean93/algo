import sys
sys.stdin = open('input.txt', 'r')

vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_wall(p_x, p_y, wall):
    if (0 <= p_x < n and 0 <= p_y < m) and matrix[p_x][p_y] == 0:
        if (p_x, p_y) in wall:
            pass
        else:
            return True
    return False


def dfs(p_x, p_y, wall):
    b_cnt = 0
    visit[p_x][p_y] = 1
    stack = [(p_x, p_y)]

    while stack:
        now_x, now_y = stack.pop()
        for dal_x, dal_y in vector:
            next_x = now_x + dal_x
            next_y = now_y + dal_y
            if is_wall(next_x, next_y, wall) and visit[next_x][next_y] == 0:
                visit[next_x][next_y] = 1
                stack.append((next_x, next_y))
                b_cnt += 1
    return b_cnt


def conbi(use_list):
    if use_list:
        start = use_list[-1] + 1
    else:
        start = 0
    for next_node in range(start, k):
        next_list = use_list + [next_node]
        if len(next_list) == 3:
            wall_list.append([can_wall[p] for p in next_list])
        else:
            conbi(next_list)


n, m = map(int, input().split())
bi = []
matrix = [0] * n
can_wall = []
wall_list = []
score = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            bi.append((i, j))
        elif line[j] == 1:
            pass
        else:
            can_wall.append((i, j))
            cnt += 1
    matrix[i] = line

k = len(can_wall)
conbi([])
max_num = 0
for case in wall_list:
    visit = [[0 for __ in range(m)] for _ in range(n)]
    case_live = cnt - 3
    for x, y in bi:
        case_live -= dfs(x, y, case)
    if case_live:
        if max_num < case_live:
            max_num = case_live

print(max_num)
