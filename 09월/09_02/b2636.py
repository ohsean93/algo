import sys

sys.stdin = open("input.txt", "r")
vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < m:
        return True
    return False


def search(p_x, p_y):
    for dal_x, dal_y in vector:
        next_x, next_y = p_x + dal_x, p_y + dal_y
        if is_wall(next_x, next_y) and (matrix[next_x][next_y] == '2'):
            return True
    return False


def bfs():
    global queue
    while queue:
        p_x, p_y = queue.pop(0)
        matrix[p_x][p_y] = '2'
        for dal_x, dal_y in vector:
            next_x, next_y = p_x + dal_x, p_y + dal_y
            if is_wall(next_x, next_y):
                if matrix[next_x][next_y] == '0':
                    # matrix[next_x][next_y] = '2'
                    queue.append((next_x, next_y))


T = 1
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [0] * n
    one_list = []
    for i in range(n):
        line = input().split()
        matrix[i] = line
        for j in range(m):
            if line[j] == '1':
                one_list.append((i, j))
    queue = [(0, 0)]
    # matrix[0][0] = '2'
    bfs()
    c = []
    time = 0
    while len(one_list):
        time += 1
        cnt = 0
        new_one_list = []
        for i, j in one_list:
            if search(i, j):
                queue.append((i, j))
                cnt += 1
            else:
                new_one_list.append((i, j))

        for i, j in queue:
            matrix[i][j] = '2'
        # x, y = queue[0]
        # matrix[x][y] = '2'
        bfs()
        one_list = new_one_list

    print(time)
    print(cnt)