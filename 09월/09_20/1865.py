import sys
sys.stdin = open('input.txt', 'r')

def dfs(rate_num, deep):
    global matrix, visit, ans
    if rate_num <= ans:
        return
    m = deep
    if m == n:
        if ans < rate_num:
            ans = rate_num
    else:
        for i in range(n):
            if visit[i]:
                visit[i] = 0
                dfs(rate_num * matrix[m][i]/100, deep + 1)
                visit[i] = 1


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    visit = [1] * n
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dfs(1, 0)
    # ans = ans * 10**(-2 * (n-1))

    print('#{} {:0.6f}'.format(test_case, 100 * ans))