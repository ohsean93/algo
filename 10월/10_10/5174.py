import sys

sys.stdin = open('input.txt', 'r')


def dfs(start_node):
    global cnt, linked_list, visit
    stack = [start_node]
    while stack:
        now_node = stack.pop()
        for next_node in linked_list[now_node]:
            if visit[next_node]:
                visit[next_node] = 0
                cnt += 1
                stack.append(next_node)


T = int(input())
for test_case in range(1, 1 + T):
    e, n = map(int, input().split())
    visit = [1] * (e + 2)
    cnt = 1
    linked_list = [[] for _ in range(e+2)]
    input_list = list(map(int, input().split()))
    while input_list:
        s_n, e_n = input_list[:2]
        input_list = input_list[2:]
        linked_list[s_n].append(e_n)
    dfs(n)
    print('#{} {}'.format(test_case, cnt))