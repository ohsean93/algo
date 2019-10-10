def dfs(start_node):
    stack = [start_node]
    while stack:
        now_node = stack.pop()


T = int(input())
for test_case in range(1, 1 + T):
    e, n = map(int, input().split())
    visit = [1] * (e + 2)
    input_list = list(map(int, input().split()))
    while input_list:
        s_n, e_n = input_list[]
