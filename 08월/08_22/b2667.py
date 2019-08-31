import sys

sys.stdin = open("input.txt", "r")

udrl = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(p_x, p_y):
    global cnt
    for dal_x, dal_y in udrl:
        x, y = p_x + dal_x, p_y + dal_y
        if is_wall(x, y):
            if matrix[x][y]:
                cnt += 1
                matrix[x][y] = 0
                dfs(x, y)


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


ans = []

n = int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = list(map(int, list(input())))


for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            matrix[i][j] = 0
            cnt = 1
            dfs(i, j)
            ans.append(cnt)

ans.sort()

print(len(ans))
for num in ans:
    print(num)

