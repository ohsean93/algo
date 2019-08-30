import sys

sys.stdin = open("input.txt", "r")


def search(count_lines, size, hight):
    can_line = []
    for num in range(1, size):
        start = count_lines[num]
        end = count_lines[num + 1]
        for index in range(1, hight + 1):
            if start[index] + end[index] == 0:
                can_line.append((index, num))

    return can_line


def is_ans(exit_list, size):
    for index in range(size + 1):
        if index != exit_list[index]:
            return False
    else:
        return True


def ddd(lines, deep):
    a = deep
    b = lines

    global add_line_origin
    global exit_line_origin
    global ans
    add_line = add_line_origin.copy()
    exit_line = exit_line_origin.copy()
    for i, j in b:
        if i != 0:
            exit_line[j], exit_line[j + 1] = exit_line[j + 1], exit_line[j]
            add_line[j][i] = 1
            add_line[j + 1][i] = 1

    if is_ans(exit_line, n):
        if ans >= a:
            ans = a
        return
    else:
        for add_i, add_j in search(add_line, n, h):
            b.append((add_i, add_j))
            b.sort()
            a += 1
            if a < 4:
                ddd(b, a)
            a -= 1


T = int(input())
for test_case in range(T):
    n, m, h = map(int, input().split())
    ans = 4
    add_line_origin = [[0] * (h + 1) for _ in range(n + 1)]
    exit_line_origin = list(range(n + 1))
    line_list = [(0, 0)] * m

    for line_num in range(m):
        i, j = map(int, input().split())
        line_list[line_num] = (i, j)

    line_list.sort()
    ddd(line_list, 0)


    print(ans)



    #
    #
    #
    #
    # if is_ans(exit_line, n):
    #     print(0)
    #     continue
    #
    # else:
    #     ans = 4
    #     for i_1, j_1 in search(add_line, n, h):
    #         exit_line[i_1], exit_line[i_1 + 1] = exit_line[i_1 + 1], exit_line[i_1]
    #         add_line[i_1][j_1] = 1
    #         add_line[i_1 + 1][j_1] = 1
    #
    #         if is_ans(exit_line, n):
    #             ans = 1
    #             break
    #
    #         for i_2, j_2 in search(add_line, n, h):
    #             if ans == 2:
    #                 break
    #
    #             exit_line[i_2], exit_line[i_2 + 1] = exit_line[i_2 + 1], exit_line[i_2]
    #             add_line[i_2][j_2] = 1
    #             add_line[i_2 + 1][j_2] = 1
    #
    #             if is_ans(exit_line, n):
    #                 ans = 2
    #             else:
    #                 if ans == 4:
    #                     for i_3, j_3 in search(add_line, n, h):
    #                         if ans == 3:
    #                             break
    #                         exit_line[i_3], exit_line[i_3 + 1] = exit_line[i_3 + 1], exit_line[i_3]
    #                         add_line[i_3][j_3] = 1
    #                         add_line[i_3 + 1][j_3] = 1
    #
    #                         if is_ans(exit_line, n):
    #                             ans = 3
    #
    #                         exit_line[i_3], exit_line[i_3 + 1] = exit_line[i_3 + 1], exit_line[i_3]
    #                         add_line[i_3][j_3] = 0
    #                         add_line[i_3 + 1][j_3] = 0
    #
    #             exit_line[i_2], exit_line[i_2 + 1] = exit_line[i_2 + 1], exit_line[i_2]
    #             add_line[i_2][j_2] = 0
    #             add_line[i_2 + 1][j_2] = 0
    #
    #         exit_line[i_1], exit_line[i_1 + 1] = exit_line[i_1 + 1], exit_line[i_1]
    #         add_line[i_1][j_1] = 0
    #         add_line[i_1 + 1][j_1] = 0
    #
    # if ans == 4:
    #     ans = -1
    #
    # print(ans)
