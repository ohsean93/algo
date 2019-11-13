import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
vector = ((0, 1), (1, 0), (0, -1), (-1, 0))


def is_wall(p_x, p_y):
    if 0 <= p_x < n and 0 <= p_y < n:
        return True
    return False


for test_case in range(1, T+1):
    n, k = map(int, input().split())
    highest = 0
    highest_location = []
    matrix = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        matrix[i] = line
        for j, num in enumerate(line):
            if highest < num:
                highest = num
                highest_location = [(i, j, 0, 1, highest, [(i, j)])]
            elif highest == num:
                highest_location.append((i, j, 0, 1, highest, [(i, j)]))

    queue = highest_location.copy()
    longest_len = 1

    while queue:
        x, y, digging, len_path, now_high, visit = queue.pop()
        for d_x, d_y in vector:
            n_x, n_y = x + d_x, y + d_y
            if is_wall(n_x, n_y):
                if (n_x, n_y) in visit:
                    continue
                next_visit = visit.copy()
                next_visit.append((n_x, n_y))
                next_high = matrix[n_x][n_y]
                if next_high < now_high:
                    queue.append((n_x, n_y, digging, len_path + 1, next_high, next_visit))
                    if longest_len < len_path + 1:
                        longest_len = len_path + 1
                elif digging == 0:
                    for dig in range(1, k+1):
                        dig_high = next_high - dig
                        if dig_high < now_high:
                            queue.append((n_x, n_y, 1, len_path + 1, dig_high, next_visit))
                            if longest_len < len_path + 1:
                                longest_len = len_path + 1
                            break

    print(test_case, longest_len)
