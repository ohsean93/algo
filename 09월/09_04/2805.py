import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, 2):
    N = int(input())
    ans = 0
    matrix = [list(map(int, list(input()))) for _ in range(N)]

    d = (N+1)//2

    for i in range(N):
        if i < d:
            temp = i + 1
        else:
            temp = (N - i)

        ans += sum(matrix[i][d-temp:d+temp-1])

    print('#{} {}'.format(test_case, ans))