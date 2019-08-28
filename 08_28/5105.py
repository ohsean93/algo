import sys

sys.stdin = open("input.txt", "r")
vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def iswall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n and (matrix[p_x][p_y] == 0 or matrix[p_x][p_y] == 3):
        return True
    return False


def bfs():
    global queue
    global ans
    while ans == 0:

        if len(queue) == 0:
            return
        p_x, p_y = queue.pop(0)
        for dal_x, dal_y in vector:
            x, y = p_x + dal_x, p_y + dal_y
            if iswall(x, y):
                queue.append((x, y))

                if matrix[x][y] == 3:
                    ans = matrix[p_x][p_y]
                    return
                else:
                    matrix[x][y] = matrix[p_x][p_y] + 1


T = int(input())
for test_case in range(T):
    ans = 0

    n = int(input())
    matrix = [0] * n
    for i in range(n):
        line = list(map(int, list(input())))

        for j, num in enumerate(line):
            if num == 2:
                start_x = i
                start_y = j
                line[j] = 4

        matrix[i] = line

    queue = [(start_x, start_y)]
    bfs()
    if ans:
        ans -= 4

    print('#{} {}'.format(test_case+1, ans))