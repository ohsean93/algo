import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    time_list = [list(map(int, input().split()))[::-1] for _ in range(n)]
    time_list = sorted(time_list,reverse=True)
    ans = 0
    start_time = 0

    while time_list:
        et, st = time_list.pop()
        if st >= start_time:
            start_time = et
            ans += 1
    print('#{} {}'.format(test_case, ans))