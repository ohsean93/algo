import sys

sys.stdin = open("input.txt", "r")
# 모든 케이스를 좌측으로 미는걸로 바꾸기 위해 회전을 한다.
direction = {
    'down': 3,
    'left': 0,
    'up': 1,
    'right': 2,
}


def turn(array):  # 좌회전
    return [[line[i] for line in array] for i in range(n-1, -1, -1)]


def step(array):
    return_list = [0] * n
    for i in range(n):
        line = array[i]
        temp = 0
        temp_list = []
        for j in range(n):
            if line[j]:
                if temp == line[j]:
                    temp_list.append(2 * temp)
                    temp = 0
                else:
                    if temp:
                        temp_list.append(temp)
                    temp = line[j]
        if temp:
            temp_list.append(temp)
        while len(temp_list) != n:
            temp_list.append(0)
        return_list[i] = temp_list
    return return_list


T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    n, d = input().split()
    n = int(n)
    d = direction[d]
    matrix = [list(map(int, input().split())) for _ in range(n)]

    for __ in range(d):
        matrix = turn(matrix)
    matrix = step(matrix)
    for __ in range((4-d)%4):
        matrix = turn(matrix)

    print('#{}'.format(test_case))
    for i in range(n):
        print(' '.join(list(map(str, matrix[i]))))