# L[0:N//2], L[N//2:N]
import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(input_list, n_num):
    global cnt
    if n_num == 1:
        return input_list

    d = n_num//2
    L_list, R_list = merge_sort(input_list[0:d], d), merge_sort(input_list[d:n_num], n_num - d)
    if L_list[-1] > R_list[-1]:
        cnt += 1

    output_list = [0] * n_num
    i = j = 0
    while (i != d) and (j != n_num - d):
        if L_list[i] < R_list[j]:
            output_list[i + j] = L_list[i]
            i += 1
        else:
            output_list[i + j] = R_list[j]
            j += 1
    if i == d:
        while j != n_num - d:
            output_list[i + j] = R_list[j]
            j += 1
    else:
        while i != d:
            output_list[i + j] = L_list[i]
            i += 1

    return output_list


T = int(input())
for test_case in range(1, T + 1):
    cnt = 0
    n = int(input())
    origin_list = list(map(int, input().split()))
    a = merge_sort(origin_list, n)[n//2]
    print('#{} {} {}'.format(test_case, a, cnt))
