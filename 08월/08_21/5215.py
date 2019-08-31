import sys

sys.stdin = open("input.txt", "r")
ans = 0


def find(now_num, cal, good):

    global ans
    if good > ans:
        ans = good

    for num in range(now_num + 1, n):
        good += ham_list[num][0]
        cal += ham_list[num][1]
        if cal <= k:
            find(num, cal, good)
        good -= ham_list[num][0]
        cal -= ham_list[num][1]


T = int(input())
for test_case in range(T):
    n, k = map(int, input().split())

    ham_list = [0] * n
    for i in range(n):
        t, c = map(int, input().split())
        ham_list[i] = (t, c)

    find(-1, 0, 0)

    print('#{} {}'.format(test_case + 1, ans))
