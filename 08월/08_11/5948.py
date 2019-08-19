import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(T):
    max_num_list = [0]*6
    
    num_list = list(map(int,input().split()))
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                sum_num = num_list[i] + num_list[j] + num_list[k]

                if sum_num in max_num_list:
                    continue
                max_num_list[5] = sum_num
                for index in range(4, -1, -1):
                    if max_num_list[index] < max_num_list[index+1]:
                        max_num_list[index], max_num_list[index+1] = max_num_list[index+1], max_num_list[index]
                    else:
                        break

    print('#{} {}'.format(test_case+1, max_num_list[4]))