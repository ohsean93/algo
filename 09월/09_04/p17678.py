import sys

sys.stdin = open("input.txt", "r")


def change_min(h, m):
    return h * 60 + m


case = int(input())
for test_case in range(1, case + 1):
    N, T, M = map(int, input().split())

    times = [change_min(*tuple(map(int, time.split(':')))) for time in input().split()]

    bus_list = [9*60 + T * i for i in range(N)]
    times.sort()

    answer = 0

    can_go_list = [M * (N - i) for i in range(N)]
    waiting_list = [0] * (1441)

    for time in times:
        for num in range(time, 1441):
            waiting_list[num] += 1

    temp = 0
    for i, time in enumerate(bus_list):
        if can_go_list[i] <= waiting_list[time] - temp:
            target_num = can_go_list[i]
            answer = time
            while waiting_list[answer] - temp >= target_num:
                answer -= 1
            break
        elif i == N - 1:
            answer = time
            break
        temp += min(waiting_list[time], M)

    print('{}:{}'.format(str(answer//60).zfill(2), str(answer%60).zfill(2)))