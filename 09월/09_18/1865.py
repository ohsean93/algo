import sys

sys.stdin = open('input.txt', 'r')


def dfs(now_num):
    global visit, max_num
    a = sum(visit)
    if a:
        for next_col in range(n):
            if visit[next_col]:
                visit[next_col] = 0
                temp = matrix[a - 1][next_col]
                next_num = now_num * temp
                dfs(next_num)
                visit[next_col] = 1
    else:
        if max_num < now_num:
            max_num = now_num


T = int(input())
for test_case in range(1, 11):
    ans = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    visit = [1] * n
    dfs(1)

    ans = max_num/(10**(2*n-2))
    print('#{} {:.6f}'.format(test_case, ans))