import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):
    n = int(input())
    num_list = list(map(int,input().split()))
    for i in range(n):
        for j in range(n-2,i-1,-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    print('#{}'.format(test_case+1),end=' ')
    for i in range(n):
        if i == n-1:
            print(num_list[i])
        else:
            print(num_list[i],end=' ')
                