import sys

sys.stdin = open('input.txt', 'r')


def dfs(start_node):
    global visit, linked_list
    stack = [start_node]
    while stack:
        now_node = stack.pop()
        for next_node in linked_list[now_node]:
            if visit[next_node]:
                visit[next_node] = 0
                stack.append(next_node)


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    linked_list = [[] for _ in range(n+1)]
    visit = [1] * (n + 1)
    cnt = 0

    input_list = list(map(int, input().split()))
    while input_list:
        s_n, e_n = input_list[:2]
        input_list = input_list[2:]
        linked_list[s_n].append(e_n)
        linked_list[e_n].append(s_n)

    for node in range(1, n+1):
        if visit[node]:
            visit[node] = 0
            dfs(node)
            cnt += 1

    print('#{} {}'.format(test_case, cnt))