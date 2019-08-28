import sys

sys.stdin = open("input.txt", "r")


def bfs():
    global ans
    while ans == 0:
        if len(queue) == 0:
            break
        now_v = queue.pop(0)
        for next_v in linked_list[now_v]:
            if now_condition[next_v] == 0:
                now_condition[next_v] = now_condition[now_v] + 1
                queue.append(next_v)
                if next_v == e_v:
                    ans = now_condition[next_v]
                    break


T = int(input())
for test_case in range(T):
    ans = 0

    v, e = map(int, input().split())

    now_condition = [0] * (v + 1)
    linked_list = [[] for _ in range(v + 1)]

    for _ in range(e):
        s_v, e_v = map(int, input().split())
        linked_list[s_v].append(e_v)
        linked_list[e_v].append(s_v)

    s_v, e_v = map(int, input().split())

    queue = [s_v]
    now_condition[s_v] = 1
    bfs()

    if ans:
        ans -= 1

    print('#{} {}'.format(test_case+1, ans))