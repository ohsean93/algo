import sys

sys.stdin = open('input.txt', 'r')

vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_wall(p_x, p_y):
    if 0 <= p_x < 4 and 0 <= p_y < 4:
        return True
    return False


T = int(input())
for test_case in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    ans_list = set()
    for i in range(4):
        for j in range(4):
            stack = [(i, j, matrix[i][j])]
            while stack:
                x, y, now_str = stack.pop()
                for dx, dy in vector:
                    next_x, next_y = x + dx, y + dy
                    if is_wall(next_x, next_y):
                        next_str = now_str + matrix[next_x][next_y]
                        if len(next_str) == 7:
                            ans_list.add(next_str)
                        else:
                            stack.append((next_x, next_y, next_str))

    print('#{} {}'.format(test_case, len(ans_list)))