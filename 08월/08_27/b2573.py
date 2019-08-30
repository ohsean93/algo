import sys

sys.stdin = open("input.txt", "r")

vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_wall(p_x, p_y):
    global n, m
    if 0 <= p_x < n and 0 <= p_y < m:
        return True
    return False


def dfs(p_x, p_y):
    stack = [(p_x, p_y)]
    while True:
        if len(stack) == 0:
            return
        x, y = stack[-1]
        for dal_x, dal_y in vector:
            X, Y = x + dal_x, y + dal_y
            if is_wall(X, Y) and copy_matrix[X][Y] == 0 and matrix[X][Y]:
                stack.append((X, Y))
                copy_matrix[X][Y] = 1
                break
        else:
            stack.pop()
            continue


def search(p_x, p_y, map_list):
    cnt = 0
    for dal_x, dal_y in vector:
        X, Y = p_x + dal_x, p_y + dal_y
        if is_wall(X, Y) and map_list[X][Y] == 0:
            cnt += 1
    return cnt


n, m = map(int, input().split())
ans = 0
matrix = [0] * n
for i in range(n):
    matrix[i] = list(map(int, input().split()))

ice_list = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            ice_list.append((i, j))

ans = 0
while True:
    if len(ice_list) == 0:
        ans = 0
        break

    copy_matrix = [[0] * m for _ in range(n)]

    mass_ice = 0
    for i, j in ice_list:
        if copy_matrix[i][j] == 0:
            copy_matrix[i][j] = 1
            mass_ice += 1
            dfs(i, j)

    if mass_ice >= 2:
        break

    ans += 1
    copy_matrix = [[0] * m for _ in range(n)]

    for i, j in ice_list:
        copy_matrix[i][j] = search(i, j, matrix)

    new_ice_list = []
    for i, j in ice_list:
        a = matrix[i][j] - copy_matrix[i][j]
        if a <= 0:
            matrix[i][j] = 0
        else:
            matrix[i][j] = a
            new_ice_list.append((i, j))
    ice_list = new_ice_list

print(ans)