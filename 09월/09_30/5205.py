import sys

sys.stdin = open('input.txt', 'r')


def quick_sort(r_num, l_num):
    if r_num >= l_num:
        return
    global num_list
    dr = r_num + 1
    dl = l_num
    p = num_list[r_num]
    while True:
        while p < num_list[dl] and dl > r_num:
            dl -= 1
        while p >= num_list[dr] and dr < l_num:
            dr += 1
        if dr < dl:
            num_list[dl], num_list[dr] = num_list[dr], num_list[dl]
        else:
            break

    num_list[r_num], num_list[dl] = num_list[dl], num_list[r_num]
    quick_sort(r_num, dl-1)
    quick_sort(dl+1, l_num)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    quick_sort(0, n-1)
    print('#{} {}'.format(test_case, num_list[n//2]))