import sys

sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(T):
    ans = 0
    queue = []
    linked_list = [[] for _ in range(101)]
    condition_list = [0] * 101

    e, s_v = map(int, input().split())
    queue.append(s_v)
    condition_list[s_v] = 1
    e_list = list(map(int, input().split()))
    for i in range(e//2):
        linked_list[e_list[2 * i]].append(e_list[2 * i + 1])

    while len(queue) != 0:
        now_v = queue.pop(0)
        for next_v in linked_list[now_v]:
            if condition_list[next_v] == 0:
                queue.append(next_v)
                condition_list[next_v] = condition_list[now_v] + 1
                ans = condition_list[next_v]

    ans_list = []
    for i, num in enumerate(condition_list):
        if num == ans:
            ans_list.append(i)

    print('#{} {}'.format(test_case+1, ans_list[-1]))