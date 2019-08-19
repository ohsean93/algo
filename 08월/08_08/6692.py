import sys

sys.stdin = open("input.txt", "r")


for test_case in range(int(input())):
    ans = 0
    cases = int(input())
    for case in range(cases):
        x, p = map(float,input().split())
        ans += x*p

    print('#{} {}'.format(test_case+1,ans))