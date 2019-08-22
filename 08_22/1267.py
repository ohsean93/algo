import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    v_cnt, e_cnt = map(int, input().split())
    input_degree = [0] * (v_cnt + 1)
    linked_list = [[] for _ in range(v_cnt + 1)]

    a = list(map(int, input().split()))

    for i in range(e_cnt):
        start_v, end_v = a[2 * i], a[2 * i + 1]
        linked_list[start_v].append(end_v)
        input_degree[end_v] += 1

    ans = []
    while True:
        for i in range(1, v_cnt+1):
            if input_degree[i] == 0:
                ans.append(str(i))
                input_degree[i] = -1
                for j in linked_list[i]:
                    input_degree[j] -= 1
                break

        if len(ans) == v_cnt:
            break

    print('#{} {}'.format(test_case + 1, ' '.join(ans)))
