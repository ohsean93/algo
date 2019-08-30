import sys


def iswell(x, y, size):
    if 0 <= x < size and 0 <= y < size:
        return True
    else:
        return False


def search(x, y, size, map_array):
    can_go = [0, 0, 0, 0]
    index_can_go = 0
    for dal_x, dal_y in udlr:
        X, Y = x + dal_x, y + dal_y
        if iswell(X, Y, size):
            if map_array[X][Y] == '0' or map_array[X][Y] == '3':
                can_go[index_can_go] = (X, Y)
                index_can_go += 1

    return can_go, index_can_go


def miro(x, y, size, map_array, g):
    global ans
    if (x, y) == g:
        ans = 1

    if ans == 1:
        return

    next_list, case_num = search(x, y, size, map_array)
    if case_num == 0:
        return
    else:
        if map_array[x][y] == '0':
            map_array[x][y] = '4'
        for X, Y in next_list[:case_num]:
            # for line in map_array:
            #     print(line)
            # print()
            miro(X, Y, size, map_array, g)
        if map_array[x][y] == '4':
            map_array[x][y] = '0'


sys.stdin = open("input.txt", "r")
udlr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for test_case in range(T):
    ans = 0
    n = int(input())
    matrix = [0] * n

    for i in range(n):
        line = list(input())
        matrix[i] = line
        for j in range(n):
            if line[j] == '3':
                end = (i, j)
            elif line[j] == '2':
                start = (i, j)

    miro(start[0], start[1], n, matrix, end)

    print('#{} {}'.format(test_case+1, ans))