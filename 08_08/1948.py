import sys

sys.stdin = open("input.txt", "r")
#            1  2  3  4  5  6   7  8  9 10 11 12
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]

for test_case in range(int(input())):
    start_m, start_d, end_m, end_d = map(int,input().split())
    ans = 0

    for m in range(start_m,end_m):
        ans += month_day[m-1]

    ans = ans + end_d - start_d + 1

    print('#{} {}'.format(test_case+1,ans))