import sys

sys.stdin = open("input.txt", "r")


def checker(start_time, people_num, num_list, k):
    time = start_time
    while True:
        time += 10**k
        check_num = 0
        for sec in num_list:
            check_num += (time // sec)

        if check_num >= people_num:
            return time - 10**k


T = int(input())
for test_case in range(1, T + 1):
    t = 0
    n, m = map(int, input().split())
    task_list = [int(input()) for _ in range(n)]

    len_list = max(task_list) * m // n

    p = 0
    while len_list > 10**k:
        p += 1

    for i in list(range(p))[::-1]:
        t = checker(t, m, task_list, i)
    ans = t+1

    print('#{} {}'.format(test_case, ans))