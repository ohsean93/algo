import sys

sys.stdin = open("input.txt", "r")

face = {
    'U': [0, (2, 1, 0, 1), (1, 1, 0, 1), (5, 1, 0, 1), (4, 1, 0, 1)],  # 무조건 1행
    'D': [3, (4, 3, 0, 1), (5, 3, 0, 1), (1, 3, 0, 1), (2, 3, 0, 1)],  # 무조건 3행
    'F': [1, (0, 3, 0, 1), (2, 0, 3, -1), (3, 1, 0, -1), (5, 0, 1, 1)],  # u 3행 b 1행 r 3열 l 1열
    'B': [4, (0, 1, 0, 1), (5, 0, 3, 1), (3, 3, 0, -1), (2, 0, 1, -1)],  # u 1행 b 3행 r 1열 l 3열
    'L': [2, (0, 0, 1, 1), (4, 0, 3, -1), (3, 0, 1, 1), (1, 0, 1, 1)],  # u 1열 b 3열 f 1열 b 3열
    'R': [5, (0, 0, 3, 1), (1, 0, 3, 1), (3, 0, 3, 1), (4, 0, 1, -1)],  # u 3열 b 1열 f 3열 b 1열
}


def right_turn(f_num):
    map_list = matrix[f_num].copy()
    for col in range(3):
        matrix[f_num][2 - col] = [line[col] for line in map_list]


def left_turn(f_num):
    map_list = matrix[f_num].copy()
    for col in range(3):
        matrix[f_num][col] = [line[col] for line in map_list[::-1]]


T = int(input())
for test_case in range(T):
    n = int(input())
    turn_list = input().split()
    matrix = [0] * 6
    colors = ['w', 'r', 'g', 'y', 'o', 'b']
    for i, color in enumerate(colors):
        matrix[i] = [[color]*3 for _ in range(3)]

    for i in range(n):
        info_turn = turn_list[i][0]  # 회전면
        direction = turn_list[i][1]  # 회전방향
        side_cube = [0] * 4
        for j in range(4):
            side_cube_info = face[info_turn][j + 1]
            f = side_cube_info[0]
            if side_cube_info[1] == 0:
                k = side_cube_info[2]
                if side_cube_info[3] == 1:
                    side_cube[j] = [(f, 0, k - 1), (f, 1, k - 1), (f, 2, k - 1)]
                else:
                    side_cube[j] = [(f, 2, k - 1), (f, 1, k - 1), (f, 0, k - 1)]
            else:
                k = side_cube_info[1]
                if side_cube_info[3] == 1:
                    side_cube[j] = [(f, k - 1, 0), (f, k - 1, 1), (f, k - 1, 2)]
                else:
                    side_cube[j] = [(f, k - 1, 2), (f, k - 1, 1), (f, k - 1, 0)]

        temporary = [0] * 3
        if direction == '+':
            left_turn(face[info_turn][0])
            for num in range(3):
                a, b, c = side_cube[0][num][0], side_cube[0][num][1], side_cube[0][num][2]
                temporary[num] = matrix[a][b][c]
            for index in range(1, 4):
                for num in range(3):
                    a_1, b_1, c_1 = side_cube[index-1][num][0], side_cube[index-1][num][1], side_cube[index-1][num][2]
                    a_2, b_2, c_2 = side_cube[index][num][0], side_cube[index][num][1], side_cube[index][num][2]
                    matrix[a_1][b_1][c_1] = matrix[a_2][b_2][c_2]
            for num in range(3):
                a, b, c = side_cube[3][num][0], side_cube[3][num][1], side_cube[3][num][2]
                matrix[a][b][c] = temporary[num]
        else:
            right_turn(face[info_turn][0])
            for num in range(3):
                a, b, c = side_cube[3][num][0], side_cube[3][num][1], side_cube[3][num][2]
                temporary[num] = matrix[a][b][c]
            for index in range(3, 0, -1):
                for num in range(3):
                    a_1, b_1, c_1 = side_cube[index][num][0], side_cube[index][num][1], side_cube[index][num][2]
                    a_2, b_2, c_2 = side_cube[index-1][num][0], side_cube[index-1][num][1], side_cube[index-1][num][2]
                    matrix[a_1][b_1][c_1] = matrix[a_2][b_2][c_2]
            for num in range(3):
                a, b, c = side_cube[0][num][0], side_cube[0][num][1], side_cube[0][num][2]
                matrix[a][b][c] = temporary[num]

    for p in range(3):
        print(''.join(matrix[0][p]))