vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move(d):
    global red, blue, next_red, next_blue, matrix
    r_x, r_y = red
    b_x, b_y = blue
    r_cnt = b_cnt = 0
    dx, dy = vector[d]
    while matrix[r_x][r_y] == '.':
        r_x += dx
        r_y += dy
        r_cnt += 1
    while matrix[b_x][b_y] == '.':
        b_x += dx
        b_y += dy
        b_cnt += 1

    r_x -= dx
    r_y -= dy

    b_x -= dx
    b_y -= dy
    if r_x == b_x and b_y == r_y:
        if r_cnt > b_cnt:
            r_x -= dx
            r_y -= dy
        else:
            b_x -= dx
            b_y -= dy
    next_red = (r_x, r_y)
    next_blue = (b_x, b_y)
    if matrix[r_x][r_y] == 'O':
        return 1
    elif matrix[b_x][b_y] == 'O':
        return -1
    else:
        return 0


n, m = map(int, input().split())
matrix = [0] * n
red, blue = (0, 0)
for i in range(n):
    line = list(input())
    for j, char in enumerate(line):
        if char == 'R':
            red = (i, j)
            line[j] = '.'
        elif char == 'B':
            blue = (i, j)
            line[j] = '.'

    matrix[i] = line

ans = checker = 0
stack = [(red, blue, 0)]
while checker == 0 and ans == 0:
    red, blue, cnt = stack.pop(0)
    next_red, next_blue = red, blue
    cnt += 1
    for d in range(4):
        checker = move(d)
        if checker == 1:
            ans = cnt
            break
        elif checker == -1:
            checker = 0
        else:
            if blue != next_blue or red != next_red:
                stack.append((next_red, next_blue, cnt))
print(ans)