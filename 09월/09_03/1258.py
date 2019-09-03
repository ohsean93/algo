import sys

sys.stdin = open("input.txt", "r")
vector = [(0, 1), (1, 0)]


def is_wall(p_x, p_y):
    if 0 <= p_x < N and 0 <= p_y < N:
        if matrix[p_x][p_y]:
            return True
    return False


def find_box(p_x, p_y):
    x, y = p_x, p_y
    for dal_x, dal_y in vector:
        while is_wall(x, y):
            x += dal_x
            y += dal_y
        x -= dal_x
        y -= dal_y
    for temp_x in range(p_x, x + 1):
        for temp_y in range(p_y, y + 1):
            matrix[temp_x][temp_y] = 0
    return x - p_x + 1, y - p_y + 1


T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    boxes = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                line, col = find_box(i, j)
                boxes.append((line*col, line, col))
                ans += 1

    boxes.sort()

    print('#{} {}'.format(test_case, ans), end=' ')
    for size, line, col in boxes:
        print(line, col, end=' ')
    print()