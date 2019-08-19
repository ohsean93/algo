import sys

sys.stdin = open("input.txt", "r")


def search(count_lines, size, hight):
    can_line = []
    for num in range(1, size):
        start = count_lines[num]
        end = count_lines[num + 1]
        for index in range(1, hight + 1):
            if start[index] + end[index] == 0:
                can_line.append((num, index))

    return can_line


def is_ans(exit_list, size):
    for index in range(size + 1):
        if index != exit_list[index]:
            return False
    else:
        return True


T = int(input())
for test_case in range(T):
    n, m, h = map(int, input().split())
    ans = 3
    add_line = [[0] * (h + 1) for _ in range(n + 1)]
    exit_line = list(range(n + 1))
    for _ in range(m):
        j, i = map(int, input().split())
        exit_line[i], exit_line[i + 1] = exit_line[i + 1], exit_line[i]
        add_line[i][j] = 1
        add_line[i + 1][j] = 1

    ans = ans_ans(add_line, exit_line, n, h, -1)

    if ans == 3:
        ans = -1

    print(ans)
