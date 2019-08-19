import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1,11):
    input()
    max_num = 0
    matrix = [[]] * 100
    for line_num in range(100):
        line = list(map(int,input().split()))
        sum_num = 0
        for num in line:
            sum_num += num
        if sum_num > max_num:
            max_num = sum_num
        matrix[line_num] = line

    for col_num in range(100):
        col = [line[col_num] for line in matrix]
        sum_num = 0
        for num in col:
            sum_num += num
        if sum_num > max_num:
            max_num = sum_num

    cross_line = [[matrix[i][i] for i in range(100)], [matrix[i][99-i] for i in range(100)]]

    for cl in cross_line:
        
        sum_num = 0
        for num in cl:
            sum_num += num
        if sum_num > max_num:
            max_num = sum_num

    print("#{} {}".format(test_case,max_num))
    

