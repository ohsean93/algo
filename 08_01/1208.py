import sys

sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    list_block = list(map(int, input().split()))

    list_count = [0] * 101
    min_num, max_num = 100, 0
    for i in list_block:
        list_count[i] += 1
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i

    for try_num in range(n):
        list_count[max_num] -= 1
        list_count[max_num - 1] += 1

        if list_count[max_num] == 0:
            max_num -= 1

        list_count[min_num] -= 1
        list_count[min_num + 1] += 1

        if list_count[min_num] == 0:
            min_num += 1

    ans = max_num - min_num
    print('#{} {}'.format(test_case, ans))
