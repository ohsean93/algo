import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):

    n = int(input())
    num_list = list(map(int,input().split()))
    
    max_num = 0
    
    for i in range(n):
        for j in range(i+1,n):
            num = num_list[i] * num_list[j]
            b = num % 10
            num //= 10
            while num > 9:
                a = num % 10
                num //= 10
                if b>=a:
                    b=a:
                else:
                    break
            if num > max_num:
                max_num = num


    print('#{} {}'.format(test_case+1,max_num))