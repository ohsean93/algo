import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    ans = 0
    secs = int(input())
    v = 0
    for sec in range(secs):
        line = input()
        if line != '0':
            mode, a = map(int,line.split())
        else:
            mode = 0

        if mode == 0:
            ans += v
        elif mode == 1:
            v += a
            ans += v
        elif mode == 2:
            v -= a
            if v < 0:
                v = 0 
            ans += v


    print('#{} {}'.format(test_case+1,ans))