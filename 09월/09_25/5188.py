import sys

sys.stdin = open('input.txt', 'r')


def is_wall(p_x, p_y):
    global matrix, n
    if 0 <= p_x < n and 0 <= p_y < n:
        return matrix[p_x][p_y]
    return 10000


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    for k in range(1, 2 * n-1):
        for i in range(n):
            j = k - i
            if is_wall(i, j) != 10000:
                temp = 10000
                matrix[i][j] += min(is_wall(i - 1, j), is_wall(i, j - 1))

    print('#{} {}'.format(test_case, matrix[n - 1][n - 1]))