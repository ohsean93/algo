import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1,int(input()) + 1):
    n = int(input())
    num_list = list(map(int,input().split()))
    for i in range(10):
        if i % 2:
            for j in range(n - 2, i-1, -1):
                if num_list[j] > num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        else:
            for j in range(n - 2, i-1, -1):
                if num_list[j] < num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]


    print('#{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}'.format(test_case,num_list[0],num_list[1],num_list[2],num_list[3],num_list[4],num_list[5],num_list[6],num_list[7],num_list[8],num_list[9]))