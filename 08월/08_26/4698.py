import sys

sys.stdin = open("input.txt", "r")
prim_num = [1] * (10**6 + 1)
prim_num[0] = 0
prim_num[1] = 0
for num in range(2, 1000):
    if prim_num[num]:
        for i in range(2 * num, 10**6+1, num):
            prim_num[i] = 0

T = int(input())
for test_case in range(T):
    cnt = 0
    d, a, b = map(int, input().split())
    d = str(d)
    for num in range(a, b+1):
        if prim_num[num]:
            if d in str(num):
                cnt += 1

    print('#{} {}'.format(test_case+1, cnt))