import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    if m > n:
        m, n = n, m
        A, B = B, A

    max_num = 0

    for i in range(n-m+1):
        sum_num = 0
        for j in range(m):
            sum_num += A[i+j]*B[j]

        if i == 0:
            max_num = sum_num
        
        if sum_num > max_num:
            max_num = sum_num

    
    print('#{} {}'.format(test_case+1,max_num))