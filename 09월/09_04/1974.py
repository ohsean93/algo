import sys

sys.stdin = open("input.txt", "r")

start_sq = [
    (0, 0), (0, 3), (0, 6),
    (3, 0), (3, 3), (3, 6),
    (6, 0), (6, 3), (6, 6),
]
small_sq = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
]


def check(my_list):
    for char in '123456789':
        if char in my_list:
            continue
        else:
            return False
    else:
        return True


T = int(input())
for test_case in range(1, T + 1):
    ans = 1
    matrix = [input().split() for _ in range(9)]
    matrix2 = [[line[i] for line in matrix] for i in range(9)]
    for i in range(9):
        if check(matrix[i]) and check(matrix2[i]):
            continue
        else:
            ans = 0
            break
    if ans:
        for i, j in start_sq:
            temp = []
            for dal_x, dal_y in small_sq:
                temp.append(matrix[i+dal_x][j+dal_y])

            if check(temp):
                continue
            else:
                ans = 0
                break

    print('#{} {}'.format(test_case, ans))