import sys

sys.stdin = open("input.txt", "r")


def turn(array_1, n):
    return [[line[n - i-1] for line in array_1] for i in range(n)]


T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case))
    N = int(input())

    matrix = [input().split() for _ in range(N)]

    matrix_1 = turn(matrix, N)
    matrix_2 = turn(matrix_1, N)
    matrix_3 = turn(matrix_2, N)

    for i in range(N):
        print(''.join(matrix_3[i]), ''.join(matrix_2[i]), ''.join(matrix_1[i]))