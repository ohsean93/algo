import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    h1, m1, h2, m2 = map(int,input().split())
    ans_m = (m1+m2)%60
    p = (m1+m2)//60
    ans_h = (h1+h2+p)%12
    if ans_h == 0:
        ans_h = 12

    print('#{} {} {}'.format(test_case+1, ans_h, ans_m))
