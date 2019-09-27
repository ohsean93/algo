# import sys
#
# sys.stdin = open('input_1.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    sub_matrix = list(zip(*matrix))
    min_sum = 400000
    x = 0

    for i in range(n):
        line = matrix[i]
        for j in range(n):
            col = list(sub_matrix[j])
            col.pop(i)
            check_list = line + col

            case_num = 400000
            h = 0
            for k in range(1, 6):
                sum_num = 0
                for num in check_list:
                    sum_num += abs(k-num)
                if case_num > sum_num:
                    case_num = sum_num
                else:
                    h = k-1
                    break
            if min_sum > case_num:
                min_sum = case_num
                x = h
            elif min_sum == case_num:
                x = min(x, h)
    print('#{} {} {}'.format(test_case, min_sum, x))




