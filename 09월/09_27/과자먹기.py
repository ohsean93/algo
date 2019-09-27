# import sys
#
# sys.stdin = open('input_2.txt', 'r')

from itertools import permutations


def d(p1_x, p1_y, p2_x, p2_y):
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)


T = int(input())
for test_case in range(1, T + 1):
    t = input()
    robot = []
    cookie = []
    min_num = 1200

    for i in range(10):
        line = list(map(int, input().split()))
        for j, num in enumerate(line):
            if num:
                if num == 9:
                    robot.append((i, j))
                else:
                    cookie.append((i, j))
    # print(robot, cookie)

    for case in permutations(cookie, 6):
        sum_num = 0
        for i in range(6):
            sum_num += d(*case[i], *robot[i])
        if min_num > sum_num:
            min_num = sum_num
    print('#{} {}'.format(test_case, min_num))