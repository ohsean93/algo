import sys

sys.stdin = open("input.txt", "r")


def dfs(v):
    global ans
    global visit
    for v_next in linked_list[v]:
        if not visit[v_next]:
            dfs(v_next)
            ans.append(str(v_next))
            visit[v_next] = 1


T = int(input())
for test_case in range(T):
    v_cnt, e_cnt = map(int, input().split())
    linked_list = [[] for _ in range(v_cnt + 1)]
    visit = [0] * (v_cnt + 1)

    a = list(map(int, input().split()))

    for i in range(e_cnt):
        start_v, end_v = a[2 * i], a[2 * i + 1]
        linked_list[end_v].append(start_v)

    ans = []
    for i in range(1, v_cnt+1):
        if not visit[i]:
            dfs(i)
            ans.append(str(i))
            visit[i] = 1
        if len(ans) == v_cnt:
            break
    print('#{} {}'.format(test_case + 1, ' '.join(ans)))

