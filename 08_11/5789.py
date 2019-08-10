import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    n, q = map(int,input().split())
    boxs = [0]*n
    for i in range(q):
        l, r = map(int,input().split())
        for j in range(l-1,r):
            boxs[j] = i + 1


    print('#{}'.format(test_case+1),end='')
    for i in range(n):
        print(' {}'.format(boxs[i]),end='')
    print()