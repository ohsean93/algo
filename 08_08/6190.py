import sys

sys.stdin = open("input.txt", "r")

for test_case in range(int(input())):

    n = int(input())
    num_list = list(map(int,input().split()))
    
    max_num = 0
    
    for i in range(n):
        for j in range(i+1,n):
            num = num_list[i] * num_list[j]
            list_num = list(str(num))
            for k in range(len(list_num)-1):
                if list_num[k] > list_num[k+1]:
                    break
            else:
                if num > max_num:
                    max_num = num


    print('#{} {}'.format(test_case+1,max_num))