import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    bus_stop = list(map(int, input().split()))

    n = bus_stop.pop(0)
    ans = n
    stack = [(0, bus_stop[0], 0)]
    while stack:
        visit, can_go, cnt = stack.pop()
        if cnt > ans:
            continue
        if visit + can_go >= n - 1:
            if ans > cnt:
                ans = cnt
            continue
        cnt += 1
        for i in range(visit + 1, min(n - 1, visit + can_go + 1)):
            stack.append((i, bus_stop[i], cnt))
    print('#{} {}'.format(test_case, ans))