import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    visit = [1] * n
    linked_list = [[] for _ in range(n)]
    for __ in range(m):
        n_1, n_2 = map(int, input().split())
        linked_list[n_1 - 1].append(n_2 - 1)
        linked_list[n_2 - 1].append(n_1 - 1)

    cnt = 0
    for i in range(n):
        if visit[i]:
            cnt += 1
            visit[i] = 0
            stack = [i]
            while stack:
                node = stack.pop()
                for next_node in linked_list[node]:
                    if visit[next_node]:
                        visit[next_node] = 0
                        stack.append(next_node)
    print('#{} {}'.format(test_case, cnt))