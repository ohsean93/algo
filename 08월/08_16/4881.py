import sys


def conbi(checker, map_array, use_size, size, sum_num):
    x = use_size
    global ans
    if x == size:
        if ans > sum_num:
            ans = sum_num
    else:
        if ans < sum_num:
            return
        for ele in range(size):
            if not checker[ele]:
                checker[ele] = 1
                use_size += 1
                sum_num2 = sum_num + map_array[x][ele]
                conbi(checker, map_array, use_size, size, sum_num2)
                checker[ele] = 0
                use_size -= 1


sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(T):
    n = int(input())
    ans = 10 * n
    matrix = [0] * n

    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    check = [0] * n

    conbi(check, matrix, 0, n, 0)

    print('#{} {}'.format(test_case+1, ans))