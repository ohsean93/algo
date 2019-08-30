import sys

sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(T):
    n = int(input())

    matrix = [0] * n
    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    cnt = 0
    for j in range(n):
        checker = 1
        for i in range(n):
            if matrix[i][j] and matrix[i][j] == checker:
                if checker == 2:
                    cnt += 1
                    checker = 1
                else:
                    checker = 2

    print('#{} {}'.format(test_case+1, cnt))