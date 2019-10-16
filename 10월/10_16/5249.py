import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    v += 1
    matrix = [[0] * v for _ in range(v)]
    min_w = 11
    linked_list = {i: set() for i in range(v)}
    first_edge = (0, 0)

    for __ in range(e):
        s_n, e_n, w = map(int, input().split())
        matrix[s_n][e_n] = w
        matrix[e_n][s_n] = w
        linked_list[s_n].add(e_n)
        linked_list[e_n].add(s_n)
        if w < min_w:
            min_w = w
            first_edge = (s_n, e_n)

    s_n_1, s_n_2 = first_edge
    all_node = set(first_edge)
    checker = v - 2
    sum_num = min_w
    while checker:
        min_w = 11
        for now_node in all_node:
            for next_node in (linked_list[now_node] - all_node):
                w = matrix[now_node][next_node]
                if w < min_w:
                    min_w = w
                    add_node = next_node
        all_node.add(add_node)
        sum_num += min_w

        checker -= 1

    print('#{} {}'.format(test_case, sum_num))

