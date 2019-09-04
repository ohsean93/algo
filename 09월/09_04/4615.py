import sys

sys.stdin = open("input.txt", "r")
vector = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


def turn(p_x, p_y, color):
    matrix[p_x][p_y] = color
    for dal_x, dal_y in vector:
        temp = []
        x, y = p_x + dal_x, p_y + dal_y

        while is_wall(x, y):
            if matrix[x][y] == 0:
                break
            if matrix[x][y] != color:
                temp.append((x, y))
            if matrix[x][y] == color:
                for c_x, c_y in temp:
                    matrix[c_x][c_y] = color
                break
            x += dal_x
            y += dal_y


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [[0]*n for _ in range(n)]

    d = n//2 - 1
    matrix[d][d] = matrix[d+1][d+1] = 2
    matrix[d+1][d] = matrix[d][d+1] = 1

    for _ in range(m):
        i, j, c = map(int, input().split())
        turn(i-1, j-1, c)

    cnt_b, cnt_w = 0, 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                cnt_b += 1
            elif matrix[i][j] == 2:
                cnt_w += 1
    print('#{} {} {}'.format(test_case, cnt_b, cnt_w))