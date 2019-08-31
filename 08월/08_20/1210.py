import sys

sys.stdin = open("input.txt", "r")


def search(x, y, map_ladder):
    for dal_x, dal_y in [(0, 1), (0, -1)]:
        X, Y = x + dal_x, y + dal_y
        if 0 <= Y < 100:
            a = map_ladder[X][Y]
            if a == 1:
                return dal_y
    else:
        return 0


T = 10
for test_case in range(T):
    input()
    matrix = [0] * 100
    for i in range(100):
        matrix[i] = list(map(int, input().split()))

    end = 100
    line_list = []
    line_num = 0
    end = matrix[99]

    for i in range(100):
        if end[i]:
            if end[i] == 2:
                line_num = len(line_list)
            line_list.append(i)

    x = 99
    while x != 0:
        y = line_list[line_num]
        line_num += search(x, y, matrix)
        x -= 1

    print('#{} {}'.format(test_case+1, line_list[line_num]))